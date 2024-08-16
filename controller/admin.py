from django.contrib import admin
from .models.credit import Credit
from .models.others_credit import OthersCredit
from .models.debit import Debit
# Register your models here.

class CreditAdmin(admin.ModelAdmin):
    readonly_fields = ('must_pay',)
    list_display = ('member', 'month', 'amount','booster_amount',)

    class Media:
        js = ('js/admin_custom.js',)

class OthersCreditAdmin(admin.ModelAdmin):
    list_display = ('source', 'month', 'amount',)

class DebitAdmin(admin.ModelAdmin):
    list_display = ('source', 'month', 'amount',)

admin.site.register(Credit, CreditAdmin)
admin.site.register(OthersCredit, OthersCreditAdmin)
admin.site.register(Debit, DebitAdmin)
