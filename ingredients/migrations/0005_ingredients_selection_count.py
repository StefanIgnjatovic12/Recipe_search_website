# Generated by Django 4.0 on 2022-01-02 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingredients', '0004_ingredients_selection'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredients',
            name='selection_count',
            field=models.BigIntegerField(default='0'),
        ),
    ]
