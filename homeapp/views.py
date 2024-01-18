from django.shortcuts import render, redirect
from homeapp.models import userDb,CatDb,ProductDb
from Interfaceapp.models import GetDb, ServiceDb, SignupDb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.

def index_fun(request):
    return render(request, 'index.html')

def add_fun(a):
    cat = CatDb.objects.all()
    return render(a, 'workers/regn.html', {'cat': cat})

def view_fun(v):
    if v.method == 'POST':
        na = v.POST.get('rname')
        ct = v.POST.get('rcat')
        mb = v.POST.get('rmob')
        em = v.POST.get('remail')
        pd = v.POST.get('rpswd')
        ds = v.POST.get('rtext')
        im = v.FILES['rimg']
        obj = userDb(Name=na, Category=ct, Mobile=mb, Email=em, Password=pd, Description=ds, Image=im)
        obj.save()
        messages.success(v, 'Worker added sucessfully..!')
        return redirect('add_fun')

def disp_fun(d):
    users = userDb.objects.all()
    return render(d, 'workers/disp.html', {'users': users})   

def edit_fun(e, userid):
    users = userDb.objects.get(id=userid)
    return render(e, 'workers/edit.html', {'users': users})    
    
def del_fun(d, userid):
    users = userDb.objects.filter(id=userid)
    users.delete()
    messages.error(d, 'Worker removed..!')
    return redirect('disp_fun')

def update_fun(u, userid):    
    if u.method == 'POST':
        na = u.POST.get('rname')
        ct = u.POST.get('rcat')
        mb = u.POST.get('rmob')
        em = u.POST.get('remail')
        ps = u.POST.get('rpswd')
        ds = u.POST.get('rtext')
        try:
            im = u.FILES['rimg']
            fs = FileSystemStorage()
            file = fs.save(im.name, im)
        except MultiValueDictKeyError:
            file =  userDb.objects.get(id=userid).Image
        userDb.objects.filter(id=userid).update(Name=na, Category=ct, Mobile=mb, Email=em, Password=ps, Description=ds, Image=file)      
        messages.success(u, 'Worker updated sucessfully..!')
        return redirect('disp_fun')



# ===================================== ADMIN_RENDER_SECTION =============================================


def adlogin(request):
    return render(request, 'admin/adinface.html')
   
def adminLogin(request):
    if request.method == 'POST':
        unm = request.POST.get('uname')
        pwd = request.POST.get('pswrd')
        if User.objects.filter(username__contains=unm).exists():
            x = authenticate(username=unm, password=pwd)
            if x is not None:
                login(request, x)
                request.session['username'] = unm
                request.session['password'] = pwd
                messages.success(request, 'Welcome to Admin Panel...!')
                return redirect('index_fun')
            else:
                messages.error(request, 'Login Error..!')
                return redirect('adlogin')   
        else:
            messages.error(request, 'Login Error..!')
            return redirect('adlogin')

def adminLogout(request):
    del request.session['username']
    del request.session['password']
    return redirect('adlogin')



# ===================================== CATEGORY_SECTION ===============================================



def addCat(a):
    return render(a, 'categories/CatAdd.html')

def catData(c):
    if c.method == 'POST':
        na = c.POST.get('cname')
        ds = c.POST.get('ctext')
        im = c.FILES['cimg']
        obj = CatDb(Cat_Name=na, Cat_Desc=ds, Cat_Image=im)
        obj.save()
        messages.success(c, 'Category added sucessfully...!')
        return redirect('addCat')

def disCat(d):
    cat = CatDb.objects.all()
    return render(d, 'categories/CatDisplay.html', {'cat': cat})   

def editCat(e, catId):
    cat = CatDb.objects.get(id=catId)
    return render(e, 'categories/CatEdit.html', {'cat': cat})

def updateCat(u, catId):
    na = u.POST.get('uname')
    ds = u.POST.get('utext')
    try:
        im = u.FILES['uimg']
        fs = FileSystemStorage()
        file = fs.save(im.name, im)
    except MultiValueDictKeyError:
        file =  CatDb.objects.get(id=catId).Cat_Image
    CatDb.objects.filter(id=catId).update(Cat_Name=na, Cat_Desc=ds, Cat_Image=file)
    messages.success(u, 'Category updated successfully...!')
    return redirect('disCat')       

def deleteCat(d, catId):
    cat = CatDb.objects.filter(id=catId)
    cat.delete()
    messages.error(d, 'Category removed...!')
    return redirect('disCat')


# ===================================== PRODUCTS_SECTION ===============================================


def addProduct(p):
    Category = CatDb.objects.all() 
    return render(p, 'products/ProductAdd.html', {'Category': Category})

def saveProduct(s):
    if s.method=='POST':
        cat = s.POST.get('pcat')
        nam = s.POST.get('pname')
        prc = s.POST.get('price')
        des = s.POST.get('pdesc')
        img = s.FILES['pimg']
        obj = ProductDb(ProCat_Name=cat, ProName=nam, ProPrice=prc, Pro_Desc=des, Pro_Image=img)
        obj.save()
        messages.success(s, 'Product added successfully...!')
        return redirect('addProduct')

def displayProducts(d):
    product = ProductDb.objects.all()
    return render(d, 'products/ProductDisplay.html', {'product': product})

def editProducts(e, ProId):
    cat = CatDb.objects.all()
    product = ProductDb.objects.get(id=ProId)
    return render(e, 'products/ProductEdit.html', {'product': product, 'cat': cat})

def updateProducts(u, ProId):
    if u.method == 'POST':
        cat = u.POST.get('upcat')
        nam = u.POST.get('upname')
        prc = u.POST.get('uprice')
        des = u.POST.get('updesc')
        try:
            img = u.FILES['upimg']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = ProductDb.objects.get(id=ProId).Pro_Image
        ProductDb.objects.filter(id=ProId).update(ProCat_Name=cat, ProName=nam, ProPrice=prc, Pro_Desc=des, Pro_Image=file) 
        messages.success(u, 'Product updated successfully...!')
        return redirect('displayProducts')   

def deleteProducts(d, ProId):
    product = ProductDb.objects.filter(id=ProId)
    product.delete()
    messages.error(d, 'Product removed...!')
    return redirect('displayProducts')


# =================================== USER_FEEDBACK_FROM_INTERFACEAPP ==============================================
        

def getIn_display(disp):
    users = GetDb.objects.all()
    return render(disp, 'users/getindisplay.html', {'users': users})

def getIn_delete(rem, getId):
    users = GetDb.objects.filter(id=getId)
    users.delete()
    messages.error(rem, 'User Feedback removed...!')
    return redirect('getIn_display')


# ===================================== USER_REQUESTS_SECTION ===============================================


def reqservice(r): 
    requests = ServiceDb.objects.all()
    return render(r, 'users/userReq.html', {'requests': requests})

def reqDelete(d, reqId):
    requests = ServiceDb.objects.filter(id=reqId)
    requests.delete()
    messages.error(d, 'User requests removed...!')
    return redirect(reqservice)


# ===================================== SIGNUP_DETAILS_SECTION ===============================================


def userdetails(u):
    users = SignupDb.objects.all()
    return render(u, 'users/userDetails.html', {'users': users})

def userdelete(d, userid):
    users = SignupDb.objects.filter(id=userid)
    users.delete()
    return redirect(userdetails)













# ========================================= REDIRECTION_FN() ====================================================

def generalFun(gen):
    return render(gen, 'main/Interface.html')