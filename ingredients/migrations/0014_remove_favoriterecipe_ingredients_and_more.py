# Generated by Django 4.0 on 2022-01-16 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingredients', '0013_delete_displayrecipe_favoriterecipe_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favoriterecipe',
            name='ingredients',
        ),
        migrations.RemoveField(
            model_name='favoriterecipe',
            name='saturated_fat',
        ),
        migrations.AddField(
            model_name='favoriterecipe',
            name='missed_ingredient_count',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='favoriterecipe',
            name='missed_ingredients',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='favoriterecipe',
            name='used_ingredient_count',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='favoriterecipe',
            name='used_ingredients',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]