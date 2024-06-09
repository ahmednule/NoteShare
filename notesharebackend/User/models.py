from django.db import models
from django.contrib.auth.models import AbstractUser


#Abstract user 
class User(AbstractUser):
  class Meta:
        db_table = 'User_user'
  