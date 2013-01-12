# Create your views here.

from django.http import HttpResponse
from fandjango.decorators import facebook_authorization_required

@facebook_authorization_required(permissions=["publish_actions"])
def canvas(request):
    fb = request.facebook
    user = fb.user
    return HttpResponse("Hello user: id {0} -- {1} {2}".format(user.facebook_id, user.first_name, user.last_name))
