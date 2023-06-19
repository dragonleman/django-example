from django.http import HttpResponse
from django.template import loader
from config.settings.base import BASE_DIR
from election.models import Election, Vote


def create_election(request):

  if request.GET and 'title' in request.GET:
    election, created = Election.objects.get_or_create(title=request.GET['title'])

    election.maxchoices = int(request.GET['maxchoices'])

    voters = []
    voters_file = open(str(BASE_DIR.parent) + "/election/" + request.GET['voters'], 'r')
    voters_file_lines = voters_file.readlines()
    for line in voters_file_lines:
      voters.append(line.strip())
    election.voters = voters

    candidates = []
    candidates_file = open(str(BASE_DIR.parent) + "/election/" + request.GET['candidates'], 'r')
    candidates_file_lines = candidates_file.readlines()
    for line in candidates_file_lines:
      data = line.split(", ")
      candidate = {
        "name": data[0],
        "username": data[1],
        "link": data[2],
      }
      candidates.append(candidate)
    election.candidates = candidates

    election.save()

  context = { "elections": Election.objects.all() }
  if request.user:
    context["user"] = request.user

  template = loader.get_template('elections.html')
  return HttpResponse(template.render(context))


def result_election(request):

  voters = Vote.objects.all()
  
  blancs = 0
  candidates = {}
  for voter in voters:
    choices = voter.choices.split(",")
    if choices == [""]:
      blancs += 1
    for choice in choices:
      if choice == "":
        choice = "**blank**"
      candidates[choice] = candidates.get(choice, 0) + 1

  context = { 
    "votes": voters,
    "blancs": blancs,
    "candidates": dict(sorted(candidates.items(), key=lambda item: item[1], reverse=True)),
    "election": Election.objects.all().first()
  }

  template = loader.get_template('results.html')
  return HttpResponse(template.render(context))
