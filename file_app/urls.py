# from django.conf.urls import url
from django.urls import path
from django.urls import re_path as url
from .views import FileView

urlpatterns = [
    # path(r'^upload/$', FileView.as_view(), name='file-upload'),
    url(r'^upload/$', FileView.as_view(), name='file-upload'),

]