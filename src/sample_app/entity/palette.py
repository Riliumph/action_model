from django.db import models
from rest_framework.serializers import ModelSerializer

from base.entity import BaseEntity
from sample_app.entity.map import Map



class Palette(BaseEntity):
    palette_id = models.AutoField(primary_key=True)
    qr_id = models.IntegerField(null=False)

    grid_id = models.ManyToManyField(Map, through=)

    class Meta:
        db_table = "palettes"
        constraints = [
            models.UniqueConstraint(fields=["palette_id", "qr_id"],
                                    name="palettes_palette_id_qr_id_key"
                                    )
        ]


class PaletteSerializer(ModelSerializer):
    class Meta:
        model = Palette
        fields = '__all__'