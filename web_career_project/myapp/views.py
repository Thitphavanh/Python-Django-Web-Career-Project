from django.shortcuts import *
from .models import *
from django.core.files.storage import FileSystemStorage


def home(request):
    # variable = Table.objects.method()
    # Query all posts
    all_posts = Post.objects.all()
    context = {"all_posts": all_posts}
    return render(request, "webcareer/home.html", context)


def login(request):
    all_login = Portal.objects.all()
    context = {"all_login": all_login}
    return render(request, "webcareer/login.html", context)


def portal(request):
    all_portals = Portal.objects.all()
    context = {"all_portals": all_portals}
    return render(request, "webcareer/portal.html", context)


def add_article(request):
    if request.method == 'POST' and request.FILES['uploadfile']:
        data = request.POST.copy()
        title = data.get("title")
        detail = data.get("detail")

        new_artical = Portal()
        new_artical.title = title
        new_artical.detail = detail

        upload_file = request.FILES['uploadfile']
        upload_file_name = request.FILES['uploadfile'].name.replace(' ', '')
        print('FILE_IMAGE: ', upload_file)
        print('IMAGE_NAME: ', upload_file_name)
        fs = FileSystemStorage()
        filename = fs.save("pdf/" + upload_file_name, upload_file)
        upload_file_url = fs.url(filename)
        new_artical.file = upload_file_url[6:]

        new_artical.save()

    return render(request, "webcareer/add-article.html")


def edit_article(request, id):
    portal = Portal.objects.get(id=id)

    if request.method == "POST" and request.FILES['uploadfile']:
        data = request.POST.copy()
        title = data.get("title")
        detail = data.get("detail")

        portal.title = title
        portal.detail = detail

        upload_file = request.FILES['uploadfile']
        upload_file_name = request.FILES['uploadfile'].name.replace(' ', '')
        print('FILE_IMAGE: ', upload_file)
        print('IMAGE_NAME: ', upload_file_name)
        fs = FileSystemStorage()
        filename = fs.save("pdf/" + upload_file_name, upload_file)
        upload_file_url = fs.url(filename)
        portal.file = upload_file_url[6:]

        portal.save()

    elif request.method == "POST":
        if request.POST.get("form_type") == 'formOne':
            data = request.POST.copy()
            title = data.get("title")
            detail = data.get("detail")

            portal.title = title
            portal.detail = detail

            portal.save()
   
        elif request.POST.get("form_type") == 'formTwo':
            portal.delete()
            

    portal = Portal.objects.get(id=id)
    context = {"portal": portal}
    return render(request, "webcareer/edit-article.html", context)


def about(request):
    all_abouts = Portal.objects.all()
    context = {"all_abouts": all_abouts}
    return render(request, "webcareer/about.html", context)
