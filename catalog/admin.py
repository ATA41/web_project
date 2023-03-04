from django.contrib import admin

from .models import ModelCategory, ModelProduct


admin.site.register(ModelCategory)
admin.site.register(ModelProduct)
