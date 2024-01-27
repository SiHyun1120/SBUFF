from django.db import models


class RecommendModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=100)


    def __str__(self):
        return self.model_name