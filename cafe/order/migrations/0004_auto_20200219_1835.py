# Generated by Django 3.0.1 on 2020-02-19 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_auto_20200208_1906'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='Data_Time',
        ),
        migrations.RemoveField(
            model_name='order',
            name='Description',
        ),
        migrations.RemoveField(
            model_name='order',
            name='Second_Name',
        ),
        migrations.AddField(
            model_name='order',
            name='Choice',
            field=models.CharField(choices=[('1', '1 персона'), ('2', '2 персони'), ('3', '3 персони'), ('4', '4 персони'), ('5', '5 персон'), ('6', '6 персон')], default=1, max_length=10),
        ),
    ]