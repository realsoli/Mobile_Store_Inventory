from django.urls import path
from . import views

urlpatterns = [
    path('', views.PhoneListView.as_view(), name='list_phone'),
    path('phone-add/', views.AddPhoneView.as_view(), name='add_phone'),
    path('phone/<slug:slug>/edit/', views.EditPhoneView.as_view(), name='edit_phone'),
    path('phone/<slug:slug>/delete/', views.DeletePhoneView.as_view(), name='delete_phone'),

    path('phone-color/', views.AddColorView.as_view(), name='add_color'),
    path('edit-color/<slug:slug>/', views.EditColorView.as_view(), name='edit_color'),
    path('delete-color/<slug:slug>/', views.DeleteColorView.as_view(), name='delete_color'),

    path('phone-brand/', views.AddBrandView.as_view(), name='add_brand'),
    path('edit-brand/<slug:slug>/', views.EditBrandView.as_view(), name='edit_brand'),
    path('delete-brand/<slug:slug>/', views.DeleteBrandView.as_view(), name='delete_brand'),

    path('phone-country/', views.AddCountryView.as_view(), name='add_country'),
    path('edit-country/<slug:slug>/', views.EditCountryView.as_view(), name='edit_country'),
    path('delete-country/<slug:slug>/', views.DeleteCountryView.as_view(), name='delete_country'),

]
