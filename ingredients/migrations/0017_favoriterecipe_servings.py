# Generated by Django 4.0 on 2022-01-16 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingredients', '0016_favoriterecipe_cuisines'),
    ]

    operations = [
        migrations.AddField(
            model_name='favoriterecipe',
            name='servings',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
