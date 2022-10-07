from rest_framework.pagination import PageNumberPagination


__all__ = ('DefaultPageNumberPagination', )


class DefaultPageNumberPagination(PageNumberPagination):
    page_size = 10