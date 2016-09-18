from django.contrib import admin

from .mixins import *
from .inlines import *
from ..models import group_models
from ..settings import group_schema


def build_admin_class(name, group_info):
    bases = []
    inlines = []

    if group_info['ordering']:
        bases.append(SortableAdminMixin)
    else:
        bases.append(DisableSortableAdminMixin)

    if group_info['can_add']:
        bases.append(admin_add_mixin_factory(name, group_info))
    else:
        bases.append(AdminDinyAddMixin)

    if group_info['wysiwyg']:
        bases.append(AdminWysiwygMixin)

    if group_info['has_images']:
        inlines.append(BlockImageInline)

    if group_info['has_files']:
        inlines.append(BlockFileInline)

    if group_info['has_subblock']:
        inlines.append(SubBlockWysiwygAdmin
                       if group_info['wysiwyg'] else SubBlockAdmin)

    bases.append(ModelAdmin)

    return type('{}ModelAdmin'.format(name),
                tuple(bases),
                {'inlines': inlines})


for name, group_info in group_schema.items():
    admin.site.register(group_models[name],
                        build_admin_class(name, group_info))
