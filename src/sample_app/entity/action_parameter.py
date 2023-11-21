from django.db import models
from rest_framework.serializers import ModelSerializer

from base.entity import BaseEntity

TABLE_NAME = "action_parameters"


class ActionParameter(BaseEntity):
    parameter_id = models.AutoField(primary_key=True)
    parameter_gid = models.IntegerField(null=False)
    p_key = models.TextField(null=False)
    p_value = models.TextField(null=False)

    class Meta:
        db_table = TABLE_NAME
        constraints = [
            models.UniqueConstraint(fields=["parameter_gid", "p_key"])
        ]


class ActionParameterSerializer(ModelSerializer):
    class Meta:
        model = ActionParameter
        fields = '__all__'
