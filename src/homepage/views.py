from django.http import HttpResponse
from django.template import loader
from election.models import Vote


def homepage(request):

  if request.GET:
    vote, created = Vote.objects.get_or_create(voter=request.user.profile.enckey)
    choices = ""
    for choice in request.GET:
      choices += str(choice) + ","
    vote.choices = choices[:-1]
    vote.save()
    template = loader.get_template('thanks.html')
    context = {"user": request.user, "username": vote.voter, "choices": vote.choices}
    return HttpResponse(template.render(context))

  if request.user:
    context = {"user": request.user }
  else:
    context = {}
  template = loader.get_template('homepage.html')
  return HttpResponse(template.render(context))

