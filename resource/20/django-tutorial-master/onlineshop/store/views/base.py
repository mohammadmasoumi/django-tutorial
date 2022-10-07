from rest_framework import mixins 
from rest_framework.viewsets import GenericViewSet


class CreateRetrieveDestroy(mixins.RetrieveModelMixin,
                           mixins.DestroyModelMixin,
                           mixins.CreateModelMixin,
                           GenericViewSet):
    """
    A viewset that provides default `list()` and `retrieve()` actions.
    """
    pass