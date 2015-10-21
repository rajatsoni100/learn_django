from django.conf.urls import include, url, patterns
from login import views

urlpatterns = patterns(' ',
    url(r'^$',      views.index),
)


