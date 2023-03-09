from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("item/", views.list_item, name="list_item"),
    path("item/<int:id>/", views.detail_item, name="detail_item"),
]