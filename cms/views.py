from django.http import HttpResponse
from django.template import RequestContext, loader

from cms.models import Partner

def index(request):
    return HttpResponse("Index")

def article(request, title):
    partners = Partner.objects.select_related().all()
    template = loader.get_template('cms/article.html')
    context = RequestContext(request, {
        'partners': partners,
    })
    return HttpResponse(template.render(context))

