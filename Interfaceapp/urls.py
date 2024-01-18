from django.urls import path
from Interfaceapp import views



urlpatterns =[
    path('Rdrct/', views.Rdrct, name='Rdrct'),

    path('interface/', views.interface, name='interface'),
    path('menuFun/', views.menuFun, name='menuFun'),
    path('aboutFun/', views.aboutFun, name='aboutFun'),
    path('contactFun/', views.contactFun, name='contactFun'),
    path('getInTouch/', views.getInTouch, name='getInTouch'),
    path('saveGet/', views.saveGet, name='saveGet'),

    path('proindex/', views.proindex, name='proindex'),
    path('buyPro/<cat_name>/', views.buyPro, name='buyPro'),
    path('serviceMain/', views.serviceMain, name='serviceMain'),
    path('singleProduct/<int:dataid>', views.singleProduct, name='singleProduct'),

    path('login_user/', views.login_user, name='login_user'),
    path('signup_user/', views.signup_user, name='signup_user'),
    path('signup_savedata/', views.signup_savedata, name='signup_savedata'),
    path('userLogin/', views.userLogin, name='userLogin'),
    path('userLogout/', views.userLogout, name='userLogout'),

    path('serviceSave/', views.serviceSave, name='serviceSave'),
    

]