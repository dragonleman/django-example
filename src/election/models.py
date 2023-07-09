"""
(c) All rights reserved. ECOLE POLYTECHNIQUE FEDERALE DE LAUSANNE, Switzerland, VPSI, 2023
"""

import ast
from datetime import date
from django.db import models


class Vote(models.Model):
    """ Vote model """
    voter = models.CharField(max_length=1000, unique=True)
    choices = models.CharField(max_length=1000, null=True, blank=True)


class Election(models.Model):
    """ Election model """
    title = models.CharField(max_length=200, default="")
    maxchoices = models.IntegerField(default=1)
    
    startdate = models.CharField(max_length=50, default=date.today())
    enddate = models.CharField(max_length=50, default=date.today())

    contact_name = models.CharField(max_length=100, default="")
    contact_phone = models.CharField(max_length=100, default="")
    contact_email = models.CharField(max_length=100, default="")

    voters = models.TextField(null=True, blank=True)
    candidates = models.TextField(null=True, blank=True)


    def get_voters(self):
        return ast.literal_eval(self.voters)


    def get_candidates(self):
        return ast.literal_eval(self.candidates)


    def get_candidates_username(self):
        candidates = self.get_candidates()
        result = []
        for candidate in candidates:
          result.append(candidate['username'])
        return result
