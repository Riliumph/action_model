from django.db import models
from rest_framework.serializers import ModelSerializer

from base.entity import BaseEntity
from sample_app.entity import scenario_detail


class Scenario(BaseEntity):
    scenario_id = models.AutoField(primary_key=True)
    scenario_name = models.TextField(null=False)

    class Meta:
        db_table = "scenarios"


class ScenarioSerializer(ModelSerializer):
    scenario_detail

    class Meta:
        model = Scenario
        fields = '__all__'
