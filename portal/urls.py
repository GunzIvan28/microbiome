from django.conf.urls import url
from django.urls import path, include
from django.views.generic import TemplateView

from .models import Project
from . import views

urlpatterns = [
    #url(r'^$', TemplateView.as_view(template_name="index.html"), name='home'),
    #url(r'^$', views.view_maps, name='index'),
    #path('charts/', views.make_pie_and_barcharts, name='piechart'),
    path('dashboard/', views.dashboard_charts, name='dashboard'),
]


#from djgeojson.views import GeoJSONLayerView
#re_path(r'^(?P<year>[0-9]{4})/(?P<month>0?[1-9]|1[0-2])/',views.index, name='index'),
#url(r'^data/$', GeoJSONLayerView.as_view(model=Project)),geometry_field="log_lat", properties=("platform","country")), name='data'),
#url(r'^data/(?P<pk>[0-9]+)$',DetailView.as_view(model=Project), name='index'),
