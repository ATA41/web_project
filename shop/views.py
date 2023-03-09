from django.shortcuts import render, get_object_or_404, redirect

from django.http import HttpResponse

from .models import Item, Purchase


def list_item(request):
    items = Item.objects.all()
    return render(request, "list_item.html", {"items": items})


def detail_item(request, id):
    items_detail = Item.objects.get(id=id)
    items_purchases = items_detail.purchases.all()
    data = {
        "items_detail": items_detail,
        "items_purchases": items_purchases,
    }
    return render(request, "detail_item.html", data)