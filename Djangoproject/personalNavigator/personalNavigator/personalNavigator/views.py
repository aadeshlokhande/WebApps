# i created this file
from django.http import HttpResponse

def index(request):
    return HttpResponse('''<h1>Aadesh Personal Navigator</h1><hr><a href = "https://www.facebook.com/aadesh00786"> facebook </a><hr>
    <a href = "https://www.instagram.com/aadesh_lokhande"> instagram </a><hr>
    <a href = "https://www.github.com/aadeshlokhande"> github </a><hr>
    <a href = "https://www.linkedin.com/in/aadesh-lokhande-534126154/"> linkedin </a><hr>''')