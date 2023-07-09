"""
(c) All rights reserved. ECOLE POLYTECHNIQUE FEDERALE DE LAUSANNE, Switzerland, VPSI, 2023
"""

from django.contrib import admin
from django.urls import include, path
from django_tequila.urls import urlpatterns as django_tequila_urlpatterns
from django_tequila.admin import TequilaAdminSite

admin.autodiscover()
admin.site.__class__ = TequilaAdminSite


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homepage.urls')),
    path('election/', include('election.urls'))
]

urlpatterns += django_tequila_urlpatterns
