"""
URL configuration for NASEEHA project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from NASEEHA.views import *
from doctors.views import *
from hospital.views import *
from interactions.views import *
from chat.views import *
urlpatterns = [
    # path('admin/', admin.site.urls, name='admin'),
    # naseeha
    path('', homepage, name='homepage'),
    path('login/', login_user, name='login'),
    path('services/', services, name='services'),
    path('signup/', signup, name='signup'),
    path('authenticate_userp/', authenticate_userp),
    path('logout/', logout, name='logout'),
    path("admin_profile/", admin_profile, name='admin_profile'),
    path("add_hospital", add_hospital, name='add_hospital'),


    # hospital
    path('user_profile/', profile, name='user_profile'),
    path('edit_profile/', editprofile, name='editprofile'),
    path('handle_edit_profile/', handle_editprofile, name='handleedit'),
    path('survey/', forms, name='survey'),
    path("appointment_list/", appointment_list, name="appointment_list"),
    path("save_hospital/", save_hospital, name="save_hospital"),
    path("assign_dept/", assign_dept, name="assign_dept"),
    path("hospital/", hospital, name="hospital"),
    path("hospitaldetails/", hospitaldetails, name="hospitaldetails"),
    path("department_doctor/", hos_dept_wise_doc, name="hos_dept_wise_doc"),

    # doctor
    path("doctorBase/", doctorBase),
    path("doctor_profile/", doctor_profile, name='doctor_profile'),
    path("doctor_edit_profile/", doctor_edit_profile, name='doc_edit_profile'),
    path("handle_doctor_edit_profile/", handle_doctor_edit_profile,
         name='handle_doc_edit_profile'),
    path("patientlist/", patientlist, name='patientlist'),

    # interactions
    path("req_appointment/", request_appointment, name='req_appointment'),
    path("appointment_details/", appointment_details, name='appointment_details'),
    path("update_appointment/", update_appointment, name='update_appointment'),


    # chat
    path("chat/", chatHome, name='chatHome'),
    path("get_chats/", get_chats, name='getMessages'),
    path("send_chat/", send_chat, name='sendMessages'),

]
