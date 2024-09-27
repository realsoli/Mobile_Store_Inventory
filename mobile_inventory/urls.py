from django.urls import path
from . import views

urlpatterns = [
    path('phones/', views.PhoneListView.as_view(), name='list_phone'),
    path('phone-add/', views.AddPhoneView.as_view(), name='add_phone'),
    path('phone-brand/', views.AddBrandView.as_view(), name='add_brand'),
    path('phone-country/', views.AddCountryView.as_view(), name='add_country'),
    path('phone-color/', views.AddColorView.as_view(), name='add_color'),
]
