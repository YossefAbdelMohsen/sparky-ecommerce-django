# Generated by Django 4.0.4 on 2022-05-29 19:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_customeruser_image1'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customeruser',
            old_name='image1',
            new_name='image',
        ),
    ]