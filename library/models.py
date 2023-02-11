from django.db import models
import uuid

# Create your models here.

class File(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    video_id = models.UUIDField(editable=False, null=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    type = models.CharField(max_length=128, null=True)
    title = models.CharField(max_length=128, null=True)
    url = models.URLField(null=True, blank=True)
    location = models.ForeignKey('Folder', null=True, blank=True,
                                 related_name="file_folderlocation", on_delete=models.CASCADE)
    category = models.ForeignKey(
        'Folder', null=True, blank=True, related_name="file_category", on_delete=models.CASCADE)
    workspace =  models.UUIDField(editable=False, null=True)
    modified_on = models.DateTimeField(auto_now=True, null=True)
    created_by = models.UUIDField(editable=False, null=True)
    modified_by = models.UUIDField(editable=False, null=True)
    file_size = models.FloatField(null=True)
    path = models.URLField(null=True)

    class Meta:

        indexes = [
            models.Index(fields=['title', ]),
            models.Index(fields=['created_on', ]),

        ]


class Folder(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    title = models.CharField(max_length=128, null=True)
    parent = models.ForeignKey('self', null=True, blank=True,
                               related_name="folder_parent", on_delete=models.CASCADE)
    category = models.ForeignKey(
        'self', null=True, blank=True, related_name="folder_category", on_delete=models.CASCADE)
    title_metadata = models.UUIDField(editable=False, null=True)
    modified_on = models.DateTimeField(auto_now=True, null=True)
    created_by = models.UUIDField(editable=False, null=True)
    modified_by = models.UUIDField(editable=False, null=True)
    folder_type = models.CharField(max_length=64, null=True, blank=True)
    path = models.URLField(null=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        indexes = [
            models.Index(fields=['title', ]),
            models.Index(fields=['created_on', ]),

        ]