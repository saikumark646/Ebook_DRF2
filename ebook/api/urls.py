from django.urls import path
from ebook.api.views import EbookListCreteView, EbookListDetailView
from ebook.api.views import ReviewDetailApiView, ReviewCreateApiView

urlpatterns = [
     path('ebook/', EbookListCreteView.as_view(), name='EbookListCreteView'),
     path('ebook/<int:pk>/', EbookListDetailView.as_view(),
          name='EbookListDetailView'),

     path('ebook/<int:ebook_pk>/review/', ReviewCreateApiView.as_view(),
          name='ReviewCreateApiView'),
     path('review/<int:pk>/', ReviewDetailApiView.as_view(),
          name='ReviewDetailApiView')
]
