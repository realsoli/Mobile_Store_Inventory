from django.contrib.auth.mixins import PermissionRequiredMixin
from django.db.models import Q
from django.shortcuts import redirect
from django.views import View
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
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


class AddPhoneView(CreateView):
    model = Phone
    form_class = PhoneForm
    template_name = 'mobile_inventory/add_phone.html'
    success_url = reverse_lazy('list_phone')  # آدرس صفحه بعد از ذخیره موفق

    def dispatch(self, *args, **kwargs):
        # بررسی اینکه حداقل یک برند، رنگ و کشور در دیتابیس وجود داشته باشد
        if not Brand.objects.exists() or not Color.objects.exists() or not Country.objects.exists():
            return redirect('add_brand')  # اگر یکی از آن‌ها وجود نداشت، به صفحه افزودن برند بازگردانده شود
        return super().dispatch(*args, **kwargs)


# -------------------------------------------------------------------

class AddBrandView(CreateView):
    model = Brand
    form_class = BrandForm
    template_name = 'mobile_inventory/add_brand.html'
    success_url = reverse_lazy('add_color')  # آدرس صفحه بعد از ذخیره موفق

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['brands'] = Brand.objects.all()  # اضافه کردن لیست برند ها به context
        return context


class EditBrandView(UpdateView):
    model = Brand
    form_class = BrandForm
    template_name = 'mobile_inventory/edit_brand.html'
    success_url = reverse_lazy('add_brand')  # آدرس برگشت بعد از ویرایش


class DeleteBrandView(DeleteView):
    model = Brand
    template_name = 'mobile_inventory/delete_brand.html'
    success_url = reverse_lazy('add_brand')  # آدرس برگشت بعد از ویرایش


# ---------------------------------------------------------------


class AddColorView(CreateView):
    model = Color
    form_class = ColorForm
    template_name = 'mobile_inventory/add_color.html'
    success_url = reverse_lazy('add_country')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['colors'] = Color.objects.all()  # اضافه کردن لیست رنگ‌ها به context
        return context


class EditColorView(UpdateView):
    model = Color
    form_class = ColorForm
    template_name = 'mobile_inventory/edit_color.html'
    success_url = reverse_lazy('add_color')  # آدرس برگشت بعد از ویرایش


class DeleteColorView(DeleteView):
    model = Color
    template_name = 'mobile_inventory/delete_color.html'
    success_url = reverse_lazy('add_color')


# -------------------------------------------------------------------


class AddCountryView(CreateView):
    model = Country
    form_class = CountryForm
    template_name = 'mobile_inventory/add_country.html'
    success_url = reverse_lazy('add_phone')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['countries'] = Country.objects.all()
        return context


class EditCountryView(UpdateView):
    model = Country
    form_class = CountryForm
    template_name = 'mobile_inventory/edit_country.html'
    success_url = reverse_lazy('add_country')


class DeleteCountryView(DeleteView):
    model = Country
    template_name = 'mobile_inventory/delete_country.html'
    success_url = reverse_lazy('add_country')
