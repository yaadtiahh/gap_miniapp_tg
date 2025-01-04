from django.db import models
# from ckeditor.fields import RichTextField


class Quest(models.Model):
    title = models.CharField(max_length=255)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
