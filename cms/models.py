from django.db import models

class Partner(models.Model):
    def __unicode__(self):
        return self.name
    name = models.CharField(max_length=64)
    info_url = models.CharField(max_length=128)
    logo_url = models.CharField(max_length=64)
    description = models.CharField(max_length=512)

class Media(models.Model):
    def __unicode__(self):
        return self.partner.name+"."+self.media_type
    partner = models.ForeignKey(Partner, related_name='medias')
    media_type = models.CharField(max_length=16)
    link = models.CharField(max_length=128)

class Article(models.Model):
    def __unicode__(self):
        return self.title
    title = models.CharField(max_length=64)
    title_url =  models.CharField(max_length=32)
    date_published = models.DateTimeField()
    article_type =  models.CharField(max_length=16)
    summary =  models.CharField(max_length=256)
    image_thumb_url =  models.CharField(max_length=128, null=True, blank=True)
    story = models.BooleanField()
    
    def makeUrl(self):
        if self.article_type=='link':
            return self.articlelink.link_url
        else:
            return "/content/"+self.title_url

class ArticleText(Article):
    body = models.CharField(max_length=3000)
    image_body_url = models.CharField(max_length=128, null=True, blank=True)
    image_alt_text = models.CharField(max_length=128, null=True, blank=True)

class ArticleYoutube(Article):
    video_url =  models.CharField(max_length=128, null=True, blank=True)
    caption = models.CharField(max_length=64, null=True, blank=True)

class ArticleLink(Article):
    link_url =  models.CharField(max_length=128)
    caption = models.CharField(max_length=64, null=True, blank=True)

class ArticlePhoto(Article):
    photo_url = models.CharField(max_length=128)
    caption = models.CharField(max_length=128, null=True, blank=True)

