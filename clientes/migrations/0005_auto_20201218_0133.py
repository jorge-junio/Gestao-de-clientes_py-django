# Generated by Django 3.1.4 on 2020-12-18 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0004_vendas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendas',
            name='num_venda',
            field=models.CharField(max_length=7),
        ),
    ]
