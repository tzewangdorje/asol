from django.http import HttpResponse
from django.template import RequestContext, loader

from cms.models import Partner, Article

def index(request):
    return HttpResponse("Index")

def article(request, title):
    partners = Partner.objects.select_related().all()
    article = Article.objects.select_related().get(title_url=title)
    recentStories = Article.objects.select_related().exclude(title_url=title).order_by('date_published')
    photoStories = None
    if article.article_type == "text":
        template = loader.get_template('cms/article_text.html')
    elif article.article_type == "photo":
        template = loader.get_template('cms/article_photo.html')
        photoStories = Article.objects.select_related().all().filter(article_type="photo")
    elif article.article_type == "youtube":
        template = loader.get_template('cms/article_youtube.html')
    else:
        # something went wrong! Raise exception?
        pass
    context = RequestContext(request, {
        'partners': partners,
        'article': article,
        'recentStories': recentStories,
        'photoStories': photoStories,
    })
    return HttpResponse(template.render(context))

