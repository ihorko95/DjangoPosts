from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from time import time


def gen_slug(s):
    new_slug = slugify(s, allow_unicode=True)
    return new_slug + '-' + str(int(time()))


class Post(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True)
    body = models.TextField(blank=True, db_index=True)
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts')
    date_pub = models.DateField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={'slug': self.slug})

    def update_url(self):
        return reverse('post_update_url', kwargs={'slug': self.slug})

    def delete_url(self):
        # return reverse('post_list_url')
        return reverse('post_delete_url', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['-date_pub']

    def __str__(self):
        return '{}'.format(self.title)


class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def get_absolute_url(self):
        return reverse('tag_detail_url', kwargs={'slug': self.slug})

    def update_url(self):
        return reverse('tag_update_url', kwargs={'slug': self.slug})

    def delete_url(self):
        # return reverse('tags_list_url')
        return reverse('tag_delete_url', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['title']

    def __str__(self):
        return '{}'.format(self.title)
# Create your models here.
