from django.db import models


class Block(models.Model):
    page = models.CharField(max_length=255, db_index=True)
    slug = models.CharField(max_length=255, db_index=True)
    header = models.CharField(blank=True, max_length=255)
    content = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    def __str__(self):
        return "{}.{}".format(self.page, self.slug)

    class Meta(object):
        ordering = ('order',)
        unique_together = (
            ('page', 'slug')
        )


class BlockFile(models.Model):
    block = models.ForeignKey('block.Block')
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='block/files/%Y/%m/%d/')
    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta(object):
        ordering = ('order',)


class BlockImage(models.Model):
    block = models.ForeignKey('block.Block')
    title = models.CharField(max_length=255)
    file = models.ImageField(upload_to='block/images/%Y/%m/%d/')
    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta(object):
        ordering = ('order',)


class SubBlock(models.Model):
    block = models.ForeignKey('block.Block')
    header = models.CharField(blank=True, max_length=255)
    content = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta(object):
        ordering = ('order',)
