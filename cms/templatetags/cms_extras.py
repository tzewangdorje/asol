from django import template
import re

register = template.Library()

@register.filter(name='makeUrl')
def makeUrl(article):
    return article.makeUrl()

@register.filter(name='tel')
def tel(number):
    return re.sub('[^0-9]', '', number)

@register.filter(name='icon')
def icon(type):
    if type == "twitter":
        return "social foundicon-twitter"
    if type == "facebook":
        return "social foundicon-facebook"
    elif type == "email":
        return "gen-enclosed foundicon-mail"
    elif type == "facebook":
        return "gen-enclosed foundicon-idea"
    elif type == "website":
        return "gen-enclosed foundicon-website"
    elif type == "phone":
        return "gen-enclosed foundicon-phone"
    else:
        return "gen-enclosed foundicon-idea"
    


