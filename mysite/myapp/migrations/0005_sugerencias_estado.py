# Generated by Django 5.1.1 on 2024-11-16 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='sugerencias',
            name='estado',
            field=models.CharField(choices=[('Pendiente', 'Pendiente'), ('Revisada', 'Revisada'), ('Implementada', 'Implementada')], default='Pendiente', max_length=20),
        ),
    ]
