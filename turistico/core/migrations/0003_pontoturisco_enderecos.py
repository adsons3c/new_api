# Generated by Django 3.0 on 2019-12-14 13:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('enderecos', '0001_initial'),
        ('core', '0002_remove_pontoturisco_enderecos'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontoturisco',
            name='enderecos',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='enderecos.Enderecos'),
            preserve_default=False,
        ),
    ]
