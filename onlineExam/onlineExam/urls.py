from django.contrib import admin
from django.urls import path
from student import views

urlpatterns = [
    # 管理员登陆
    path('admin/', admin.site.urls),
    # 学生登陆
    path('studentLogin/', views.studentLogin),
    # 教师登陆
    path('teacherLogin/', views.teacherLogin),
    # 默认访问首页
    path('', views.index),
    path('toIndex/', views.toIndex),
    path('showGrade/', views.showGrade),
    path('queryStudent/', views.queryStudent),
    path('startExam/', views.startExam),
    path('calGrade/', views.calGrade),
    path('logout/', views.logOut),
]
