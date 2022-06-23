from django import template
from schedule_app.models import adddate
from schedule_app.views import *

register = template.Library()

@register.simple_tag
def my_tag():
    return('!!!!!!!!!!')


