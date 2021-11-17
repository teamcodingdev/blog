from django.db import models

class Tag(models.Model):
    tag = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.tag

    def save(self, *args, **kwargs):
        self.tag = self.tag.lower()
        super().save(*args, **kwargs)