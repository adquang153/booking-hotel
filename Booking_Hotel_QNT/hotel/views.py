from django.shortcuts import render
from django.views import View
# Create your views here.

class indexView(View):
    def get(self,request):
        return render(request, 'hoteltp/index.html')
    
class galleryView(View):
    def get(self,request):
        return render(request, 'hoteltp/gallery.html')
    
class asView(View):
    def get(self,request):
        return render(request, 'hoteltp/about-us.html')
    
class bookingView(View):
    def get(self,request):
        return render(request, 'hoteltp/booking.html')

class failedView(View):
    def get(self,request):
        return render(request, 'hoteltp/404.html')
    
class blogView(View):
    def get(self,request):
        return render(request, 'hoteltp/blog.html')    