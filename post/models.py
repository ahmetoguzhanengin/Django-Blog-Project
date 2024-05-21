from django.db import models
from django.urls import  reverse
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=120,verbose_name="Başlık")
    content  = models.TextField(verbose_name="İçerik")
    publisihing_date = models.DateTimeField(verbose_name="Yayınlanma Tarihi", auto_now_add=True)
    def __str__(self):
        return self.title


#return "/post/{}".format(self.id)

    def get_absolute_url(self):
        return reverse('post:detail', kwargs={'id': self.id})