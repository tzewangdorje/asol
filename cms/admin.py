from django.contrib import admin
from django.forms import *
from django.db.models import *
from tinymce.widgets import TinyMCE
from cms.models import Partner, Media, Article, ArticleText, ArticlePhoto, ArticleYoutube, ArticleLink

class ArticleTextAdmin(admin.ModelAdmin):
    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super(ArticleTextAdmin, self).formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'body':
            formfield.widget = forms.Textarea(attrs=formfield.widget.attrs)
        return formfield
    
class ArticleTextForm(forms.ModelForm):
    body = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 20}))

    class Meta:
        model = ArticleText

class ArticleTextAdmin(admin.ModelAdmin):
    form = ArticleTextForm
    
admin.site.register(Partner)
admin.site.register(Media)
admin.site.register(Article)
admin.site.register(ArticleText, ArticleTextAdmin)
admin.site.register(ArticleLink)
admin.site.register(ArticleYoutube)
admin.site.register(ArticlePhoto)

