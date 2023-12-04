import logging

from rest_framework.exceptions import *
from rest_framework.generics import *

from sample_app.entity.action import *

logger = logging.getLogger("app")


class RUD(RetrieveUpdateDestroyAPIView):
    '''ActionのRead/Update/Delete
    '''
    lookup_field = Action._meta.pk.name
    serializer_class = ActionSerializer
    queryset = Action.objects.all()


class LC(ListCreateAPIView):
    '''ActionのList/Create
    '''
    lookup_field = Action._meta.pk.name
    serializer_class = ActionSerializer
    queryset = Action.objects.all()
