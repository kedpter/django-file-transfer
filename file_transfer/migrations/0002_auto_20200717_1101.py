# Generated by Django 3.0.7 on 2020-07-17 03:01

from django.db import migrations, models
import file_transfer.models


class Migration(migrations.Migration):

    dependencies = [
        ('file_transfer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='document',
            field=models.FileField(storage=file_transfer.models.OverwriteStorage(), upload_to=''),
        ),
    ]
