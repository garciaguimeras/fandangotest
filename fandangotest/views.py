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
    og_path = "{0}/feed".format(user.facebook_id)
    message = "TestApp acaba de hacer una publicacion en tu muro"
    graph.post(path=og_path, og_msg=message)
    
    return HttpResponse("Hello user: id {0} -- {1} {2}".format(user.facebook_id, user.first_name, user.last_name))
