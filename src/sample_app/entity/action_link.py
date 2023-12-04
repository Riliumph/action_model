from django.db import models
from rest_framework.serializers import ModelSerializer

from base.entity import BaseEntity
from sample_app.entity.action import Action


class ActionLink(BaseEntity):
    action_link_id = models.AutoField(primary_key=True)
    root_action_id = models.ForeignKey(Action,
                                       db_column="root_action_id",
                                       related_name="root_action",
                                       on_delete=models.CASCADE)
    seq = models.IntegerField(null=False)
    action_id = models.ForeignKey(Action,
                                  db_column="action_id",
                                  related_name="action",
                                  on_delete=models.CASCADE)

    class Meta:
        db_table = "action_links"
        constraints = [
            models.UniqueConstraint(fields=["root_action_id", "seq"],
                                    name="action_links_root_action_id_seq_key")
        ]


class ActionLinkSerializer(ModelSerializer):
    class Meta:
        model = ActionLink
        fields = '__all__'
