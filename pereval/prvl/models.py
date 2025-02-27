from operator import index
from tkinter.constants import CASCADE

from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser


class Users(models.Model):
    email = models.EmailField(unique=True, max_length=254)
    name = models.CharField(max_length=50)
    phone = models.CharField(unique=True, max_length=20)
    otc = models.CharField(max_length=100)
    fam = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.email}'


class Levels(models.Model):

    CHOICES_LEVEL = [('1A', '1а'),
                     ('1B', '1б'),
                     ('2A', '2а'),
                     ('2B', '2б'),
                     ('3A', '3а'),
                     ('3B', '3б'),
                     ('3B*', '3б*')
                     ]

    summer = models.CharField(choices=CHOICES_LEVEL, default='1A', max_length=10)
    autumn = models.CharField(choices=CHOICES_LEVEL, default='1A', max_length=10)
    winter = models.CharField(choices=CHOICES_LEVEL, default='1A', max_length=10)
    spring = models.CharField(choices=CHOICES_LEVEL, default='1A', max_length=10)


class Coords(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    height = models.IntegerField()


class Perevals(models.Model):

    CHOICES_STATUS = [('new', 'Новый'),
                      ('pending', 'В работе'),
                      ('accepted', 'Принято'),
                      ('rejected', 'Отколонено'),
                      ]

    status = models.CharField(db_index=True, choices=CHOICES_STATUS, default='new', max_length=10)
    beauty_title = models.CharField(blank=True, max_length=20,)
    title = models.CharField(blank=True, max_length=50)
    other_titles = models.CharField(blank=True, max_length=50)
    connect = models.DateTimeField(auto_now=True)
    add_time = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    level = models.OneToOneField(Levels, on_delete=models.CASCADE)
    coord = models.OneToOneField(Coords, on_delete=models.CASCADE)


class Images(models.Model):
    data = models.ImageField()
    title = models.CharField(max_length=254)


class PerevalImages(models.Model):
    pereval = models.OneToOneField(Perevals, on_delete=models.CASCADE, related_name='pereval_images_pereval')
    image = models.OneToOneField(Perevals, on_delete=models.CASCADE, related_name='pereval_images_image')