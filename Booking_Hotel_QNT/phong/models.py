from django.db import models

# Create your models here.

class Phong(models.Model):
    choice_phong = {(0,"Phòng cao cấp Loại 1"),(1,"Phòng đơn"),(2,"Phòng đôi"),(3,"Phòng trẻ em")}
    sophong= models.CharField(max_length=30,primary_key=True,null=False)
    loaiphong = models.IntegerField(choices = choice_phong,default=0)
    gia= models.BigIntegerField(default=0)
    
    def __str__(self):
        return self.sophong