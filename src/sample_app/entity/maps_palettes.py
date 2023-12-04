from django.db import models
from rest_framework.serializers import ModelSerializer

from base.entity import BaseEntity
from sample_app.entity.map import Map
from sample_app.entity.palette import Palette


class MapsPalettes(BaseEntity):
    id = models.AutoField(primary_key=True)
    grid_id = models.ForeignKey(Map,
                                db_column="grid_id",
                                on_delete=models.CASCADE)
    palette_id = models.ForeignKey(Palette,
                                   db_column="palette_id",
                                   on_delete=models.CASCADE)

    class Meta:
        db_table = "maps_palettes"


class MapsPalettesSerializer(ModelSerializer):
    class Meta:
        model = MapsPalettes
        fields = '__all__'
