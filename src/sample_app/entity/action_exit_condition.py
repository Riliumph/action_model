from django.db import models
from rest_framework.serializers import ModelSerializer

from base.entity import BaseEntity
from sample_app.entity import action_link


class ActionExitCond(BaseEntity):
    exit_condition_id = models.AutoField(primary_key=True)
    action_link_id = models.ForeignKey(action_link.Model,
                                       db_column="action_link_id",
                                       on_delete=models.CASCADE)
    l_value = models.TextField(null=False)
    operator = models.TextField(null=False)
    r_value = models.TextField(null=False)

    class Meta:
        db_table = "action_exit_conditions"


class ActionExitCondSerializer(ModelSerializer):
    class Meta:
        model = ActionExitCond
        fields = '__all__'
