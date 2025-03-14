from django import template
register = template.Library()


@register.filter
def get_item(dictionary, key):
    return dictionary.get(int(key), "") if isinstance(dictionary, dict) else ""
