# Create your views here.

from django.http import HttpResponse
from fandjango.decorators import facebook_authorization_required
from facepy import GraphAPI

@facebook_authorization_required(permissions=["publish_actions"])
def canvas(request):

    fb = request.facebook
    user = fb.user
    access_token = user.oauth_token.token

    graph = GraphAPI(access_token)
    fbpath = "{0}/feed".format(user.facebook_id)
    fbmsg = "TestApp acaba de hacer una publicacion en tu muro"
    graph.post(path=fbpath, message=fbmsg)
    
    return HttpResponse("Hello user: id {0} -- {1} {2} -- access token: {3}".format(user.facebook_id, user.first_name, user.last_name, access_token))
