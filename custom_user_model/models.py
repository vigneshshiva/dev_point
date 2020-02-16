from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
class Custom_Base_user(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not username:
            raise VallueError('username must filled')
        if not email:
            raise VallueError('email must be entered')
        user = self.model(
            email = self.normalize_email(email),
            username = username,
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self,username,email,password):
        user = self.create_user(
            username = username,
            email = self.normalize_email(email),
            password = password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user

class Custom_user(AbstractBaseUser):
    username = models.CharField(max_length=10000,unique=True)
    email = models.EmailField(unique=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username',]

    objects = Custom_Base_user()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
