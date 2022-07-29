from rest_framework.pagination import PageNumberPagination


class SmallSetPagination(PageNumberPagination):
    page_size = 2    # this will give 2 ebook models per page
    
    
    """
    On "GenericAPIView" subclasses you may also set the pagination_class attribute to select PageNumberPagination on a per-view basis.
    
    """