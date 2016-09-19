import yaml
import os
dir_path = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(dir_path, 'group_schema.yml')) as f:
    GROUP_SCHEMA = yaml.load(f.read())
# GROUP_SCHEMA = {
    # 'News': {
        # 'verbose_name_plural': 'Newses',
        # 'group': 'news',
        # 'ordering': False,
        # 'can_add': True,
        # 'wysiwyg': True,
        # 'has_images': False,
        # 'has_files': False,
        # 'has_subblock': True,
    # },
    # 'Note': {
        # 'group': 'notes',
        # 'ordering': True,
        # 'can_add': True,
        # 'wysiwyg': False,
        # 'has_images': False,
        # 'has_files': False,
        # 'has_subblock': True,
    # },
    # 'Gallery': {
        # 'verbose_name_plural': 'Galleries',
        # 'group': 'gallery',
        # 'ordering': False,
        # 'can_add': False,
        # 'wysiwyg': False,
        # 'has_images': True,
        # 'has_files': False,
        # 'has_subblock': False,
    # },
    # 'Document': {
        # 'group': 'documents',
        # 'ordering': True,
        # 'can_add': True,
        # 'wysiwyg': False,
        # 'has_images': False,
        # 'has_files': True,
        # 'has_subblock': False,
    # }
# }
