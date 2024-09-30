$(document).ready(function () {
    // دکمه حذف برند
    $('.delete-brand').click(function (e) {
        e.preventDefault();
        var brandId = $(this).data('id');  // دریافت شناسه برند

        Swal.fire({
            title: 'آیا مطمئن هستید؟',
            text: "این برند حذف خواهد شد!",
            icon: 'warning',
            showCancelButton: true,
            confirmButtonColor: '#3085d6',
            cancelButtonColor: '#d33',
            confirmButtonText: 'بله، حذف کن!',
            cancelButtonText: 'لغو'
        }).then((result) => {
            if (result.isConfirmed) {
                // ارسال درخواست AJAX برای حذف برند
                $.ajax({
                    url: "/delete-brand/" + brandId + "/",  // استفاده از آدرس URL با id برند
                    type: 'POST',
                    data: {
                        'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(),  // استفاده از توکن CSRF
                    },
                    success: function (response) {
                        Swal.fire(
                            'حذف شد!',
                            'برند با موفقیت حذف شد.',
                            'success'
                        );
                        // حذف ردیف برند از جدول
                        $('#brand-row-' + brandId).remove();
                         // بررسی اینکه آیا جدولی باقی نمانده است
                        if ($('#brands-table tbody tr').length === 0) {
                            $('#brands-table tbody').html(`
                                <tr>
                                    <td colspan="10" style="text-align: center;">
                                        <div class="alert alert-warning">
                                            <p>هیچ محصولی یافت نشد</p>
                                        </div>
                                    </td>
                                </tr>
                            `);
                        }
                    },
                    error: function (xhr, status, error) {
                        Swal.fire(
                            'خطا!',
                            'مشکلی در حذف برند پیش آمد.',
                            'error'
                        );
                    }
                });
            }
        });
    });
});
// -----------------------------------

// نمایش پیش‌نمایش تصویر
$(document).ready(function () {
    // نمایش پیش‌نمایش تصویر
    document.getElementById('imageInput').onchange = function (e) {
        const reader = new FileReader();
        reader.onload = function (event) {
            const imgElement = document.getElementById('imagePreview');
            imgElement.src = event.target.result;
            imgElement.style.display = 'block';
        };
        reader.readAsDataURL(e.target.files[0]);
    };

    // وقتی گزینه برند تغییر کند
    $('#id_brand').change(function () {
        var brandId = $(this).val(); // شناسه برند انتخاب شده
        $('#editBrandLink').attr('href', '/edit-brand/' + brandId + '/?next=' + window.location.pathname);
    });

    // وقتی گزینه رنگ تغییر کند
    $('#id_color').change(function () {
        var colorId = $(this).val(); // شناسه رنگ انتخاب شده
        $('#editColorLink').attr('href', '/edit-color/' + colorId + '/?next=' + window.location.pathname);
    });

    // وقتی گزینه کشور تغییر کند
    $('#id_country_of_manufacture').change(function () {
        var countryId = $(this).val(); // شناسه کشور انتخاب شده
        $('#editCountryLink').attr('href', '/edit-country/' + countryId + '/?next=' + window.location.pathname);
    });
});

// دکمه حذف
$(document).ready(function () {
    // دکمه حذف گوشی
    $('.delete-phone').click(function (e) {
        e.preventDefault();
        var phoneId = $(this).data('id');  // دریافت شناسه موبایل

        Swal.fire({
            title: 'آیا مطمئن هستید؟',
            text: "این گوشی حذف خواهد شد!",
            icon: 'warning',
            showCancelButton: true,
            confirmButtonColor: '#3085d6',
            cancelButtonColor: '#d33',
            confirmButtonText: 'بله، حذف کن!',
            cancelButtonText: 'لغو'
        }).then((result) => {
            if (result.isConfirmed) {
                // ارسال درخواست AJAX برای حذف گوشی
                $.ajax({
                    url: "/phone/" + phoneId + "/delete/",  // استفاده از آدرس URL صحیح
                    type: 'POST',
                    data: {
                        'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(),  // استفاده از توکن CSRF
                    },
                    success: function (response) {
                        Swal.fire(
                            'حذف شد!',
                            'گوشی با موفقیت حذف شد.',
                            'success'
                        );
                        // حذف ردیف گوشی از جدول
                        $('#phone-row-' + phoneId).remove();

                        // بررسی اینکه آیا جدولی باقی نمانده است
                        if ($('#phones-table tbody tr').length === 0) {
                            $('#phones-table tbody').html(`
                                <tr>
                                    <td colspan="10" style="text-align: center;">
                                        <div class="alert alert-warning">
                                            <p>هیچ محصولی یافت نشد</p>
                                        </div>
                                    </td>
                                </tr>
                            `);
                        }
                    },
                    error: function (xhr, status, error) {
                        Swal.fire(
                            'خطا!',
                            'مشکلی در حذف گوشی پیش آمد.',
                            'error'
                        );
                    }
                });
            }
        });
    });
});


$(document).ready(function () {
    // دکمه حذف رنگ
    $('.delete-color').click(function (e) {
        e.preventDefault();
        var colorId = $(this).data('id');  // دریافت شناسه رنگ

        Swal.fire({
            title: 'آیا مطمئن هستید؟',
            text: "این رنگ حذف خواهد شد!",
            icon: 'warning',
            showCancelButton: true,
            confirmButtonColor: '#3085d6',
            cancelButtonColor: '#d33',
            confirmButtonText: 'بله، حذف کن!',
            cancelButtonText: 'لغو'
        }).then((result) => {
            if (result.isConfirmed) {
                // ارسال درخواست AJAX برای حذف رنگ
                $.ajax({
                    url: "/delete-color/" + colorId + "/",  // استفاده از آدرس URL با id رنگ
                    type: 'POST',
                    data: {
                        'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(),  // استفاده از توکن CSRF
                    },
                    success: function (response) {
                        Swal.fire(
                            'حذف شد!',
                            'رنگ با موفقیت حذف شد.',
                            'success'
                        );
                        // حذف ردیف رنگ از جدول
                        $('#color-row-' + colorId).remove();

                         // بررسی اینکه آیا جدولی باقی نمانده است
                        if ($('#colors-table tbody tr').length === 0) {
                            $('#colors-table tbody').html(`
                                <tr>
                                    <td colspan="10" style="text-align: center;">
                                        <div class="alert alert-warning">
                                            <p>هیچ محصولی یافت نشد</p>
                                        </div>
                                    </td>
                                </tr>
                            `);
                        }
                    },

                    error: function (xhr, status, error) {
                        Swal.fire(
                            'خطا!',
                            'مشکلی در حذف رنگ پیش آمد.',
                            'error'
                        );
                    }
                });
            }
        });
    });
});


$(document).ready(function () {
    // دکمه حذف رنگ
    $('.delete-country').click(function (e) {
        e.preventDefault();
        var countryId = $(this).data('id');  // دریافت شناسه رنگ

        Swal.fire({
            title: 'آیا مطمئن هستید؟',
            text: "این کشور حذف خواهد شد!",
            icon: 'warning',
            showCancelButton: true,
            confirmButtonColor: '#3085d6',
            cancelButtonColor: '#d33',
            confirmButtonText: 'بله، حذف کن!',
            cancelButtonText: 'لغو'
        }).then((result) => {
            if (result.isConfirmed) {
                // ارسال درخواست AJAX برای حذف کشور
                $.ajax({
                    url: "/delete-country/" + countryId + "/",  // استفاده از آدرس URL با id کشور
                    type: 'POST',
                    data: {
                        'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(),  // استفاده از توکن CSRF
                    },
                    success: function (response) {
                        Swal.fire(
                            'حذف شد!',
                            'کشور با موفقیت حذف شد.',
                            'success'
                        );
                        // حذف ردیف کشور از جدول
                        $('#country-row-' + countryId).remove();

                         // بررسی اینکه آیا جدولی باقی نمانده است
                        if ($('#countries-table tbody tr').length === 0) {
                            $('#countries-table tbody').html(`
                                <tr>
                                    <td colspan="10" style="text-align: center;">
                                        <div class="alert alert-warning">
                                            <p>هیچ محصولی یافت نشد</p>
                                        </div>
                                    </td>
                                </tr>
                            `);
                        }
                    },

                    error: function (xhr, status, error) {
                        Swal.fire(
                            'خطا!',
                            'مشکلی در حذف کشور پیش آمد.',
                            'error'
                        );
                    }
                });
            }
        });
    });
});