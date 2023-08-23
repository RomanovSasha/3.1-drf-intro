from django.contrib import admin
from django.urls import path

from measurement.views import SensorAPIList, SensorCreate, SensorUpdate, MeasurementCreate, SensorDetail

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты

    path('sensors/', SensorAPIList.as_view()),
    path('sensorcreate/', SensorCreate.as_view()),
    path('sensorupdate/<pk>/', SensorUpdate.as_view()),
    path('measurements/', MeasurementCreate.as_view()),
    path('sensordetail/<pk>/', SensorDetail.as_view()),


]


