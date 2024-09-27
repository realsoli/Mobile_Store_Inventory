from django.contrib.auth.mixins import PermissionRequiredMixin
from django.db.models import Q
from django.views import View
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from django.http import JsonResponse
from .models import Brand, Phone, Country, Color
from .forms import BrandForm, PhoneForm, CountryForm, ColorForm


class PhoneListView(ListView):
    model = Phone
    template_name = 'mobile_inventory/phone_list.html'
    context_object_name = 'phones'

    def get_queryset(self):
        queryset = Phone.objects.all()

        query = self.request.GET.get('query', None)
        if query:
            queryset = queryset.filter(
                Q(model__icontains=query) |
                Q(brand__name__icontains=query) |
                Q(brand__nationality__icontains=query)
            )  # جستجو بر اساس مدل، برند یا ملیت برند
        return queryset


class AddBrandView(CreateView):
    model = Brand
    form_class = BrandForm
    template_name = 'mobile_inventory/add_brand.html'
    success_url = reverse_lazy('list_phone')  # آدرس صفحه بعد از ذخیره موفق


class AddCountryView(CreateView):
    model = Country
    from_class = CountryForm
    template_name = 'mobile_inventory/add_country.html'
    success_url = reverse_lazy('add_phone')


class AddColorView(CreateView):
    model = Color
    from_class = ColorForm
    template_name = 'mobile_inventory/add_color.html'
    success_url = reverse_lazy('add_phone')


class AddPhoneView(CreateView):
    model = Phone
    form_class = PhoneForm
    template_name = 'mobile_inventory/add_phone.html'
    success_url = reverse_lazy('list_phone')  # آدرس صفحه بعد از ذخیره موفق


class PhonesByBrandView(View):
    def get(self, request, brand_name):
        phones = Phone.objects.filter(brand__name=brand_name).values('model', 'price')
        return JsonResponse(list(phones), safe=False)
