# Generated by Django 3.1.7 on 2021-04-25 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0002_blooddonar_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='blooddonar',
            name='profession',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
