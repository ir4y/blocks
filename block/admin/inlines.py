from django.contrib import admin
from adminsortable2.admin import SortableInlineAdminMixin
from ..models import *
from .mixins import AdminWysiwygMixin


class BlockFileInline(SortableInlineAdminMixin,
                      admin.TabularInline):
    model = BlockFile


class BlockImageInline(SortableInlineAdminMixin,
                       admin.TabularInline):
    model = BlockImage


class SubBlockAdmin(SortableInlineAdminMixin,
                    admin.StackedInline):
    model = SubBlock
    extra = 0

class SubBlockWysiwygAdmin(SortableInlineAdminMixin,
                    AdminWysiwygMixin,
                    admin.StackedInline):
    model = SubBlock
    extra = 0
