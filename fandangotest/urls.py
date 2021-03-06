from django.conf.urls import patterns, include, url
import fbapp.views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fandangotest.views.home', name='home'),
    # url(r'^fandangotest/', include('fandangotest.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    (r'^fandjango/', include('fandjango.urls')),
    (r'^canvas/', fbapp.views.canvas),
    (r'^post/', fbapp.views.post),
)
