from django.shortcuts import *
from .models import *


def home(request):
    # variable = Table.objects.method()
    # Query all posts
    all_posts = Post.objects.all()
    context = {"all_posts": all_posts}
    return render(request, "webcareer/home.html", context)


def about(request):
    all_portals = Portal.objects.all()
    context = {"all_portals": all_portals}
    return render(request, "webcareer/about.html", context)


def portal(request):
    all_portals = Portal.objects.all()
    context = {"all_portals": all_portals}
    return render(request, "webcareer/edit-information.html", context)

def information(request):
    all_informations = Portal.objects.all()
    context = {"all_informations": all_informations}
    return render(request, "webcareer/information.html", context)


def information(request):
    all_edit_informations = Portal.objects.all()
    context = {"all_edit_informations": all_edit_informations}
    return render(request, "webcareer/edit-information.html", context)
