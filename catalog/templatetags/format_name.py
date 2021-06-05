from django import template

register = template.Library()


@register.filter(name="format_name")
def format_name(value):
    names = value
    reversed_name = names[::-1]
    return ", ".join(reversed_name)
