# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics

from .models import Sensor
from .models import Measurement
from .serializers import SensorsSerializer, SensorDetailSerializer, MeasurementSerializer, SensorSerializer


class SensorAPIList(generics. ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorsSerializer


class SensorCreate(generics. CreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorUpdate(generics. RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class MeasurementCreate(generics. CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer


class SensorDetail(generics. RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer







