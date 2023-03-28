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
    return render(request, "webcareer/portal.html", context)
