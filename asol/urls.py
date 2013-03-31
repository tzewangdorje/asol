from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'cms.views.home', name='home'),
    url(r'^gallery$', 'cms.views.gallery', name='gallery'),
    url(r'^ajaxLoadStories/(?P<title_url>[A-Za-z0-9\-]+)/(?P<page>[0-9]+)$', 'cms.views.ajaxLoadStories', name='ajaxLoadStories'),
    url(r'^content/', include('cms.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'^tinymce/', include('tinymce.urls'))
)
