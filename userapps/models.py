from django.db import models
from django.contrib.auth.models import User


GENDER = (
    ('M','M'),
    ('F','F'),
)
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=50)
    gender = models.CharField(max_length=50,choices=GENDER, default='M')
    profile_pix = models.ImageField(upload_to='profile',default="https://www.pngplay.com/wp-content/uploads/12/User-Avatar-Profile-PNG-Pic-Clip-Art-Background.png",null=True,blank=True)

    def __str__(self):
        return self.user.username
