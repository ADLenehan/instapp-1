from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'instapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'pages.views.index', name='homepage'),
    url(r'^admin/', include(admin.site.urls)),
)
