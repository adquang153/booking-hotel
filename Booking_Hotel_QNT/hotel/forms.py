from phong.models import Phong
from django.forms import ModelForm

class formPhong(ModelForm):
    class Meta:
        model=Phong
        fields=['sophong','loaiphong','gia']
        labels= {'sophong':'So Phong'}