# Generated by Django 4.2.7 on 2023-11-14 01:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_continentes_paises'),
    ]

    operations = [
        migrations.AlterField(
            model_name='continentes',
            name='paises',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.pais'),
            preserve_default=False,
        ),
    ]
