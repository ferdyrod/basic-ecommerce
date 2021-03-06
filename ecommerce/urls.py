from django.conf.urls import patterns, include, url
from django.conf import settings


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', 'products.views.home', name='home'),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.STATIC_ROOT}),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^products/', include('products.urls')),
    (r'^accounts/', include('registration.backends.default.urls')),
    url(r'^cart/', include('cart.urls')),
    url(r'^orders/', include('orders.urls')),
    url(r'^contact/', 'contact.views.contact_us', name='contact_us'),
    url(r'^checkout/', 'cart.views.checkout', name='checkout'),
    url(r'^search/', 'products.views.search', name='search'),
)
