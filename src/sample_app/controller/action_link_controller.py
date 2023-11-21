import logging

from rest_framework.exceptions import *
from rest_framework.generics import *

from sample_app.entity.action_link import *

logger = logging.getLogger("app")


class RUD(RetrieveUpdateDestroyAPIView):
    serializer_class = ActionLinkSerializer
    lookup_field = ActionLink._meta.pk.name

    def get_queryset(self):
        return ActionLink.objects.all().order_by(self.lookup_field)


class LC(ListCreateAPIView):
    serializer_class = ActionLinkSerializer
    lookup_field = ActionLink._meta.pk.name

    def get_queryset(self):
        return ActionLink.objects.all().order_by(self.lookup_field)
