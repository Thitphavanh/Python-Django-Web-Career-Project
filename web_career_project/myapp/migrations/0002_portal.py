# Generated by Django 4.0 on 2023-03-27 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('detail', models.TextField()),
                ('file', models.FileField(upload_to='files/')),
                ('tag', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
