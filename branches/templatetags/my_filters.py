from django import template

register = template.Library()

@register.filter(name='upper_text')
def upper_text(value):
    """فلتر خاص يحول الحروف إلى حروف كبيرة (كبس لوتش)"""
    if value:
        return value.upper()
    return value