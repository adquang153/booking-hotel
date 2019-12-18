from django.db import models
from khachhang.models import KhachHang
from phong.models import Phong
from django.utils import timezone
# Create your models here.
class ChiTietBooking(models.Model):
    mabooking= models.CharField(max_length=30,primary_key=True)
    tendn= models.ForeignKey(KhachHang, on_delete=models.CASCADE)
#     tenkh= models.ForeignKey(KhachHang, on_delete=models.CASCADE)
    sophong= models.ForeignKey(Phong, on_delete=models.CASCADE)
    ngaynhanphong= models.DateTimeField(default= timezone.now)
    ngaytratphong= models.DateTimeField(default= timezone.now)
    thanhtien=models.BigIntegerField(default=0)
    
    def __str__(self):
        return self.mabooking