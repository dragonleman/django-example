from django.http import HttpResponse
from django.template import loader
from election.models import Vote, Election


def homepage(request):

  election = Election.objects.all().first()

  if request.GET:
    vote, created = Vote.objects.get_or_create(voter=request.user.profile.pk)
    choices = ""
    
    if not "blank_vote" in request.GET:
      for choice in request.GET:
        choices += str(choice) + ","
      choices = choices[:-1]

      validated = validate_vote(choices, election)
      
      if not validated:
        # cheating means a blank vote
        vote.choices = ""
        vote.save()
        template = loader.get_template('cheat.html')
        context = {
          "user": request.user,
        }
        return HttpResponse(template.render(context))

    vote.choices = choices
    vote.save()
    template = loader.get_template('thanks.html')
    context = {"user": request.user, "choices": vote.choices, "numberchoices": vote.choices.count(",") + 1}
    return HttpResponse(template.render(context))

  context = { "election": election }
  if request.user:
    context["user"] = request.user
  
  if request.user.is_authenticated:
    context["display_election"] = election and request.user.profile.sciper in election.voters
  else:
    context["display_election"] = False

  template = loader.get_template('homepage.html')
  return HttpResponse(template.render(context))


# in case of cheating on the html/script file
def validate_vote(choices, election):
  chosencandidates = choices.split(",")
  candidates = election.get_candidates_username()
    
  # check if there is a new cadidate
  check = all(item in candidates for item in chosencandidates)
  if not check:
    return False
  
  # check if number of choices is ok
  if len(chosencandidates) > len(candidates):
    return False
  
  return True
