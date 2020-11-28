from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('deposit/', views.deposit),
    path('deposit/depositmoney/', views.depositmoney),
    path('withdraw/', views.withdraw),
    path('withdraw/withdrawmoney/', views.withdrawmoney),
]
