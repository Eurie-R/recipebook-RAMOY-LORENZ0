# Generated by Django 5.1.6 on 2025-03-07 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ledger', '0002_alter_recipe_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='recipeingredient',
            name='Quantity',
            field=models.CharField(max_length=50),
        ),
    ]
