from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login
# Create your views here.

class indexView(LoginRequiredMixin, View):
    login_url="/login/"
    def get(self,request):
        return render(request, 'hoteltp/index.html')
    
class galleryView(LoginRequiredMixin,View):
    login_url="/login/"
    def get(self,request):
        return render(request, 'hoteltp/gallery.html')
    
class asView(LoginRequiredMixin,View):
    login_url="/login/"
    def get(self,request):
        return render(request, 'hoteltp/about-us.html')
    
class bookingView(LoginRequiredMixin,View):
    login_url="/login/"
    def get(self,request):
        return render(request, 'hoteltp/booking.html')

class failedView(LoginRequiredMixin,View):
    login_url="/login/"
    def get(self,request):
        return render(request, 'hoteltp/404.html')
    
class blogView(LoginRequiredMixin,View):
    login_url="/login/"
    def get(self,request):
        return render(request, 'hoteltp/blog.html')    
class loginView(View):
    login_url="/login/"
    def get(self,request):
        return render(request, 'hoteltp/login.html')
    def post(self, request):
        tk = request.POST.get('un')
        mk = request.POST.get('pass')
        my_user = authenticate(username=tk,password=mk)
        if(my_user is None):
            return HttpResponse("User k tồn tại")
        else:
            login(request, my_user)
            return render(request, 'hoteltp/index.html')