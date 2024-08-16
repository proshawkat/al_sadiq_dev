from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_GET
from .models import PerMember, Member

# Create your views here.
@require_GET
def get_must_pay(request):
    member_id = request.GET.get('member_id')
    if member_id:
        try:
            member = Member.objects.get(id=member_id)
            per_member = PerMember.objects.get(id=member.id)
            must_pay = per_member.monthly_amount * member.membership
            return JsonResponse({'must_pay': must_pay})
        except (Member.DoesNotExist, PerMember.DoesNotExist):
            pass
    return JsonResponse({'must_pay': 0})