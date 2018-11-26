
from django.utils import timezone
from django.db import models
from ckeditor.fields import RichTextField


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    #text = RichTextField()
    text = models.TextField()
    des = models.TextField()
    photo = models.CharField(max_length=255, default='#')
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


