# Generated by Django 5.0.6 on 2024-06-24 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('re_mirada', '0008_pedido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='fecha',
            field=models.CharField(max_length=255),
        ),
    ]
