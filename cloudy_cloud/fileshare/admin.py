from django.contrib import admin
from .models import SharedFile
from django.contrib.auth.models import Group


admin.site.unregister(Group)


@admin.register(SharedFile)
class FileAdmin(admin.ModelAdmin):
    list_display = ("show_file_name", "date_created", "file_key", "show_file_size")
    list_filter = ("date_created",)
    search_fields = ("file_key__startswith",)
    fields = ("file", "file_key")

    def show_file_size(self, obj):
        return obj.file.size
    show_file_size.short_description="Size in bytes"

    def show_file_name(self, obj):
    	return str(obj.file.file).split('/')[-1]
    show_file_name.short_description="Name"