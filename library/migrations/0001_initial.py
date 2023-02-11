# Generated by Django 4.1.5 on 2023-02-11 18:56

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('title', models.CharField(max_length=128, null=True)),
                ('title_metadata', models.UUIDField(editable=False, null=True)),
                ('modified_on', models.DateTimeField(auto_now=True, null=True)),
                ('created_by', models.UUIDField(editable=False, null=True)),
                ('modified_by', models.UUIDField(editable=False, null=True)),
                ('folder_type', models.CharField(blank=True, max_length=64, null=True)),
                ('path', models.URLField(null=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='folder_category', to='library.folder')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='folder_parent', to='library.folder')),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('video_id', models.UUIDField(editable=False, null=True)),
                ('file_type', models.CharField(max_length=128, null=True)),
                ('title', models.CharField(max_length=128, null=True)),
                ('url', models.URLField(blank=True, null=True)),
                ('workspace', models.UUIDField(editable=False, null=True)),
                ('file_size', models.FloatField(null=True)),
                ('path', models.URLField(null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_on', models.DateTimeField(auto_now=True, null=True)),
                ('created_by', models.UUIDField(editable=False, null=True)),
                ('modified_by', models.UUIDField(editable=False, null=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='file_category', to='library.folder')),
                ('location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='file_folderlocation', to='library.folder')),
            ],
        ),
        migrations.AddIndex(
            model_name='folder',
            index=models.Index(fields=['title'], name='library_fol_title_142d90_idx'),
        ),
        migrations.AddIndex(
            model_name='folder',
            index=models.Index(fields=['created_on'], name='library_fol_created_0ee51d_idx'),
        ),
        migrations.AddIndex(
            model_name='file',
            index=models.Index(fields=['title'], name='library_fil_title_ff7f76_idx'),
        ),
        migrations.AddIndex(
            model_name='file',
            index=models.Index(fields=['created_on'], name='library_fil_created_3fd2ce_idx'),
        ),
    ]