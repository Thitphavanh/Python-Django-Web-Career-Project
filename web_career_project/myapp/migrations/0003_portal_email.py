# Generated by Django 4.1.4 on 2023-04-28 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0002_portal"),
    ]

    operations = [
        migrations.AddField(
            model_name="portal",
            name="email",
            field=models.TextField(blank=True, null=True),
        ),
    ]
