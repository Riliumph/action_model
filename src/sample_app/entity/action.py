from django.db import models
from rest_framework.serializers import ModelSerializer

from base.entity import BaseEntity

TABLE_NAME = "actions"


class Action(BaseEntity):
    action_id = models.AutoField(primary_key=True)
    action_name = models.TextField(null=False)
    # 自身の中で自信を参照させるために遅延評価を導入
    # action_link.Model側でaction.Modelを参照しており、循環参照を避けるために遅延評価を導入
    unit_action = models.ManyToManyField("Action",
                                         through="ActionLink",
                                         related_name=TABLE_NAME)
    # parameters = models.ManyToManyField("ActionParameter",
    #                                     through="ActionsParamsRule",
    #                                     related_name="actions_params_rule")

    class Meta:
        db_table = TABLE_NAME


class ActionSerializer(ModelSerializer):
    class Meta:
        model = Action
        fields = '__all__'
