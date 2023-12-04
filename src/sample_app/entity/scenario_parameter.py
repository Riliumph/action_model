from django.db import models
from rest_framework.serializers import ModelSerializer

from base.entity import BaseEntity


class ScenarioParameter(BaseEntity):
    parameter_id = models.AutoField(primary_key=True)
    parameter_gid = models.IntegerField(null=False)
    p_key = models.TextField(null=False)
    p_value = models.TextField(null=False)

    class Meta:
        db_table = "action_parameters"
        constraints = [
            models.UniqueConstraint(fields=["parameter_gid", "p_key"])
        ]


class ScenarioParameterSerializer(ModelSerializer):
    class Meta:
        model = ScenarioParameter
        fields = '__all__'
