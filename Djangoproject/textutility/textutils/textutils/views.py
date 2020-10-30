# This file created by me
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello aadesh")
def about(request):
    return HttpResponse("About aadesh")