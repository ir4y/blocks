from django.db import models
from .models import *
from ..settings import group_schema


def create_flatblock_for_group_model(name, group_info):
    class GroupBlockManager(models.Manager):

        def get_queryset(self):
            return super(GroupBlockManager, self)\
                .get_queryset()\
                .filter(group=group_info['group'])

    class GroupBlockMeta:
        proxy = True
        verbose_name = name
        verbose_name_plural = group_info.get('verbose_name_plural')

    class_name = '{}Block'.format(name)
    return type(class_name,
                (Block, ),
                {
                    'objects': GroupBlockManager(),
                    '__module__': __name__,
                    'Meta': GroupBlockMeta
                })

group_models = {name: create_flatblock_for_group_model(
    name, group) for name, group in group_schema.items()}
