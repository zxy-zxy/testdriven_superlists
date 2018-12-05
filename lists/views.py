from django.shortcuts import render, redirect
from django.http import HttpResponse

from lists.models import Item, List


def home_page(request):
    return render(request, 'lists/home.html')


def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    return render(request, 'lists/list.html', {'list': list_})


def new_list(request):
    if request.method == 'POST':
        list_ = List.objects.create()
        new_item_text = request.POST.get('item_text')
        Item.objects.create(text=new_item_text, list=list_)
        return redirect(f'/lists/{list_.id}/')


def add_item(request, list_id):
    if request.method == 'POST':
        list_ = List.objects.get(id=list_id)
        item_text = request.POST.get('item_text')
        Item.objects.create(text=item_text, list=list_)
        return redirect(f'/lists/{list_.id}/')
