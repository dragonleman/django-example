"""
(c) All rights reserved. ECOLE POLYTECHNIQUE FEDERALE DE LAUSANNE, Switzerland, VPSI, 2023
"""

from django.db import models


class Vote(models.Model):
  """ Vote model """
  voter = models.CharField(max_length=1000, unique=True)
  choices = models.CharField(max_length=1000, null=True, blank=True)


class Election(models.Model):
  """ Election model """
  title = models.CharField(max_length=1000)
  maxchoices = models.IntegerField(default=1)

  startdate = "2023-06-19"
  enddate = "2023-08-31"
  
  contact = {
    "name": "",
    "phone": "",
    "email": "",
  }

  voters = []
  voters_file = open('/home/duratti/workspace-fsd/django-example/src/election/voters.txt', 'r')
  voters_file_lines = voters_file.readlines()
  for line in voters_file_lines:
    voters.append(line.strip())

  candidates = []
  candidates_file = open('/home/duratti/workspace-fsd/django-example/src/election/candidates.txt', 'r')
  candidates_file_lines = candidates_file.readlines()
  for line in candidates_file_lines:
    data = line.split(", ")
    candidate = {
      "name": data[0],
      "username": data[1],
      "link": data[2],
    }
    candidates.append(candidate)

  def get_candidates(self):
    result = []
    for candidate in self.candidates:
      result.append(candidate['username'])
    return result

