from django.contrib import admin
from . import views
from django.urls import path


app_name = 'web'

urlpatterns = [
    path('', views.index, name="index"),
    # path('admin/', admin.site.urls),
]
