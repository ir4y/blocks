from adminsortable2.admin import SortableAdminMixin
from ckeditor.widgets import CKEditorWidget
from django.contrib import admin
from django.db import models


class AdminWysiwygMixin:
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget},
    }


def admin_add_mixin_factory(name, group_info):
    class AdminAddMixin:
        def save_model(self, request, obj, form, change):
            obj.group = group_info['group']
            super(AdminAddMixin, self).save_model(request, obj, form, change)
    return AdminAddMixin


class AdminDinyAddMixin:
    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class DisableSortableAdminMixin:
    def get_form(self, request, obj=None, **kwargs):
        if self.exclude:
            if 'order' not in self.exclude:
                self.exclude.append('order')
        else:
            self.exclude = ['order']
        return super(DisableSortableAdminMixin, self).get_form(request, obj, **kwargs)


class ModelAdmin(admin.ModelAdmin):
    exclude = ['group']
