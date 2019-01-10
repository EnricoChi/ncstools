from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


class Account(AbstractUser):

    password = models.CharField('password', max_length=128, blank=True)

    class Meta:
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'
