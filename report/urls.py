from django.urls import path
from .views import *

urlpatterns = [
    path('all/', all_credits, name='all_credits'),
    path('view_v/', report_view, name='report'),
    path('current_balance/', current_balance, name='current_balance'),
    path('member/<int:member_id>/', individual_credits, name='member_wise_credit'),
]
