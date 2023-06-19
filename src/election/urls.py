# -*- coding:utf-8 -*-

"""(c) All rights reserved. ECOLE POLYTECHNIQUE FEDERALE DE LAUSANNE, Switzerland, VPSI, 2023"""

from django.urls import path

from election.views import create_election, result_election

urlpatterns = [
    path('create_election', create_election, name='create_election'),
    path('result_election', result_election, name='result_election'),
]
