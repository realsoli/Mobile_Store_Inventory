from django.urls import path
from . import views

urlpatterns = [
    path('phones/', views.PhoneListView.as_view(), name='list_phone'),
    path('phone-add/', views.AddPhoneView.as_view(), name='add_phone'),

    path('phone-color/', views.AddColorView.as_view(), name='add_color'),
    path('edit-color/<int:pk>/', views.EditColorView.as_view(), name='edit_color'),
    path('delete-color/<int:pk>/', views.DeleteColorView.as_view(), name='delete_color'),

    path('phone-brand/', views.AddBrandView.as_view(), name='add_brand'),
    path('edit-brand/<int:pk>/', views.EditBrandView.as_view(), name='edit_brand'),
    path('delete-brand/<int:pk>/', views.DeleteBrandView.as_view(), name='delete_brand'),

    path('phone-country/', views.AddCountryView.as_view(), name='add_country'),
    path('edit-country/<int:pk>/', views.EditCountryView.as_view(), name='edit_country'),
    path('delete-country/<int:pk>/', views.DeleteCountryView.as_view(), name='delete_country'),

]
