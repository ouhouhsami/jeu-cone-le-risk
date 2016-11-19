# -*- coding: utf-8 -*-
"""ecoquartier URL Configuration
"""
from django.conf.urls import url, include
from django.contrib import admin

from surveys.views import home

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name='home'),
]

admin.site.site_header = u"Jeu Coné les Risks"
