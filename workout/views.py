# vim: sw=4 ai sm expandtab
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the workout index.")
