from django import template

register = template.Library()

@register.filter
def index(indexable, i):
    return indexable[i]

@register.simple_tag
def call_method(obj, method_name, *args):
    method = getattr(obj, method_name)
    return method(*args)