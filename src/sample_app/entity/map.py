from django.db import models
from rest_framework.serializers import ModelSerializer

from base.entity import BaseEntity
from sample_app.entity.maps_palettes import MapsPalettes
from sample_app.entity.palette import Palette


class GlobalMap(BaseEntity):
    grid_id = models.AutoField(primary_key=True)
    map_id = models.IntegerField(null=False)
    x = models.IntegerField(null=False)
    y = models.IntegerField(null=False)
    z = models.IntegerField(null=False)
    palettes = models.ManyToManyField(Palette,
                                      through=MapsPalettes,
                                      related_name="palettes")

    class Meta:
        db_table = "maps"


class MapSerializer(ModelSerializer):
    class Meta:
        model = GlobalMap
        fields = '__all__'
