from django.http import HttpResponse
from django.template import RequestContext, loader

from cms.models import Partner, Article

def index(request):
    return HttpResponse("Index")

def article(request, title):
    partners = Partner.objects.select_related().all()
    article = Article.objects.select_related().get(title_url=title)
    recentStories = Article.objects.select_related().exclude(title_url=title).order_by('date_published')
    template = loader.get_template('cms/article.html')
    context = RequestContext(request, {
        'partners': partners,
        'article': article,
        'recentStories': recentStories
    })
    return HttpResponse(template.render(context))

