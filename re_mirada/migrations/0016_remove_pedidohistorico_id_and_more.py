# Generated by Django 5.0.6 on 2024-06-29 18:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('re_mirada', '0015_pedidohistorico'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedidohistorico',
            name='id',
        ),
        migrations.RemoveField(
            model_name='pedidohistorico',
            name='pedido',
        ),
        migrations.AddField(
            model_name='pedidohistorico',
            name='id_pedido',
            field=models.UUIDField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pedidohistorico',
            name='usuario',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='re_mirada.usuario'),
            preserve_default=False,
        ),
    ]
