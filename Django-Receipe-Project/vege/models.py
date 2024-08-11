from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Receipe(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    receipe_name = models.CharField(max_length=100)
    receipe_description = models.TextField()
    receipe_Image = models.ImageField(upload_to="receipe/")


# here on_delete=models.SET_NULL means that if the user get deleted then all the receipes associated with it must be set to null
# so that our data will remain consistent throughout the database othewise we will get error.
