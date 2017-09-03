from django.shortcuts import render

def index(request):
    return render(request, 'event_manager/index.html')
