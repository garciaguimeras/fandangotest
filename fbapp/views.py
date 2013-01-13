# Create your views here.

from django.http import HttpResponse
from fandjango.decorators import facebook_authorization_required
#from facepy import GraphAPI

def _post_message_on_wall(user, msg):
    fbpath = "{0}/feed".format(user.facebook_id)
    user.graph.post(path=fbpath, message=msg)

@facebook_authorization_required(permissions=["publish_actions"])
def canvas(request):

    fb = request.facebook
    user = fb.user
    #access_token = user.oauth_token.token
    #graph = GraphAPI(access_token)
    
    _post_message_on_wall(user, "{0} se acaba de registrar en TestApp".format(user.first_name))
    
    return HttpResponse("Bienvenido usuario: id {0} -- {1}!".format(user.facebook_id, user.full_name))
    
def post(request):
    
    from fandjango.models import User
    users = User.objects.get()
    for user in users:
        if user.oauth_token.expired():
            user.oauth_token.extend()
        _post_message_on_wall(user, "TestApp ha publicado algo en su muro...")
        
    return HttpResponse("Se ha publicado en el muro de {0} usuarios registrados.".format(len(users)))

