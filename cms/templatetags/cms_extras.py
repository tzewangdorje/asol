from django import template
import re

register = template.Library()

@register.filter(name='makeUrl')
def makeUrl(article):
    return article.makeUrl()

@register.filter(name='tel')
def tel(number):
    return re.sub('[^0-9]', '', number)


