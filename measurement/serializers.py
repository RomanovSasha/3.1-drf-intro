from rest_framework import serializers
from .models import Sensor
from .models import Measurement
# TODO: опишите необходимые сериализаторы


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['sensor', 'temperature', 'created_at', 'image']


class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']


class SensorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['name', 'description']
