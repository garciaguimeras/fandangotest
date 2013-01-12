# Create your views here.

from django.http import HttpResponse
from fandjango.decorators import facebook_authorization_required

@facebook_authorization_required
def canvas(request):
    return HttpResponse('Hello user: , %s.' % request.facebook.user.first_name)
