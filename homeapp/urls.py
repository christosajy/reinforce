from django.urls import path
from homeapp import views

urlpatterns = [

    # path to Interfaceapp Home
    path('generalFun/', views.generalFun, name='generalFun'),

    # Index
    path('index_fun/', views.index_fun, name='index_fun'), 
    path('add_fun/', views.add_fun, name='add_fun'),
    path('view_fun/', views.view_fun, name='view_fun'),
    path('disp_fun/', views.disp_fun, name='disp_fun'),
    path('edit_fun/<int:userid>', views.edit_fun, name='edit_fun'),
    path('del_fun/<int:userid>', views.del_fun, name='del_fun'),
    path('update_fun/<int:userid>', views.update_fun, name='update_fun'),


    # login
    path('adlogin/', views.adlogin, name='adlogin'),
    path('adminLogin/', views.adminLogin, name='adminLogin'),
    path('adminLogout/', views.adminLogout, name='adminLogout'),


    # Category
    path('addCat/', views.addCat, name='addCat'),
    path('catData/', views.catData, name='catData'),
    path('disCat/', views.disCat, name='disCat'),
    path('editCat/<int:catId>/', views.editCat, name='editCat'),
    path('updateCat/<int:catId>/', views.updateCat, name='updateCat'),
    path('deleteCat/<int:catId>/', views.deleteCat, name='deleteCat'),


    # Product
    path('addProduct/', views.addProduct, name='addProduct'),
    path('saveProduct/', views.saveProduct, name='saveProduct'),
    path('displayProducts/', views.displayProducts, name='displayProducts'),
    path('editProducts/<int:ProId>/', views.editProducts, name='editProducts'),
    path('updateProducts/<int:ProId>/', views.updateProducts, name='updateProducts'),
    path('deleteProducts/<int:ProId>/', views.deleteProducts, name='deleteProducts'),


    # Get In Touch 
    path('getIn_display/', views.getIn_display, name='getIn_display'),
    path('getIn_delete/<int:getId>/', views.getIn_delete, name='getIn_delete'),


    path('reqservice/', views.reqservice, name='reqservice'),
    path('reqDelete/<int:reqId>/', views.reqDelete, name='reqDelete'),


    path('userdetails/', views.userdetails, name='userdetails'),
    path('userdelete/<int:userid>/', views.userdelete, name='userdelete'),




]
