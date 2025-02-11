# Generated by Django 5.1.5 on 2025-01-28 04:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categoria', '0001_initial'),
        ('marca', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='produtos')),
                ('description', models.TextField(blank=True, null=True)),
                ('serie_number', models.CharField(blank=True, max_length=100, null=True)),
                ('cost_price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('selling_price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('quantity', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='brand_product', to='marca.brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='category_product', to='categoria.category')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
