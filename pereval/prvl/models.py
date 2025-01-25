from django.db import models


class UserRegister(models.Model):
    email = models.EmailField(db_index=True, max_length=254)
    name = models.CharField(db_index=True, max_length=50)
    phone = models.IntegerField(max_length=20)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['email', 'phone'],
                name='unique_email_pnone'
            )
        ]


class RegisterPereval(models.Model):

    CHOICES_STATUS = [('new', 'Новый'),
                      ('pending', 'На проверке'),
                      ('accepted', 'Проверка пройдена'),
                      ('rejected', 'Проверка пройдена, информация не принята'),
                      ]

    status = models.CharField(db_index=True, choices=CHOICES_STATUS, default='new', max_length=10)
    beauty_title = models.CharField(max_length=20,)
    title = models.CharField(max_length=50)
    other_titles = models.CharField(max_length=50)
    connect = models.DateTimeField(auto_now=True)
    add_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(UserRegister,on_delete=models.CASCADE)
