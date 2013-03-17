from django.http import HttpResponse, Http404
from django.template import RequestContext, loader

from cms.models import Partner, Article

def _getModels(title=None):
    try:
        if title:
            article = Article.objects.select_related().get(title_url=title)
        else:
            article = Article.objects.select_related().latest(field_name="date_published")
    except Article.DoesNotExist:
        raise Http404("Nope, I'm sorry, but I couldn't find that page.")
    partners = Partner.objects.select_related().all().order_by('?')
    recentStories = list(Article.objects.select_related().exclude(title_url=title).exclude(story=0).order_by('-date_published'))
    photoStories = None
    if article.article_type == "text":
        template = loader.get_template('cms/article_text.html')
    elif article.article_type == "photo":
        template = loader.get_template('cms/article_photo.html')
        photoStories = list(Article.objects.select_related().all().filter(article_type="photo").exclude(title_url=title))
        photoStories.insert(0, article) # now add our chosen article to the top of the stack so it displays first
    elif article.article_type == "youtube":
        template = loader.get_template('cms/article_youtube.html')
    else:
        pass # error, raise exception?
    print recentStories[0].article_type
    return article, partners, recentStories, photoStories, template
    
def home(request):
    article, partners, recentStories, photoStories, template = _getModels()
    context = RequestContext(request, {
        'partners': partners,
        'article': article,
        'recentStories': recentStories,
        'photoStories': photoStories
    })
    return HttpResponse(template.render(context))

def article(request, title):
    article, partners, recentStories, photoStories, template = _getModels(title)
    context = RequestContext(request, {
        'partners': partners,
        'article': article,
        'recentStories': recentStories,
        'photoStories': photoStories
    })
    return HttpResponse(template.render(context))

