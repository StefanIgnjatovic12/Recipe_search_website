# Generated by Django 4.0 on 2022-01-06 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingredients', '0011_alter_ingredients_foodgroup'),
    ]

    operations = [
        migrations.CreateModel(
            name='DisplayRecipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=500)),
                ('ingredients', models.TextField(max_length=500)),
                ('link', models.URLField()),
                ('img', models.URLField()),
                ('calories', models.TextField(max_length=500)),
                ('fat', models.TextField(max_length=500)),
                ('carbs', models.TextField(max_length=500)),
                ('protein', models.TextField(max_length=500)),
                ('cholesterol', models.TextField(max_length=500)),
                ('sodium', models.TextField(max_length=500)),
                ('saturated_fat', models.TextField(max_length=500)),
                ('sugar', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='FavoriteRecipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=500)),
                ('ingredients', models.TextField(max_length=500)),
                ('link', models.URLField()),
                ('img', models.URLField()),
                ('calories', models.TextField(max_length=500)),
                ('fat', models.TextField(max_length=500)),
                ('carbs', models.TextField(max_length=500)),
                ('protein', models.TextField(max_length=500)),
                ('cholesterol', models.TextField(max_length=500)),
                ('sodium', models.TextField(max_length=500)),
                ('saturated_fat', models.TextField(max_length=500)),
                ('sugar', models.TextField(max_length=500)),
            ],
        ),
    ]
