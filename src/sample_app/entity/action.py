from django.db import models
from rest_framework.serializers import ModelSerializer

from base.entity import BaseEntity
from sample_app.entity.action_link import ActionLink

TABLE_NAME = "actions"


class Action(BaseEntity):
    action_id = models.AutoField(primary_key=True)
    action_name = models.TextField(null=False)
    unit_action_id = models.ManyToManyField("Action",
                                            through=ActionLink, related_name="actions")

    class Meta:
        db_table = TABLE_NAME


class ActionSerializer(ModelSerializer):
    class Meta:
        model = Action
        fields = '__all__'
