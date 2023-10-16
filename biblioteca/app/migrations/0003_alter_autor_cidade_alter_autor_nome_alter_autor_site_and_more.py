# Generated by Django 4.2.5 on 2023-09-05 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_livro_preco'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autor',
            name='cidade',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='autor',
            name='nome',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='autor',
            name='site',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='nome',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='cidade',
            name='nome',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='editora',
            name='cidade',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='editora',
            name='nome',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='editora',
            name='site',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='emprestimo',
            name='nome',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='leitor',
            name='cpf',
            field=models.CharField(max_length=11),
        ),
        migrations.AlterField(
            model_name='leitor',
            name='email',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='leitor',
            name='nome',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='livro',
            name='nome',
            field=models.CharField(max_length=50),
        ),
    ]