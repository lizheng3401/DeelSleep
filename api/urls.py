from django.conf.urls import url
from api import views
urlpatterns = [
    url(r'^sleepData/(?P<pk>[0-9]+)/$', view=views.SleepData.as_view(), name='sleepData'),
]