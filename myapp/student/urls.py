from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('signup', views.userSignUp, name='signup'),
    path('login', views.userlogin, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('student/', views.student_page, name="student"),
    path('student_marks/', views.student_marks_page, name="student_marks"),
    path('studentInfoView/', views.studentInfoView_page, name="studentInfoView_page"),
    path('studentView/<int:rollNo>/', views.studentView_page, name="studentView"),
    path('search/', views.search_page, name="search"),
    path('editStudentInfo/<int:rollNo>/', views.EditStudentInfo, name="EditStudentInfo"),
    path('deleteStudentInfo/<int:rollNo>/', views.deleteStudentInfo, name="deleteStudentInfo"),
    path('geturl/', views.geturl_page, name='geturl'),

    
]   
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)