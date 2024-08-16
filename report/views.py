from django.shortcuts import render, get_object_or_404
from unidecode import unidecode
from django.http import JsonResponse
from django.core.serializers import serialize
import json
from rest_framework import status
from controller.models.credit import Credit
from controller.models.others_credit import OthersCredit
from controller.models.debit import Debit
from admin_settings.models.member import Member
from admin_settings.models.month import Month
from collections import defaultdict
from django.db.models import Sum, Max

# Create your views here.

def report_view(request):
    key = request.GET.get('key')
    content = {}
    value = key
    un_value = unidecode(value)
    content['code'] = un_value
    return JsonResponse(content, status=status.HTTP_200_OK)


def all_credits(request):
    months = list(Month.objects.values('id', 'name'))
    members = list(Member.objects.values('id', 'name'))

    # Initialize report_data with defaultdict
    report_data = defaultdict(lambda: defaultdict(lambda: {'amount': 0, 'booster_amount': 0}))

    # Initialize total counters
    total_amount = 0
    total_booster_amount = 0

    # Fetch all credits
    credits = Credit.objects.all()
    for credit in credits:
        member_id = credit.member.id
        month_id = credit.month.id
        # Aggregate amount and booster_amount
        report_data[member_id][month_id]['amount'] += credit.amount
        if credit.enable_booster_amount:
            report_data[member_id][month_id]['booster_amount'] += credit.booster_amount

        # Update total counters
        total_amount += credit.amount
        if credit.enable_booster_amount:
            total_booster_amount += credit.booster_amount

    # Fetch other credits
    other_credits = OthersCredit.objects.all()
    total_other_credits = sum(oc.amount for oc in other_credits)

    # Grand totals
    grand_total_amount = total_amount + total_other_credits
    grand_total_booster_amount = total_booster_amount

    # Sum of Grand Total Amount and Grand Total Booster Amount
    combined_total = grand_total_amount + grand_total_booster_amount

    # Convert defaultdict to a regular dict for JSON serialization
    report_data_serializable = {member_id: dict(month_data) for member_id, month_data in report_data.items()}

    context = {
        'months': months,
        'members': members,
        'report_data': report_data_serializable,
        'total_amount': total_amount,
        'total_booster_amount': total_booster_amount,
        'total_other_credits': total_other_credits,
        'grand_total_amount': grand_total_amount,
        'grand_total_booster_amount': grand_total_booster_amount,
        'combined_total': combined_total,
    }

    return render(request, 'report/report.html', context)


def individual_credits(request, member_id):
    member = get_object_or_404(Member, id=member_id)
    members = Member.objects.all()

    credits = Credit.objects.filter(member__id=member_id).values(
        'month__name'
    ).annotate(
        total_amount=Sum('amount'),
        total_booster_amount=Sum('booster_amount'),
        latest_paid_at=Max('paid_at')
    ).order_by('month__id')

    # Calculate overall totals
    overall_totals = Credit.objects.filter(member__id=member_id).aggregate(
        total_amount=Sum('amount'),
        total_booster_amount=Sum('booster_amount')
    )
    overall_sum = (overall_totals['total_amount'] or 0) + (overall_totals['total_booster_amount'] or 0)

    context = {
        'member': member,
        'members': members,
        'credits': credits,
        'overall_totals': overall_totals,
        'overall_sum': overall_sum
    }

    return render(request, 'report/individual.html', context)

def current_balance(request):
    total_credits = Credit.objects.aggregate(
        total_amount=Sum('amount'),
        total_booster_amount=Sum('booster_amount')
    )
    total_others_credits = OthersCredit.objects.aggregate(
        total_amount=Sum('amount')
    )
    total_debits = Debit.objects.aggregate(
        total_amount=Sum('amount')
    )

    total_credit_amount = (total_credits['total_amount'] or 0) + (total_credits['total_booster_amount'] or 0)
    overall_credit_total = total_credit_amount + (total_others_credits['total_amount'] or 0)
    balance = overall_credit_total - (total_debits['total_amount'] or 0)
    debits = Debit.objects.all()

    context = {
        'debits': debits,
        'total_credit_amount': total_credit_amount,
        'total_others_credits': total_others_credits['total_amount'] or 0,
        'overall_credit_total': overall_credit_total,
        'total_debits': total_debits['total_amount'] or 0,
        'balance': balance
    }

    return render(request, 'report/current_balance.html', context)