from django.conf.urls import patterns, url


urlpatterns = patterns(
    'orders.views',
    url(r'^$', 'view', name='orders'),
)
