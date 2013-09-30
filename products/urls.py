from django.conf.urls import patterns, url


urlpatterns = patterns(
    'products.views',
    url(r'^$', 'all_products', name='products'),
    url(r'^(?P<slug>.*)/$', 'single_product'),
)
