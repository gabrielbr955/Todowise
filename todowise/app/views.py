from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout

from .models import User, List, Item


# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return render(request, 'app.html')
    else:
        return redirect('app_login')


def app_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('app_index')
    return render(request, 'login.html')


def app_logout(request):
    logout(request)
    return redirect('app_login')


def todo_list(request, list_id):
    #list = List.objects.get(pk=list_id)
    list = get_object_or_404(List, pk=list_id, user=request.user)
    print(list.items.all())
    return render(request, 'list.html', context={'list': list})

def add_item(request, list_id):
    item_title = request.POST.get('item_title')
    list = get_object_or_404(List, pk=list_id, user=request.user)
    item = Item(title=item_title, list=list)
    item.save()
    return redirect('todo_list', list_id=list_id)

def remove_item(request, list_id, item_id):
    list = get_object_or_404(List, pk=list_id, user=request.user)
    item = get_object_or_404(Item, pk=item_id, list=list)
    print(item.title)
    item.delete()
    return redirect('todo_list', list_id=list_id)