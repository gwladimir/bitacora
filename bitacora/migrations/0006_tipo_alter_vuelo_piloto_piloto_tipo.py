# Generated by Django 4.2 on 2023-04-11 22:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bitacora', '0005_piloto_vuelo_remove_usuario_type_delete_tipo_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=150, verbose_name='Tipo Usuario')),
            ],
            options={
                'verbose_name': 'Tipo',
                'verbose_name_plural': 'Tipos',
                'db_table': 'Tipos',
                'ordering': ['id'],
            },
        ),
        migrations.AlterField(
            model_name='vuelo',
            name='piloto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Vuelos', to='bitacora.piloto'),
        ),
        migrations.AddField(
            model_name='piloto',
            name='tipo',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='Tipos', to='bitacora.tipo'),
            preserve_default=False,
        ),
    ]
