from django.db import models


# Create your models here.
class Media(models.Model):
    media_id = models.AutoField(primary_key=True)
    file_name = models.CharField(max_length=255)
    file_type = models.ForeignKey('Media_Type', on_delete=models.CASCADE)
    mime_type = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.file_name


class Media_Type(models.Model):
    media_type_id = models.AutoField(primary_key=True)
    media_type = models.CharField(max_length=255)

    def __str__(self):
        return self.media_type
