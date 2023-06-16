"""
(c) All rights reserved. ECOLE POLYTECHNIQUE FEDERALE DE LAUSANNE, Switzerland, VPSI, 2023
"""

from django.db import models


class Vote(models.Model):
  """ Vote model """
  voter = models.CharField(max_length=1000, unique=True)
  choices = models.CharField(max_length=1000, null=True, blank=True)

