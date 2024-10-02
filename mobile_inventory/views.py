from django.contrib.auth.mixins import PermissionRequiredMixin, UserPassesTestMixin
from django.db.models import Q, F
from django.shortcuts import redirect
from django.views import View
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import JsonResponse
from .models import Brand, Phone, Country, Color
from .forms import BrandForm, PhoneForm, CountryForm, ColorForm
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib import messages


class SuperUserRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser


class PhoneListView(ListView):
    model = Phone
    template_name = 'mobile_inventory/phone_list.html'
    context_object_name = 'phones'
    ordering = ['-created_at']
    paginate_by = 6

    def get_queryset(self):
        queryset = Phone.objects.all().order_by('-created_at')

        # دریافت پارامترهای جستجو
        query = self.request.GET.get('query', None)
        brand_name = self.request.GET.get('brand_name', None)
        report_type = self.request.GET.get('report_type', None)

        # گزارش برندهای کره‌ای
        if report_type == 'korean_brands':
            queryset = queryset.filter(brand__nationality='Korea')

        # گزارش موبایل‌های برند مشخص
        elif report_type == 'brand_phones' and brand_name:
            queryset = queryset.filter(brand__name__icontains=brand_name)

        # گزارش موبایل‌هایی که ملیت برند با کشور سازنده برابر است
        elif report_type == 'matching_nationality':
            queryset = queryset.filter(brand__nationality=F('country_of_manufacture__name'))

        # جستجو بر اساس مدل، برند یا ملیت برند
        if query:
            queryset = queryset.filter(
                Q(model__icontains=query) |
                Q(brand__name__icontains=query) |
                Q(brand__nationality__icontains=query)
            )

        return queryset


class AddPhoneView(SuperUserRequiredMixin, CreateView):
    model = Phone
    form_class = PhoneForm
    template_name = 'mobile_inventory/add_phone.html'
    success_url = reverse_lazy('list_phone')  # آدرس صفحه بعد از ذخیره موفق

    # permission_required = 'mobile_inventory.add_phone'


class EditPhoneView(SuperUserRequiredMixin, UpdateView):
    model = Phone
    form_class = PhoneForm
    template_name = 'mobile_inventory/edit_phone.html'
    success_url = reverse_lazy('list_phone')

    # def form_valid(self, form):
    #     messages.success(self.request, 'گوشی با موفقیت ویرایش شد.')
    #     return super().form_valid(form)


class DeletePhoneView(SuperUserRequiredMixin, DeleteView):
    model = Phone
    # template_name = 'mobile_inventory/delete_phone.html'
    success_url = reverse_lazy('list_phone')


# -------------------------------------------------------------------

class AddBrandView(SuperUserRequiredMixin, CreateView):
    model = Brand
    form_class = BrandForm
    template_name = 'mobile_inventory/add_brand.html'

    # def form_valid(self, form):
    #     messages.success(self.request, 'برند با موفقیت اضافه شد.')
    #     return super().form_valid(form)

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return reverse_lazy('add_brand')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['brands'] = Brand.objects.all().order_by('-created_at')  # اضافه کردن لیست برند ها به context
        return context


class EditBrandView(SuperUserRequiredMixin, UpdateView):
    model = Brand
    form_class = BrandForm
    template_name = 'mobile_inventory/edit_brand.html'

    # def form_valid(self, form):
    #     messages.success(self.request, 'برند با موفقیت ویرایش شد.')
    #     return super().form_valid(form)

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return reverse_lazy('add_brand')


class DeleteBrandView(SuperUserRequiredMixin, DeleteView):
    model = Brand
    # template_name = 'mobile_inventory/delete_brand.html'
    success_url = reverse_lazy('add_brand')  # آدرس برگشت بعد از حذف


# ---------------------------------------------------------------


class AddColorView(SuperUserRequiredMixin, CreateView):
    model = Color
    form_class = ColorForm
    template_name = 'mobile_inventory/add_color.html'

    # def form_valid(self, form):
    #     messages.success(self.request, 'رنگ با موفقیت اضافه شد.')
    #     return super().form_valid(form)

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return reverse_lazy('add_color')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['colors'] = Color.objects.all().order_by('-created_at')  # اضافه کردن لیست رنگ‌ها به context
        return context


class EditColorView(SuperUserRequiredMixin, UpdateView):
    model = Color
    form_class = ColorForm
    template_name = 'mobile_inventory/edit_color.html'

    # def form_valid(self, form):
    #     messages.success(self.request, 'رنگ با موفقیت ویرایش شد.')
    #     return super().form_valid(form)

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return reverse_lazy('add_color')


class DeleteColorView(SuperUserRequiredMixin, DeleteView):
    model = Color
    template_name = 'mobile_inventory/delete_color.html'
    success_url = reverse_lazy('add_color')


# -------------------------------------------------------------------


class AddCountryView(SuperUserRequiredMixin, CreateView):
    model = Country
    form_class = CountryForm
    template_name = 'mobile_inventory/add_country.html'

    # success_url = reverse_lazy('add_phone')
    # def form_valid(self, form):
    #     messages.success(self.request, 'کشور با موفقیت اضافه شد.')
    #     return super().form_valid(form)

    def get_success_url(self):
        next_url = self.request.GET.get('next', reverse_lazy('add_country'))  # بررسی پارامتر 'next'
        return next_url

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['countries'] = Country.objects.all().order_by('-created_at')
        return context


class EditCountryView(SuperUserRequiredMixin, UpdateView):
    model = Country
    form_class = CountryForm
    template_name = 'mobile_inventory/edit_country.html'

    # def form_valid(self, form):
    #     messages.success(self.request, 'کشور با موفقیت ویرایش شد.')
    #     return super().form_valid(form)

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return reverse_lazy('add_country')  # به‌دست آوردن شناسه کشور ویرایش شده


class DeleteCountryView(SuperUserRequiredMixin, DeleteView):
    model = Country
    template_name = 'mobile_inventory/delete_country.html'
    success_url = reverse_lazy('add_country')
