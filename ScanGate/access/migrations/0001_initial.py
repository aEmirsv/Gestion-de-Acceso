# Generated by Django 5.0.6 on 2024-05-24 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='S/N', max_length=50)),
                ('apellidos', models.CharField(default='S/N', max_length=50)),
                ('hora_entrada', models.DateTimeField(auto_now_add=True)),
                ('foto', models.BinaryField()),
            ],
        ),
    ]
