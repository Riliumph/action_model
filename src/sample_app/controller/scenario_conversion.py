import logging

from rest_framework.exceptions import *
from rest_framework.generics import *

from sample_app.entity.action import *

logger = logging.getLogger("app")


class LC(ListCreateAPIView):
    '''シナリオ変換
    シナリオ変換のためのUIとしてActionのList
    Actionのjsonを投入するPostを実装する。
    一気に多対多の先や外部キーが張られていないテーブルまで作成するためserializerでのUI構築は不可能である。
    jsonのみをサポートする。
    '''
    lookup_field = Action._meta.pk.name
    serializer_class = ActionSerializer
    queryset = Action.objects.all()

    def create(self, request, *args, **kwargs):
        try:
            request
            return super().create(request, *args, **kwargs)

        except Exception as e:
            logger.error(f"{e}")
            raise APIException()


class RUD(RetrieveUpdateDestroyAPIView):
    '''シナリオ変換用ののRead/Update/Delete
    '''
    lookup_field = Action._meta.pk.name
    serializer_class = ActionSerializer
    queryset = Action.objects.all()
