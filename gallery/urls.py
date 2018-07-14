from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^search/', views.search_results, name='search_results'),
