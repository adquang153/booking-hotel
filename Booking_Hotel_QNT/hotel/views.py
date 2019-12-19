from django.shortcuts import render
from django.views import View
from django.http.response import HttpResponse
from .forms import formPhong
from phong.models import Phong
# Create your views here.

class formview(View):
    def get(self,request):
        form= Phong.objects.all()
        context={"f":form}
        return render(request, 'hoteltp/test.html',context)