from django.db import models
from rest_framework.serializers import ListSerializer, ModelSerializer

from base.entity import BaseEntity

# from sample_app.entity.map import Map
# from sample_app.entity.palette import Palette


class MapsPalettes(BaseEntity):
    id = models.AutoField(primary_key=True)
    grid_id = models.ForeignKey("GlobalMap",
                                db_column="grid_id",
                                on_delete=models.CASCADE)
    palette_id = models.ForeignKey("Palette",
                                   db_column="palette_id",
                                   on_delete=models.CASCADE)

    class Meta:
        db_table = "maps_palettes"
        constraints = [
            models.UniqueConstraint(fields=["grid_id", "palette_id"],
                                    name="maps_palettes_grid_id_palette_id_key"
                                    )
        ]


class MapsPalettesListSerializer(ListSerializer):
    '''複数処理用のシリアライザクラス
    '''

    def create(self, validated_data):
        data = [MapsPalettes(**vd) for vd in validated_data]
        return MapsPalettes.objects.bulk_create(data)

    class Meta:
        model = MapsPalettes
        fields = '__all__'


class MapsPalettesSerializer(ModelSerializer):
    class Meta:
        model = MapsPalettes
        fields = '__all__'
        list_serializer = MapsPalettesListSerializer
