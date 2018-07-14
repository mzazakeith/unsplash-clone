from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^image/(?P<image_id>\d+)', views.image, name="one"),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^location/(?P<location_id>\d+)',views.imageLocation, name='location')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
