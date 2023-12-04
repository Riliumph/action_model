import logging

from rest_framework.exceptions import *
from rest_framework.generics import *

from sample_app.entity.action_link import *

logger = logging.getLogger("app")


class RUD(RetrieveUpdateDestroyAPIView):
    lookup_field = ActionLink._meta.pk.name
    queryset = ActionLink.objects.all()
    serializer_class = ActionLinkSerializer


class LC(ListCreateAPIView):
    lookup_field = ActionLink._meta.pk.name
    queryset = ActionLink.objects.all()
    serializer_class = ActionLinkSerializer
