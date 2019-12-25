from django.shortcuts import render,redirect
from chitietbooking.models import ChiTietBooking
from django.views import View
from .forms import SignUpForm,formCTBK
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login,get_user_model, logout
from django.contrib.auth.forms import UserCreationForm
from phong.models import Phong
from khachhang.models import MyUser
# Create your views here.

class indexView(LoginRequiredMixin, View):
    login_url="/login/"
    def get(self,request):
        form = Phong.objects.all()
        context = {'f':form}
        return render(request, 'hoteltp/index.html',context)
    def post(self,request):
        sp = request.POST.get('sp')
        f = Phong.objects.get(sophong=sp)
#         f.active = True
#         f.save()
#         form = Phong.objects.all()
#         context = {'f':form}
        context = {'f' : f}
        return render(request, 'hoteltp/booking.html',context)
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
        form=ChiTietBooking.objects.all()
        context={"f":form}
        return render(request, 'hoteltp/booking.html',context)
    def post(self,request):
        sp = request.POST.get("sp")
        tentk = request.POST.get("tentk")
        a = MyUser.objects.get(username=tentk)
        f = Phong.objects.get(sophong=sp)
        f.active = True
        f.save()
        f3 = ChiTietBooking(tendn=a,sophong=f)
        f3.save()
        form = Phong.objects.all()
        context = {'f':form}
        return render(request,'hoteltp/index.html',context)
        
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
            return render(request, 'hoteltp/login.html')
        else:
            login(request, my_user)
#             return render(request, 'hoteltp/index.html')
            return redirect('hotel:index')
class resView(View):
    def get(self,request):
        form = SignUpForm()
        context = {'form': form}
        return render(request, 'hoteltp/res.html', context)   
    def post(self,request):
        dki = SignUpForm(request.POST)
        if(dki.is_valid()):
            dki.save()
            tk = request.POST.get('username')
            mk = request.POST.get('password1')
            my_user = authenticate(username=tk,password=mk)
            login(request, my_user)
#             return render(request,'hoteltp/index.html')
            return redirect('hotel:index')
        else:
            return render(request,'hoteltp/res.html')
class logoutView(View):
    def get(self,request):
        logout(request)
        return redirect('hotel:login')     