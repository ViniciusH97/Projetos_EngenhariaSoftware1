# Generated by Django 4.2.5 on 2023-09-25 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_rename_categoria_genero_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='livro',
            name='genero',
        ),
        migrations.AddField(
            model_name='livro',
            name='genero',
            field=models.ManyToManyField(to='app.genero'),
        ),
    ]
