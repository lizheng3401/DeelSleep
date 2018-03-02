from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from device import views

urlpatterns = [
    url(r'^$', views.api_root),
    url(r'^devices/$',  views.DeviceList.as_view(), name="devices-list"),
    url(r'^devices/(?P<pk>[0-9]+)/$', views.DeviceDetail.as_view(), name="devices-detail")
]

urlpatterns = format_suffix_patterns(urlpatterns)

