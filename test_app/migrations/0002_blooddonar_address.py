# Generated by Django 3.1.7 on 2021-04-22 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blooddonar',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
    ]
