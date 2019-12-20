from django.shortcuts import render
from django.views import View
# Create your views here.

class formview(View):
    def get(self,request):
        return render(request, 'hoteltp/index-two.html')