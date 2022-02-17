from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
import hmac
import time
import hashlib

@login_required
def userView(request): #127.0.0.1:8000/user
    return render(request, 'user.html')

@staff_member_required
def staffView(request): # 127.0.0.1:8000/staff
    return render(request, 'staff.html')
list = []
def signup(request):
    form = UserCreationForm()    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(username=user.username, 
                                password=request.POST['password1'])
            login(request, user)
            return redirect('/')    
    context = {'form' : form}
    return render(request, 'registration/signup.html', context)
password = "qA090296"
pivot = 1607048354.1137462
def truncate(hmac_res):
    offset = int(hmac_res[38:],16)&0xf
    return int(hmac_res[offset*2:offset*2+8],16)%10**6

def otp_generate(mess):
    t = time.time()
    intput_key =  str(int((t-pivot)/30))
    h = hmac.new(key=bytes(intput_key.encode('utf-8')), msg=bytes(mess.encode('utf-8')), digestmod=hashlib.sha1)
    return str(truncate(h.hexdigest()))
def index(request):
    a = request.POST.get("otp")
    if(a == otp_generate(password)):
        return render(request, 'S1mple.html')
    return render(request, 'index.html')