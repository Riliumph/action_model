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
    # ActionとActionParameterはActionsParametersRuleで多対多を組むべきである。
    # ActionParameterはEAVが採用されていて外部キーを張れていない
    # Action -(action_id) - ActionsParamsRules -(parameter_gid)- ActionParameters
    # parameter_gidなんてのを定義せず、parameter_idを多対多で構築すれば問題なかった。
    # TODO: 要実験
    # ActionsParamsRulesは条件が書かれているので、
    # 条件 x パラメータ分のIDでテーブルは作れそう。
    # ただし、バカみたいな行数になるし、グループ化するのがレコードなのでは？？？？？
    # parameters = models.ManyToManyField("ActionParameter",
    #                                     through="ActionsParamsRule",
    #                                     related_name="actions_params_rule")

    class Meta:
        db_table = TABLE_NAME


class ActionSerializer(ModelSerializer):
    # UI一発でやりたい場合、serializerを入れたらいいけど、Listってどうやるんや？
    class Meta:
        model = Action
        fields = '__all__'
