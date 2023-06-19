from django.http import HttpResponse
from django.template import loader
from election.models import Election, Vote


def create_election(request):

  if request.GET and 'title' in request.GET:
    election, created = Election.objects.get_or_create(title=request.GET['title'])
    if created:
      election.maxchoices = int(request.GET['maxchoices'])
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
