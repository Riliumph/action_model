from django.db import models
from rest_framework.serializers import ModelSerializer

from base.entity import BaseEntity
from sample_app.entity import scenario_detail


class ScenarioExecCond(BaseEntity):
    exec_condition_id = models.AutoField(primary_key=True)
    scenario_detail_id = models.ForeignKey(scenario_detail.ScenarioDetail,
                                           db_column="scenario_detail_id",
                                           on_delete=models.CASCADE)
    l_value = models.TextField(null=False)
    operator = models.TextField(null=False)
    r_value = models.TextField(null=False)

    class Meta:
        db_table = "scenario_exec_conditions"


class ScenarioExecCondSerializer(ModelSerializer):
    class Meta:
        model = ScenarioExecCond
        fields = '__all__'
