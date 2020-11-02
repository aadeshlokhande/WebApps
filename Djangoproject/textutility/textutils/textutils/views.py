# This file created by me
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def about(request):
    return HttpResponse("<a href = '/' > Back </a> About")

def analyze(request):
    djtext = request.GET.get('text', 'default')
    removepunc = request.GET.get('removepunc','off')
    if removepunc == 'on':
        punctuations = '''`~!@#$%^&*()_+-=[{]}\|;':",./<>?'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed+char
        params = {'purpose':'Remove Punctuations', 'analysed_text':analyzed}
        return render(request, 'analyze.html', params)
    # return HttpResponse("<a href = '/' > Back </a> removepunc")

def capfirst(request):
    return HttpResponse("<a href = '/' > Back </a> capfirst")

def newlineremove(request):
    return HttpResponse("<a href = '/' > Back </a> newlineremove")

def spaceremove(request):
    return HttpResponse("<a href = '/' > Back </a> spaceremove")

def charcount(request):
    return HttpResponse("<a href = '/' > Back </a> charcount")