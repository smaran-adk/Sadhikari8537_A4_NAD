from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user =models.OneToOneField(User, on_delete=models.CASCADE)
    bio= models.TextField(blank=True)
    OnePiece=models.ImageField(default='luffy.jpg', upload_to='One Piece') 
    updated = models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"profile of the user {self.user.username}"