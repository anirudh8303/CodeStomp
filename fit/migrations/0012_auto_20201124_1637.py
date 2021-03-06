# Generated by Django 3.1.3 on 2020-11-24 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fit', '0011_auto_20201124_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pharmacy',
            name='phar_StoreImage',
            field=models.ImageField(default='', null=True, upload_to='fit/pharmacy'),
        ),
        migrations.AlterField(
            model_name='pharmacy',
            name='phar_address',
            field=models.CharField(default='', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='pharmacy',
            name='phar_email',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='pharmacy',
            name='phar_idProof',
            field=models.ImageField(default='', null=True, upload_to='fit/pharmacy'),
        ),
        migrations.AlterField(
            model_name='pharmacy',
            name='phar_name',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='pharmacy',
            name='phar_ownerName',
            field=models.CharField(default='', max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='pharmacy',
            name='phar_phone',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='pharmacy',
            name='phar_username',
            field=models.CharField(default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='pharmacy',
            name='pharmay_location',
            field=models.CharField(default='', max_length=100, null=True),
        ),
    ]
