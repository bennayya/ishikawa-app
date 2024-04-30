from django.contrib import admin
from .models import IshikawaDiagram, Category, Cause

class CauseInline(admin.TabularInline):
    model = Cause
    extra = 1

class CategoryInline(admin.TabularInline):
    model = Category
    extra = 1
    inlines = [CauseInline]

@admin.register(IshikawaDiagram)
class IshikawaDiagramAdmin(admin.ModelAdmin):
    inlines = [CategoryInline]

admin.site.register(Category)
admin.site.register(Cause)
