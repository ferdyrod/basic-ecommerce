from django.conf.urls import patterns, url


urlpatterns = patterns(
    'cart.views',
    url(r'^$', 'view', name='cart'),
    url(r'^add$', 'add_to_cart'),

)
