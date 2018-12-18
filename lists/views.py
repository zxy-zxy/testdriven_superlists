from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError

from lists.models import Item, List


def home_page(request):
    return render(request, 'lists/home.html')


def new_list(request):
    if request.method == 'POST':
        list_ = List.objects.create()
        new_item_text = request.POST.get('item_text')
        try:
            item = Item(text=new_item_text, list=list_)
            item.full_clean()
            item.save()
        except (ValidationError, IntegrityError) as e:
            list_.delete()
            error = 'You can\'t have an empty list item'
            return render(request, 'lists/home.html', {'error': error})
        # return redirect(f'/lists/{list_.id}/')
        return redirect(list_)


def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    error = None
    if request.method == 'POST':
        try:
            new_item_text = request.POST.get('item_text')
            item = Item(text=new_item_text, list=list_)
            item.full_clean()
            item.save()
            return redirect(list_)
        except ValidationError as e:
            error = 'You can\'t have an empty list item'
    return render(request, 'lists/list.html', {'list': list_, 'error': error})
