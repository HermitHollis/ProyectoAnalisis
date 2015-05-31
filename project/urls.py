from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls import patterns
admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^$', 'project.views.home'),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^alumno/', alumno
    #url(r'^admin/', admin.site.root),
    #url(r'^hello/$', 'article.views.hello'),
    #url(r'^hello_template/$', 'article.views.hello_template'),
    #url(r'^hello_class_view/$', HelloTemplate.as_view()),
    #url(r'^articles/', include('article.urls')),
]
