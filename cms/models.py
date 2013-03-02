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
