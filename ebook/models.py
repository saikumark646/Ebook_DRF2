from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
# Create your models here.


class Ebook(models.Model):
		title = models.CharField(max_length=50)
		author = models.CharField(max_length=50)
		description = models.TextField(blank=True)
		published = models.DateField()

		def __str__(self):
				return self.title

class Review(models.Model):
		ebook = models.ForeignKey(
			Ebook, on_delete=models.CASCADE, related_name="reviews")
		review = models.TextField(blank=True, null=True)
		review_author = models.ForeignKey(
			User, on_delete=models.CASCADE, blank=True, null=True)
		rating = models.PositiveIntegerField(
			validators=[MinValueValidator(1), MaxValueValidator(5)])
		created = models.DateTimeField(auto_now_add=True)
		updated = models.DateTimeField(auto_now=True)

		def __str__(self):
				return f'review on {str(self.ebook)} '
