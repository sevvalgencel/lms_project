from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from .import views, user_login
from django.conf import settings
from django.conf.urls.static import static
from .views import contact_us,success

urlpatterns = (
    [
    path('admin', admin.site.urls),
    path('base', views.BASE, name='base'),
    path('404',views.PAGE_NOT_FOUND,name='404'),
    path('', views.HOME, name='home'),
    path('courses', views.SINGLE_COURSE, name='single_course'),
    path('courses/filter-data',views.filter_data,name="filter-data"),
    path('course/<slug:slug>',views.COURSE_DETAILS,name='course_details'),
    path('search',views.SEARCH_COURSE,name='search_course'),
    path('contact/', contact_us, name='contact_us'),
    path('about', views.ABOUT_US, name='about_us'),
    path('accounts/register', user_login.REGISTER, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('doLogin', user_login.DO_LOGIN, name='doLogin'),
    path('accounts/profile', user_login.PROFILE, name='profile'),
    path('accounts/profile/update', user_login.PROFILE_UPDATE,name='profile_update'),
    path('checkout/<slug:slug>',views.CHECKOUT, name='checkout'),
    path('my-course',views.MY_COURSE,name= 'my-course')
    ]+ static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
                )

