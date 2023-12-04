from django.db import models
from rest_framework.serializers import ModelSerializer

from base.entity import BaseEntity
from sample_app.entity import scenario


class ScenarioDetail(BaseEntity):
    scenario_detail_id = models.AutoField(primary_key=True)
    scenario_id = models.ForeignKey(scenario.Scenario,
                                    db_column="scenario_id",
                                    on_delete=models.CASCADE)
    seq = models.IntegerField(null=False)
    p_key = models.TextField(null=False)
    p_value = models.TextField(null=False)

    class Meta:
        db_table = "scenario_details"
        constraints = [models.UniqueConstraint(fields=["scenario_id", "scenario_seq", "p_key", "p_value"],
                                               name="scenario_details_scenario_id_scenario_seq_p_key_p_value_key"
                                               )
                       ]


class scenarioDetailSerializer(ModelSerializer):
    class Meta:
        model = ScenarioDetail
        fields = '__all__'
