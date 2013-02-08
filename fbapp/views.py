# Create your views here.

from django.http import HttpResponse
from fandjango.decorators import facebook_authorization_required

def _post_message_on_wall(user, msg):
    fbpath = "{0}/feed".format(user.facebook_id)
    user.graph.post(path=fbpath, message=msg)

@facebook_authorization_required(permissions=["publish_actions"])
def canvas(request):
    user = request.facebook.user
    _post_message_on_wall(user, "{0} se acaba de registrar en TestApp".format(user.first_name))
    return HttpResponse("Bienvenido usuario: id {0} -- {1}!".format(user.facebook_id, user.full_name))
    
def post(request):
    from fandjango.models import User
    users = User.objects.all()
    for user in users:
        if user.authorized:
            user.oauth_token.extend()
            _post_message_on_wall(user, "TestApp ha publicado algo en su muro...")
    return HttpResponse("Se ha publicado en el muro de los usuarios registrados.")

