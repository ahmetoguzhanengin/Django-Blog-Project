from django.db import models
from django.urls import  reverse
from django.utils.text import slugify

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=120,verbose_name="Başlık")
    content  = models.TextField(verbose_name="İçerik")
    publisihing_date = models.DateTimeField(verbose_name="Yayınlanma Tarihi", auto_now_add=True)
    image = models.ImageField(null=True, blank=True)
    slug = models.SlugField(unique=True)
    def __str__(self):
        return self.title


#return "/post/{}".format(self.id)

    def get_absolute_url(self):
        return reverse('post:detail', kwargs={'id': self.id})

    def get_create_url(self):
        return reverse('post:create')

    def get_update_url(self):
        return reverse('post:update', kwargs={'id': self.id})

    def get_delete_url(self):
        return reverse('post:delete', kwargs={'id': self.id})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title.replace('ı','i'))
        return super(Post, self).save(*args, **kwargs)


    class Meta:
        ordering =['-publisihing_date']