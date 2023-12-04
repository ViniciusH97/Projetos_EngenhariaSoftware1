# Generated by Django 4.2.7 on 2023-11-27 23:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_continentes_paises'),
    ]

    operations = [
        migrations.CreateModel(
            name='Continente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=40)),
                ('paises', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.pais')),
            ],
        ),
        migrations.DeleteModel(
            name='Continentes',
        ),
    ]
