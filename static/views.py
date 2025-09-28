# views.py
from django.shortcuts import render
from .seo import pages

def index(request):
    return render(request, "index.html", {"data": pages["index"]})

def early_investors(request):
    return render(request, "early_investors.html", {"data": pages["early_investors"]})

def security(request):
    return render(request, "security.html", {"data": pages["security"]})

def team(request):
    return render(request, "team.html", {"data": pages["team"]})

def contact(request):
    return render(request, "contact.html", {"data": pages["contact"]})
