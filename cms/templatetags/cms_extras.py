from django import template

register = template.Library()

@register.filter(name='makeUrl')
def makeUrl(article):
    return article.makeUrl()


