from django.contrib import admin
from .models import Category, Project, ProjectImage

# Register your models here.


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'category',
        'featured',
        'created_at',
    )

    list_filter = ('category', 'featured')

    search_fields = ('title', 'description')

    inlines = [ProjectImageInline]

