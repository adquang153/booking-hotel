from django.db import models

# Create your models here.
class KhachHang(models.Model):
    tendn= models.CharField(max_length=30,primary_key=True, null=False)
    tenkh= models.CharField(max_length=50,null=False)
    email= models.CharField(max_length=50)
    password= models.CharField(max_length=30 , null=False)
    sdt= models.CharField(max_length=11,null=False)
    
    def __str__(self):
        return self.tendn
    