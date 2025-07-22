from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="اسم القسم")

    class Meta:
        verbose_name = "قسم"
        verbose_name_plural = "الأقسام"

    def __str__(self):
        return self.name
