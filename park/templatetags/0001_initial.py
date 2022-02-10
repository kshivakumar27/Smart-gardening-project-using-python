# Generated by Django 3.0.5 on 2020-05-31 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Humidityupdate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Updated', models.DateTimeField(auto_now=True)),
                ('Humidity_status', models.IntegerField()),
                ('Humiditysensorstate', models.BooleanField(default=False)),
                ('Parklocation', models.CharField(max_length=100)),
                ('Review', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Firstname', models.CharField(max_length=100)),
                ('phonenumber', models.IntegerField()),
                ('EmailId', models.CharField(max_length=100)),
                ('Complaints', models.CharField(max_length=100000)),
            ],
        ),
        migrations.CreateModel(
            name='Sensorstatesupdate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Updated', models.DateTimeField(auto_now=True)),
                ('Temp_status', models.IntegerField()),
                ('Tempsensorstate', models.BooleanField(default=False)),
                ('Parklocation', models.CharField(max_length=100)),
                ('Review', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Streetlightings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Updated', models.DateTimeField(auto_now=True)),
                ('Lights_status', models.IntegerField()),
                ('Lightsensorstate', models.BooleanField(default=False)),
                ('Parklocation', models.CharField(max_length=100)),
                ('Review', models.TextField()),
            ],
        ),
    ]
