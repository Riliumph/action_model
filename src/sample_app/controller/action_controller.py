import logging

from rest_framework.exceptions import *
from rest_framework.generics import *

from sample_app.entity.action import *

logger = logging.getLogger("app")


class RUD(RetrieveUpdateDestroyAPIView):
    serializer_class = ActionSerializer
    lookup_field = Action._meta.pk.name

    def get_queryset(self):
        return Action.objects.all().order_by(self.lookup_field)


class LC(ListCreateAPIView):
    serializer_class = ActionSerializer
    lookup_field = Action._meta.pk.name

    def get_queryset(self):
        return Action.objects.all().order_by(self.lookup_field)


class RUD(RetrieveUpdateDestroyAPIView):
    serializer_class = ActionSerializer
    lookup_field = Action._meta.pk.name

    def get_queryset(self):
        return Action.objects.all().order_by(self.lookup_field)
