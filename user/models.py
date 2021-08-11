from django.db import models
from django.forms import ModelForm, Textarea


class UserInfo(models.Model):
    Full_name = models.CharField(max_length=100)
    Profile_image = models.ImageField(upload_to='images/')
    Email_ID = models.EmailField()
    Short_description = models.TextField(max_length=200)
    Long_description = models.TextField(max_length=1000)
    Degree = models.CharField(max_length=100)
    Year_of_passing = models.IntegerField()
    Certificate_image = models.ImageField(upload_to='images/')

    #def __str__(self):
        #return self.Full_name

    class Meta:
        db_table = "userinfo"
