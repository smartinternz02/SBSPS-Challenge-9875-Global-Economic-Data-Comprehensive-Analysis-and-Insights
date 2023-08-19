from django.shortcuts import render

def BASE(request):
    return render(request, 'base.html')

def REPORT(request):
    return render(request, 'report.html')

def STORY(request):
    return render(request, 'story.html')

def VISION(request):
    return render(request, 'vision.html')

def TEAM(request):
    return render(request, 'team.html')