

from django.contrib.auth import login
from django.shortcuts import render, redirect

from .forms import SignUpForm, EditForm, FeedBackForm
from .models import User, FeedBack


def frontpage(request):
    """Главная"""
    return render(request, 'appchat/frontpage.html', {'title':'Home'})


def about(request):
    """Обратная связь"""
    if request.method == 'POST':
        form = FeedBackForm(request.POST)


        try:
            if form.is_valid():
                print(form.is_valid())

                FeedBack.objects.create(**form.cleaned_data)

                return redirect('/')
            else:
                return redirect('about')
        except:
            form.add_error(None, 'An error has occurred, please try again!')

    else:
        form = FeedBackForm()

    return render(request, 'appchat/about.html', {'form': form, 'title':'About'})

def signup(request):
    """Регистрация"""
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')

            return redirect('frontpage')
    else:
        form = SignUpForm()

    return render(request, 'appchat/signup.html', {'form': form, 'title':'SignUp'})
#

#
def me(request):
    """Аккаунт"""
    if request.method == 'GET':
        if User.objects.get(id=request.user.id):
            return render(request, 'appchat/me.html', {'title':'Account'})


def edit(request):
    """Редактировать профиль"""
    if request.method == 'GET':
        if User.objects.get(id=request.user.id):
            return render(request, 'appchat/edit.html')
    if request.method == 'POST':
        if User.objects.get(id=request.user.id):
            form = EditForm(request.POST, request.FILES, instance=request.user)

            if form.is_valid():

                form.save()
                return render(request, 'appchat/me.html')
            else:
                form = EditForm()

            return render(request, 'appchat/edit.html', {'form': form, 'title':'Edit'})


def error_404(request, exception):
    return render(request, 'appchat/404.html')


def error_403(request, exception):
    return render(request, 'appchat/403.html')
