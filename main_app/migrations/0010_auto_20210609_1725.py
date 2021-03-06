# Generated by Django 3.2.3 on 2021-06-09 17:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_auto_20210604_1613'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tracker',
            options={'ordering': ['date']},
        ),
        migrations.RemoveField(
            model_name='entry',
            name='goal_met',
        ),
        migrations.AlterField(
            model_name='entry',
            name='tracker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entries', to='main_app.tracker'),
        ),
    ]
