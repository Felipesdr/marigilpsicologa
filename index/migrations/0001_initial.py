# Generated by Django 5.1.2 on 2024-10-14 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Texto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('sub_titulo', models.CharField(max_length=100)),
                ('data_postagem', models.DateField(auto_now_add=True)),
                ('conteudo', models.TextField()),
                ('imagem', models.CharField(max_length=100)),
            ],
        ),
    ]
