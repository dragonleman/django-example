# -*- coding:utf-8 -*-

"""(c) All rights reserved. ECOLE POLYTECHNIQUE FEDERALE DE LAUSANNE, Switzerland, VPSI, 2023"""

from django.urls import path

from homepage.views import homepage

urlpatterns = [
    path('', homepage, name='homepage'),
]
