from django.db import models
from rest_framework.serializers import ModelSerializer

from base.entity import BaseEntity
from sample_app.entity import action


class ActionsParamsRule(BaseEntity):
    id = models.AutoField(primary_key=True)
    action_id = models.ForeignKey(action.Model,
                                  db_column="action_id",
                                  on_delete=models.CASCADE)
    weather = models.TextField(null=False)
    parameter_gid = models.IntegerField(null=False)

    class Meta:
        db_table = "action_parameters"
        constraints = [
            models.UniqueConstraint(fields=["parameter_gid", "p_key"])
        ]


class ActionsParamsRuleSerializer(ModelSerializer):
    class Meta:
        model = ActionsParamsRule
        fields = '__all__'
