from django.db import models
from rest_framework.serializers import ModelSerializer

from base.entity import BaseEntity
from sample_app.entity.palette import Palette


class Map(BaseEntity):
    grid_id = models.AutoField(primary_key=True)
    map_id = models.IntegerField(null=False)
    x = models.IntegerField(null=False)
    y = models.IntegerField(null=False)
    z = models.IntegerField(null=False)
    palette_id = models.ManyToManyField(Palette,
                                        through="MapsPalettes",
                                        related_name="maps_palettes")

    class Meta:
        db_table = "maps"


class MapSerializer(ModelSerializer):
    class Meta:
        model = Map
        fields = '__all__'
