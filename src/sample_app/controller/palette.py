import logging

from rest_framework.exceptions import *
from rest_framework.generics import *

from sample_app.entity.palette import *

logger = logging.getLogger("app")


class RUD(RetrieveUpdateDestroyAPIView):
    '''パレットのRead/Update/Delete
    '''
    lookup_field = Palette._meta.pk.name
    serializer_class = PaletteSerializer
    queryset = Palette.objects.all()


class LC(ListCreateAPIView):
    '''パレットのList/Create
    '''
    lookup_field = Palette._meta.pk.name
    serializer_class = PaletteSerializer
    queryset = Palette.objects.all()
