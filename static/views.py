from django.shortcuts import render
from .seo import *
# Create your views here.

def index(request):
    return render(request, "index.html", {
        "data" : index_page,
    })

def early_investors(request):
    return render(request, "early-investors.html", {
        "data" : early_investors_page,
    })

def security(request):
    return render(request, "security.html", {
        "data" : security_page,
    })

def team(request):
    return render(request, "team.html", {
        "data" : team_page,
    })

def contact(request):
    return render(request, 'contact.html', {
        "data" : contact_page,
    })