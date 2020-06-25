# Generated by Django 3.0.6 on 2020-06-04 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TheftData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('current1', models.FloatField()),
                ('current2', models.FloatField()),
                ('total', models.FloatField()),
                ('source', models.FloatField()),
                ('difference', models.FloatField()),
            ],
        ),
    ]
