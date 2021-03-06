"""workinghour URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include, re_path

from apps.user import views as user_views
from apps.record import views as record_views
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'own', record_views.OwnRecordViewSet, "own records")
router.register(r'records', record_views.RecordViewSet, "records")
router.register(r'users', user_views.UsersViewSet, "users")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signin/', user_views.LoginView.as_view()),
    path('signup/', user_views.RegisterView.as_view()),
    path('profile/', user_views.ProfileView.as_view()),
    path('workinghour/', record_views.WorkingHourView.as_view()),
    path('export/', record_views.ExportView.as_view()),
    re_path(r'^', include(router.urls))
]
