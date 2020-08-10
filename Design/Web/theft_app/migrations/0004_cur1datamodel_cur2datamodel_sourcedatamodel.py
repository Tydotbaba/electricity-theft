# Generated by Django 3.0.6 on 2020-07-18 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theft_app', '0003_cur1_cur2_source'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cur1DataModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cur1', models.FloatField()),
                ('datetime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cur2DataModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cur2', models.FloatField()),
                ('datetime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='SourceDataModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.FloatField()),
                ('datetime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
