from django.db import models

# Create your models here.

class Post(models.Model):
	Title = models.CharField(max_length=128)
	Body = models.TextField()
	Author = models.ForeignKey('auth.User', on_delete = models.CASCADE)

	def __str__(self):
		return self.title
