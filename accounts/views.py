from django.shortcuts import render,HttpResponse
from .models import Users,OTPValidator
from random import randrange
import requests

def generate_otp(uid,ph):
    otp = randrange(111111, 999999)
    apikey = "ftOniK9KXe0-NpX9KYi6vgmE3nLYZVGW1wiMsQajQe"
    address = "https://api.textlocal.in/send/?"
    message = "Your OTP is " +str(otp)
    numbers = "91"+str(ph)
    sender = "TXTLCL"
    url = address + "apikey=" + apikey + "&numbers=" + numbers + "&message=" + message + "&sender=" + sender
    resp = requests.get(url)
    if resp.json().get('status') == 'success':
        OTPValidator(otp=otp, uid=uid).save()
        return 1
    else:
        return 0

# Create your views here.
def home(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['pwd']
        phone = request.POST['ph']
        user = Users(name=name,email=email,password=password,phone=phone)
        user.save()
        obj = Users.objects.get(email=email)
        otp_status = generate_otp(obj.id,phone)
        if not otp_status:
            return HttpResponse('Enter a valid otp')
        return render(request, 'enter-opt.html', {'uid':obj.id})

    return render(request, 'user-form.html')

def validate_otp(request):
    if request.method == 'POST':
        otp = request.POST['otp']
        uid = request.POST['uid']
        try:
            obj = OTPValidator.objects.get(otp=otp, uid=uid)
            uobj = Users.objects.get(id=uid)
            uobj.ph_valid = 1
            uobj.save()
            obj.delete()
            return HttpResponse("Your Phone number has validated sucessfully")
        except:
            return HttpResponse("Invalid OTP")