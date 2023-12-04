import logging

from rest_framework.exceptions import *
from rest_framework.generics import *

from sample_app.entity.map import *

logger = logging.getLogger("app")


class RUD(RetrieveUpdateDestroyAPIView):
    '''パレットのRead/Update/Delete
    '''
    lookup_field = GlobalMap._meta.pk.name
    serializer_class = MapSerializer
    queryset = GlobalMap.objects.all()


class LC(ListCreateAPIView):
    '''パレットのList/Create
    '''
    lookup_field = GlobalMap._meta.pk.name
    serializer_class = MapSerializer
    queryset = GlobalMap.objects.all()
