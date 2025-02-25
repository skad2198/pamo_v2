from django.contrib import admin
from . import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings


app_name = 'web'

urlpatterns = [
    path('', views.index, name="index"),
    # path('admin/', admin.site.urls),
    path('cars/', views.cars_page, name='cars'),
    path('cars/<int:car_id>/', views.cars_details, name='cars_details'),
]
