# Generated by Django 4.1.7 on 2023-03-29 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("job", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="job",
            name="job_type",
            field=models.CharField(
                choices=[("Full Time", "Full Time"), ("Part Time", "Part Time")],
                default="",
                max_length=15,
            ),
            preserve_default=False,
        ),
    ]
