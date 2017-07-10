from django.conf.urls import url

from goods.search_view import MySearchView
from . import views
urlpatterns = [
    url(r'^index/$',views.index,name='index'),
    url(r'^list(?P<tid>\d+)-(?P<pIndex>\d+)/$',views.list,name='list'),
    url(r'^(?P<tid>\d+)-(?P<gid>\d+)/$',views.detail,name='detail'),
    url(r'^search',views.search,name='search'),
    url(r'^search',MySearchView.as_view,name='search'),
]