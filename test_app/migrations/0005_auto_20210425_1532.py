# Generated by Django 3.1.7 on 2021-04-25 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0004_auto_20210425_1529'),
    ]

    operations = [
        migrations.AddField(
            model_name='blooddonar',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='blooddonar',
            name='facebook_link',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
