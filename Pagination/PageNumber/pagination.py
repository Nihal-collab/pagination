from rest_framework.pagination import PageNumberPagination

class Movie_Page(PageNumberPagination):
    page_size=5
    ordering="-id"