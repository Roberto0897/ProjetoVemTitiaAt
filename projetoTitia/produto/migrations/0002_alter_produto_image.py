# Generated by Django 5.1.5 on 2025-02-02 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='image',
            field=models.ImageField(upload_to='produtos/'),
        ),
    ]
