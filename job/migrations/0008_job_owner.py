# Generated by Django 5.1.6 on 2025-02-17 22:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("job", "0007_apply"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="job",
            name="owner",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="job_owner",
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
    ]
