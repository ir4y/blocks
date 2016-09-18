from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin
from ckeditor.widgets import CKEditorWidget
from django.contrib import admin
from django.db import models

from ..models import Block, BlockFile, BlockImage, SubBlock


class BlockFileInline(SortableInlineAdminMixin,
                      admin.TabularInline):
    model = BlockFile


class BlockImageInline(SortableInlineAdminMixin,
                       admin.TabularInline):
    model = BlockImage


class SubBlockAdmin(SortableInlineAdminMixin,
                    admin.StackedInline):
    model = SubBlock
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget},
    }
    extra = 0


class BlockAdmin(SortableAdminMixin, admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget},
    }
    inlines = (SubBlockAdmin, BlockImageInline, BlockFileInline, )


admin.site.register(Block, BlockAdmin)
