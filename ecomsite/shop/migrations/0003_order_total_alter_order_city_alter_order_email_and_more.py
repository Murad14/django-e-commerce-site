# Generated by Django 4.2.2 on 2023-06-26 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total',
            field=models.CharField(default='1', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='city',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='order',
            name='email',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='order',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='order',
            name='state',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='order',
            name='zipcode',
            field=models.CharField(max_length=200),
        ),
    ]