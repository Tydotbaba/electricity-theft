# Generated by Django 3.0.6 on 2020-07-01 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theft_app', '0002_auto_20200604_1202'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cur1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cur1', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Cur2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cur2', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.FloatField()),
            ],
        ),
    ]
