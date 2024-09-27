from django import template

register = template.Library()


@register.filter(name='add_class')
def add_class(field, css_clss):
    return field.as_widget(attrs={'class': css_clss})


@register.filter(name='three_digits_currency')
def three_digits_currency(value: int):
    return '{:,}'.format(value) + ' تومان'
