import logging

from rest_framework.exceptions import *
from rest_framework.generics import *

from sample_app.entity.map import *

logger = logging.getLogger("app")


class RUD(RetrieveUpdateDestroyAPIView):
    '''マップのRead/Update/Delete
    マップに存在するパレットも同時に取得
    '''
    lookup_field = GlobalMap._meta.pk.name
    queryset = GlobalMap.objects.all()
    serializer_class = MapSerializer


class LC(ListCreateAPIView):
    '''パレットのList/Create
    マップに存在するパレットも同時に取得
    '''
    lookup_field = GlobalMap._meta.pk.name
    queryset = GlobalMap.objects.all()
    serializer_class = MapSerializer
