from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^index/$',views.index,name='index'),
    url(r'^list(?P<tid>\d+)-(?P<pIndex>\d+)/$',views.list,name='list'),
    url(r'^(?P<tid>\d+)-(?P<gid>\d+)/$',views.detail,name='detail'),
]