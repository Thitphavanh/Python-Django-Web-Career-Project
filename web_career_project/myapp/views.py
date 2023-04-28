from django.shortcuts import *
from .models import *
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


def home(request):
    # variable = Table.objects.method()
    # Query all posts
    all_posts = Post.objects.all()
    context = {"all_posts": all_posts}
    return render(request, "webcareer/home.html", context)


# def login_user(request):
#     all_login_user = Portal.objects.all()
#     context = {"all_login_user": all_login_user}
#     return render(request, "webcareer/login.html", context)


def register(request):
    if request.method == 'POST':
        data = request.POST.copy()
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        email = data.get('email')
        password = data.get('password')

        new_user = User()
        new_user.username = email
        new_user.email = email
        new_user.first_name = first_name
        new_user.last_name = last_name
        new_user.set_password(password)
        new_user.save()

        profile = Profile()
        profile.user = User.objects.get(username=email)
        profile.save()

        user = authenticate(username=email, password=password)
        login(request, user)
        
        # all_login = Portal.objects.all()
        # context = {"all_login": all_login}
    return render(request, "webcareer/register.html")


def portal(request):
    all_portals = Portal.objects.all()
    context = {"all_portals": all_portals}
    return render(request, "webcareer/portal.html", context)


def add_article(request):
    if request.method == 'POST':
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
        filename = fs.save(upload_file_name, upload_file)
        upload_file_url = fs.url(filename)
        new_artical.file = upload_file_url[6:]

        new_artical.save()

    return render(request, "webcareer/add-article.html")


def edit_article(request, id):
    portal = Portal.objects.get(id=id)

    if request.method == "POST":
        data = request.POST.copy()
        title = data.get("title")
        detail = data.get("detail")

        portal.title = title
        portal.detail = detail

        if 'uploadfile' in request.FILES:
            upload_file = request.FILES['uploadfile']
            upload_file_name = request.FILES['uploadfile'].name.replace(' ', '')
            print('FILE_IMAGE: ', upload_file)
            print('IMAGE_NAME: ', upload_file_name)
            fs = FileSystemStorage()
            filename = fs.save(upload_file_name, upload_file)
            upload_file_url = fs.url(filename)
            portal.file = upload_file_url[6:]
        else:
            print('NO')
        portal.save()
        
        return redirect("portal")

    portal = Portal.objects.get(id=id)
    context = {"portal": portal}
    return render(request, "webcareer/edit-article.html", context)


def booking(request):
    all_abouts = Portal.objects.all()
    context = {"all_abouts": all_abouts}
    return render(request, "webcareer/booking.html", context)


def about(request):
    all_abouts = Portal.objects.all()
    context = {"all_abouts": all_abouts}
    return render(request, "webcareer/about.html", context)
