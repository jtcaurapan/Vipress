# Generated by Django 2.2.7 on 2019-11-17 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('persona', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seminario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('duracion', models.DurationField()),
                ('Cantidad_participantes', models.IntegerField()),
                ('fecha', models.DateField()),
                ('direccion', models.TextField()),
                ('orador', models.ManyToManyField(to='persona.Orador')),
            ],
        ),
    ]