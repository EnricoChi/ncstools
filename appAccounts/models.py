from django.contrib.auth.models import AbstractUser
from django.db import models

from django.core import serializers
from djongo.models.json import JSONField


class Account(AbstractUser):
    password = models.CharField('password', max_length=128, blank=True)

    class Meta:
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'

    def get_projects(self):
        return serializers.serialize('json', Project.objects.filter(user=self))


class Project(models.Model):
    name = models.CharField(
        'Project name', max_length=255)
    info = models.TextField(
        'Project info')
    user = models.ForeignKey(
        'Account', verbose_name='User', on_delete=models.CASCADE)
    files = JSONField(
        'Files', null=True, blank=True)

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def __str__(self):
        return self.name
