from django.contrib import admin
from .models.month import Month
from .models.per_member import PerMember
from .models.member import Member
# Register your models here.

class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'membership',)

admin.site.register(Month)
admin.site.register(PerMember)
admin.site.register(Member, MemberAdmin)

