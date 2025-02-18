# Generated by Django 5.1.6 on 2025-02-15 22:33

import job.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("job", "0005_job_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="job",
            name="slug",
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="job",
            name="image",
            field=models.ImageField(upload_to=job.models.image_upload),
        ),
    ]
