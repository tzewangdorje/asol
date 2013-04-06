from django.http import HttpResponse, Http404
from django.template import RequestContext, loader

from cms.models import Partner, Article

def _getModels(title=None):
    try:
        if title:
            article = Article.objects.select_related().get(title_url=title)
        else:
            article = Article.objects.select_related().exclude(article_type="link").exclude(story=0).latest(field_name="date_published")
    except Article.DoesNotExist:
        raise Http404("Nope, I'm sorry, but I couldn't find that page.")
    partners = Partner.objects.select_related().all().order_by('?')
    recentStories = list(Article.objects.select_related().
                         exclude(title=article.title).
                         exclude(story=0).order_by('-date_published'))
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
    return article, partners, recentStories, photoStories, template

def _getFromTo(page, recentStories):
    page = int(page)
    fromPage = 3*page
    toPage = 3*(page+1)
    if len(recentStories[fromPage:toPage])<3:
        nextPage = None
    else:
        nextPage = page + 1
    pageBack = page - 1
    return fromPage, toPage, nextPage, pageBack
    
def home(request):
    article, partners, recentStories, photoStories, template = _getModels()
    pageFrom, pageTo, page, pageBack = _getFromTo(page=0, recentStories=recentStories)
    context = RequestContext(request, {
        'partners': partners,
        'article': article,
        'recentStories': recentStories[pageFrom:pageTo],
        'photoStories': photoStories,
        'gallery': "False",
        'page': page,
        'pageBack': pageBack
    })
    return HttpResponse(template.render(context))

def article(request, title):
    article, partners, recentStories, photoStories, template = _getModels(title)
    pageFrom, pageTo, page, pageBack = _getFromTo(page=0, recentStories=recentStories)
    context = RequestContext(request, {
        'partners': partners,
        'article': article,
        'recentStories': recentStories[pageFrom:pageTo],
        'photoStories': photoStories,
        'gallery': "False",
        'page': page,
        'pageBack': pageBack
    })
    return HttpResponse(template.render(context))

def gallery(request):
    partners = Partner.objects.select_related().all().order_by('?')
    recentStories = list(Article.objects.select_related().exclude(story=0).order_by('-date_published'))
    photoStories = list(Article.objects.select_related().all().filter(article_type="photo"))
    col=0
    cols = [[],[],[]] # list of 3 lists to hold photos for the three columns
    for photo in photoStories:
        cols[col].append(photo)
        col = col+1
        if col==3:
            col=0
    template = loader.get_template('cms/gallery.html')
    context = RequestContext(request, {
        'partners': partners,
        'recentStories': recentStories,
        'photoStories': photoStories,
        'colOne': cols[0],
        'colTwo': cols[1],
        'colThree': cols[2],
        'gallery': "True",
    })
    return HttpResponse(template.render(context))

def ajaxLoadStories(request, title_url, page):
    template = loader.get_template('cms/ajaxLoadStories.html')
    recentStories = list(Article.objects.select_related().
                         exclude(title=title_url).
                         exclude(story=0).order_by('-date_published'))
    pageFrom, pageTo, page, pageBack = _getFromTo(page=int(page), recentStories=recentStories)
    context = RequestContext(request, {
      'recentStories': recentStories[pageFrom:pageTo],
      'page': page,
      'pageBack': pageBack,
      'title_url': title_url
    })
    return HttpResponse(template.render(context))

