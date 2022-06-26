from django.db import models

# User Model
class Dsuser(models.Model):
    # Primary Key
    id = models.AutoField(primary_key=True)
    # User Information
    user_id = models.CharField(max_length=20, unique=True)
    email = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=20)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now_add=True)