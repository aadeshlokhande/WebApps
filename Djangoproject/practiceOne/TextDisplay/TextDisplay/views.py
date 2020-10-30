from django.http import HttpResponse

def index(request):
    f = open("1.txt", "r")
    read = f.read()
    f.close()
    # print(read)
    return HttpResponse(read)

if __name__ == '__main__':
    index()