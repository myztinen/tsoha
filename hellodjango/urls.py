from django.conf.urls.defaults import patterns, include, url
# development static files
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'Tsoha.views.index'),
    (r'^search/', 'Tsoha.views.index'),
    (r'^recipes/(?P<recipe_id>\d+)/$', 'Tsoha.views.open_recipepage'),
    (r'^add$', 'Tsoha.views.index'),
    (r'^add_recipes/$', 'Tsoha.views.open_addpage'),
    # Examples:
    # url(r'^$', 'hellodjango.views.home', name='home'),
    # url(r'^hellodjango/', include('hellodjango.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
# development static files
urlpatterns += staticfiles_urlpatterns()
