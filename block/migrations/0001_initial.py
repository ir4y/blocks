from django.db import migrations, models
import django.db.models.deletion


def create_some_galleries(apps, schema_editor):
    Block = apps.get_model('block', 'Block')
    Block.objects.create(group='gallery',
                         slug='header',
                         order=1)
    Block.objects.create(group='gallery',
                         slug='about',
                         order=2)
    Block.objects.create(group='gallery',
                         slug='footer',
                         order=3)


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.CharField(db_index=True, max_length=255)),
                ('slug', models.CharField(db_index=True, max_length=255)),
                ('header', models.CharField(blank=True, max_length=255)),
                ('content', models.TextField(blank=True)),
                ('order', models.PositiveIntegerField(default=0)),
            ],
            options={
                'ordering': ('order',),
            },
        ),
        migrations.CreateModel(
            name='BlockFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('file', models.FileField(upload_to='block/files/%Y/%m/%d/')),
                ('order', models.PositiveIntegerField(default=0)),
                ('block', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='block.Block')),
            ],
            options={
                'ordering': ('order',),
            },
        ),
        migrations.CreateModel(
            name='BlockImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('file', models.ImageField(upload_to='block/images/%Y/%m/%d/')),
                ('order', models.PositiveIntegerField(default=0)),
                ('block', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='block.Block')),
            ],
            options={
                'ordering': ('order',),
            },
        ),
        migrations.CreateModel(
            name='SubBlock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(blank=True, max_length=255)),
                ('content', models.TextField(blank=True)),
                ('order', models.PositiveIntegerField(default=0)),
                ('block', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='block.Block')),
            ],
            options={
                'ordering': ('order',),
            },
        ),
        migrations.AlterUniqueTogether(
            name='block',
            unique_together=set([('group', 'slug')]),
        ),
        migrations.RunPython(create_some_galleries),
    ]
