# Generated by Django 4.0 on 2021-12-31 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ingredients', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Ingredient',
            new_name='Ingredients',
        ),
    ]
