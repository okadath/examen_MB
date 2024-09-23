from django.db import models

from django.contrib.auth.models import AbstractUser

from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set', 
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_permissions',  
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    first_name = models.CharField(max_length=30, verbose_name='First Name')   
    last_name = models.CharField(max_length=30, verbose_name='Last Name')   
    age = models.IntegerField(blank=True, null=True, verbose_name='Age')  
    email = models.EmailField(unique=True, verbose_name='Email')  
    phone = models.CharField(max_length=15, blank=True, null=True, verbose_name='Phone')   

    class Meta:
        verbose_name = 'Custom User'
        verbose_name_plural = 'Custom Users'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
