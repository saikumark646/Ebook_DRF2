from django.shortcuts import get_object_or_404
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework import permissions
from rest_framework.exceptions import ValidationError
from ebook.models import Ebook, Review
from ebook.api.serializers import ReviewSerializer, EbookSerializer
from ebook.api.permissions import IsAuthenticatedOrAdminOrReadOnly, IsReviewAuthorOrReadonly
from ebook.api.pagination import SmallSetPagination


# these classes are called as concrete view classes, they take queryset and serializer_class as a default parameters .

class EbookListCreteView(ListCreateAPIView):
    queryset = Ebook.objects.all().order_by('id')   # if '-id' last edited one will show first
    serializer_class = EbookSerializer
    permission_classes = [IsAuthenticatedOrAdminOrReadOnly]
    pagination_class = SmallSetPagination

class EbookListDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer
    permission_classes = [IsAuthenticatedOrAdminOrReadOnly]


class ReviewCreateApiView(CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        ebook_pk = self.kwargs.get('ebook_pk')
        ebook = get_object_or_404(Ebook, pk=ebook_pk)

        review_author = self.request.user  #assigning user to the review_author

        review_queryset = Review.objects.filter(
            ebook=ebook,
            review_author=review_author)
        if review_queryset.exists():
            raise ValidationError('you have already reviewed on this ebook')

        serializer.save(ebook=ebook, review_author=review_author)



class ReviewDetailApiView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsReviewAuthorOrReadonly]



# class EbookListCreteView(ListModelMixin,
#                          CreateModelMixin,
#                          GenericAPIView):

#     queryset = Ebook.objects.all()
#     serializer_class = EbookSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
