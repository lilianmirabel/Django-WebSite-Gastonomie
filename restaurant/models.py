from django.db import models
from django.contrib.auth.models import User
import datetime

class TypeResto(models.Model):
    noType              = models.AutoField(primary_key=True)
    nomType             = models.CharField(max_length=20)

    def __str__(self):
        return self.nomType

class Restaurant(models.Model):
    noRestaurant        = models.AutoField(primary_key=True)
    nomRestaurant       = models.CharField(max_length=25)
    villeRestaurant     = models.CharField(max_length=25)
    typeRestaurant      = models.ForeignKey(TypeResto,on_delete=models.DO_NOTHING)
    
class Commentaire(models.Model):
    noCommentaire       = models.AutoField(primary_key=True)
    noRestaurant        = models.ForeignKey(Restaurant,on_delete=models.DO_NOTHING)
    userName            = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    commentaire         = models.TextField()   
    note                = models.IntegerField(default=0)       
    dateCommentaire     = models.DateField(auto_now_add=True)
    
    
    