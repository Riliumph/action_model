import logging

from rest_framework.exceptions import *
from rest_framework.generics import *

from sample_app.entity.palette import *

logger = logging.getLogger("app")


class RUD(RetrieveUpdateDestroyAPIView):
    '''パレットのRead/Update/Delete
    パレットの情報と多対多を組んでいるグリッドを同時に取得する
    '''
    lookup_field = Palette._meta.pk.name
    queryset = Palette.objects.all()
    serializer_class = PaletteSerializer


class LC(ListCreateAPIView):
    '''パレットのList/Create
    パレットの情報と多対多を組んでいるグリッドを同時に取得する
    '''
    lookup_field = Palette._meta.pk.name
    queryset = Palette.objects.all()
    serializer_class = PaletteSerializer
