# Generated by Django 3.2.3 on 2021-06-04 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_alter_exercise_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='set1',
            field=models.CharField(default=0, max_length=2),
        ),
        migrations.AlterField(
            model_name='entry',
            name='set2',
            field=models.CharField(default=0, max_length=3),
        ),
        migrations.AlterField(
            model_name='entry',
            name='set3',
            field=models.CharField(default=0, max_length=3),
        ),
        migrations.AlterField(
            model_name='entry',
            name='set4',
            field=models.CharField(default=0, max_length=3),
        ),
        migrations.AlterField(
            model_name='entry',
            name='set5',
            field=models.CharField(default=0, max_length=3),
        ),
    ]
