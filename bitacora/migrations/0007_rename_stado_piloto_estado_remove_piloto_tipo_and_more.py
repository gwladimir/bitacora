# Generated by Django 4.2 on 2023-04-12 16:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bitacora', '0006_tipo_alter_vuelo_piloto_piloto_tipo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='piloto',
            old_name='stado',
            new_name='estado',
        ),
        migrations.RemoveField(
            model_name='piloto',
            name='tipo',
        ),
        migrations.RemoveField(
            model_name='vuelo',
            name='creado_por',
        ),
        migrations.DeleteModel(
            name='Tipo',
        ),
    ]
