from django.shortcuts import render, redirect
from homeapp.models import CatDb,ProductDb 
from Interfaceapp.models import GetDb, SignupDb, ServiceDb
# from homeapp import views
from django.contrib import messages

# Create your views here.

def Rdrct(rd):
    return render(rd, 'index.html')

def interface(request):
    return render(request, 'main/Interface.html') 

def menuFun(m):
    return render(m, 'main/menu.html')

def aboutFun(ab):
    return render(ab, 'main/about.html')

def contactFun(c):
    return render(c, 'main/contact.html')

def getInTouch(g):
    return render(g, 'main/getinTouch.html')

def saveGet(s):
    if s.method == 'POST':
        nm = s.POST.get('gname')
        em = s.POST.get('gmail')
        ds = s.POST.get('gdesc')
        obj = GetDb(Name=nm, Email=em, Description=ds)
        obj.save()
        messages.success(s, "Your feedbacks are submitted sucessfully..!")
        return redirect(getInTouch)
    
    

def proindex(r):
    category = CatDb.objects.all() 
    return render(r, 'sales/salesCategory.html', {'category': category})

def buyPro(b, cat_name):
    products = ProductDb.objects.filter(ProCat_Name=cat_name)
    return render(b, 'sales/salesProducts.html', {'products': products})

def singleProduct(s, dataid):
    data = ProductDb.objects.get(id=dataid)
    return render(s, 'sales/singleProduct.html', {'data': data})


def login_user(r):
    return render(r, 'forms/Login.html')

def signup_user(r):
    return render(r, 'forms/Register.html')

def signup_savedata(s):
    if s.method == 'POST':
        nm = s.POST.get('sname')
        mb = s.POST.get('smobile')
        em = s.POST.get('smail')
        pd = s.POST.get('pswd')
        cp = s.POST.get('cfpwsd')
        obj = SignupDb(Name=nm, Mobile=mb, Email=em, Pswd=pd, CfrmPswd=cp)
        obj.save()
        messages.success(s, "User account created successfully..!")
        return redirect(signup_user)

def userLogin(request):
    if request.method == 'POST':
        user = request.POST.get('username')
        pswd = request.POST.get('password')
        if SignupDb.objects.filter(Email=user, Pswd=pswd).exists():
            request.session['Email'] = user
            request.session['Pswd'] = pswd
            messages.success(request, "User login successful..!")
            return redirect(interface)
        else:
            messages.error(request, "User not found..!")
            return redirect(login_user)
    else:
        messages.error(request, "User not found..!")
        return redirect(login_user)
   
def userLogout(request):
    del request.session['Email']
    del request.session['Pswd']
    messages.warning(request, "User logout..!")
    return redirect(login_user)



def serviceMain(s):
    category = CatDb.objects.all()
    return render(s, 'services/services.html', {'category': category})

def serviceSave(v):
    if v.method == 'POST':
       nm = v.POST.get('rname')
       ml = v.POST.get('rmail')
       sl = v.POST.get('rselect')
       ph = v.POST.get('rphone')
       rad = v.POST.get('raddress')
       obj = ServiceDb(Name=nm, Email=ml, Select=sl, Phone=ph, Address=rad)
       obj.save()
       messages.success(v, "Service request placed successfully...!")
       return redirect(serviceMain)