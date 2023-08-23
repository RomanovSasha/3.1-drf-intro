from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)


class Sensor(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200)


class Measurement(models.Model):
    #id = models.DecimalField(max_digits=10, decimal_places=2, primary_key=True)
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, default=None)
    #tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='scopes', verbose_name='Тэг')

