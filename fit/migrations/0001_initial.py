# Generated by Django 3.1.3 on 2020-11-23 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('pat_id', models.AutoField(primary_key=True, serialize=False)),
                ('pat_name', models.CharField(default='', max_length=100)),
                ('pat_phone', models.IntegerField()),
                ('pat_loc', models.CharField(default='', max_length=100)),
                ('pat_username', models.CharField(default='', max_length=10)),
                ('pat_address', models.CharField(default='', max_length=500)),
            ],
        ),
    ]