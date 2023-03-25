from django.urls import path

from StudentApp import views

urlpatterns=[
    path('',views.log_fun,name='log'),#it will display login.htmlpage
    path('logdata',views.logdata_fun),#it wil read the data and verify user is super user

    path('reg',views.reg_fun,name='reg'),#it will redirect to register.html page
    path('regdata',views.regdata_fun), #it will create superuser account

    path('home',views.home_fun,name='home'),#it will redirect to home.html
    path('add_students',views.addstudent_fun,name='add'),#it will redirect to add.html for adding new student
    path('readdata',views.readdata_fun),#it will insert records into studentdata

    path('display',views.display_fun,name='display'),#it will display student table data in display.html file

    path('update/<int:id>',views.update_fun,name='up'),#it will update student data

    path('delete/<int:id>',views.delete_fun,name='del'),#it will delete the data from student table

    path('log_out',views.log_out_fun,name='log_out'),#it will



]