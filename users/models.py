from django.db import models


# id,first_name,last_name,username,password,role,age,location_id
# 1,Павел,Никифоров,pnikifirov,gZvptL,member,21,1
class Location(models.Model):
    name = models.CharField(max_length=255, unique=True)
    lat = models.DecimalField(max_digits=8, decimal_places=6)
    lng = models.DecimalField(max_digits=8, decimal_places=6)

    class Meta:
        verbose_name = 'Местоположение'
        verbose_name_plural = 'Местоположения'

    def __str__(self):
        return self.name


class UserRoles:
    MEMBER = 'member'
    MODERATOR = 'moderator'
    ADMIN = 'admin'
    choices = ((MEMBER, 'Пользователь'),
               (MODERATOR, 'Модератор'),
               (ADMIN, 'Администратор'))


class User(models.Model):
    first_name = models.CharField(verbose_name='Имя', max_length=150, null=True)
    last_name = models.CharField(verbose_name='Фамилия', max_length=300, null=True)
    username = models.CharField(verbose_name='Никнэйм', max_length=200, unique=True)
    password = models.CharField(verbose_name='Пароль', max_length=200)
    age = models.PositiveSmallIntegerField()
    location = models.ManyToManyField(Location)
    role = models.CharField(choices=UserRoles.choices, default=UserRoles.MEMBER, max_length=10)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
