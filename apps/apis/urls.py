from django.conf.urls import url, include
from django.conf.urls.static import static
from rest_framework.urlpatterns import format_suffix_patterns

from POKEDX import settings
from . import views

urlpatterns = [
    url(r'^regions/$', views.RegionView.as_view(), name='region-list'),
    # url(r'^regions/(?P<pk>[0-9]+)/$', views.RegionView.as_view(), name='region-create'),
    url(r'^cities/$', views.CityView.as_view(), name='cities-list'),
    url(r'^town/$', views.TownView.as_view(), name='town-list'),
    url(r'^medal/$', views.MedalView.as_view(), name='medal-list'),
    # url(r'^cities/(?P<pk>[0-9]+)/$', views.CityView.as_view(), name='cities-create'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
