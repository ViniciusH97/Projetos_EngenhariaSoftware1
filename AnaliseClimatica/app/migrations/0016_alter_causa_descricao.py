# Generated by Django 5.0 on 2023-12-04 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_remove_causa_estado_causa_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='causa',
            name='descricao',
            field=models.CharField(max_length=500),
        ),
    ]
