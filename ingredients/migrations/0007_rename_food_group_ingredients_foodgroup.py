# Generated by Django 4.0 on 2022-01-04 16:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ingredients', '0006_foodgroups_remove_ingredients_group_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ingredients',
            old_name='food_group',
            new_name='foodgroup',
        ),
    ]
