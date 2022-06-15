from django.contrib import admin
from django.urls import path,include
from . import views
import settings
from django.views.static import serve
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    # Go to url of teacher
    path('teacher/',include('teacher.urls')),
    # Go to url of student
    path('student/',include('student.urls')),
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
 

    
]
