from rest_framework import serializers


from ebook.models import Ebook, Review


class ReviewSerializer(serializers.ModelSerializer):
    review_author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        #fields = '__all__'
        exclude = ('ebook',)  # this will remove ebook pk and prints rest


class EbookSerializer(serializers.ModelSerializer):
    # creating relation between ebook and review
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Ebook
        fields = '__all__'
