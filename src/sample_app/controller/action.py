import logging

from rest_framework.exceptions import *
from rest_framework.generics import *

from sample_app.entity.action import *

logger = logging.getLogger("app")


class LC(ListCreateAPIView):
    '''ActionのList/Create
    単体のデータを作成するAPI
    '''
    lookup_field = Action._meta.pk.name
    serializer_class = ActionSerializer
    queryset = Action.objects.all()


class RUD(RetrieveUpdateDestroyAPIView):
    '''ActionのRead/Update/Delete
    単体のデータを処理するAPI
    '''
    lookup_field = Action._meta.pk.name
    serializer_class = ActionSerializer
    queryset = Action.objects.all()
