# Generated by Django 4.2.4 on 2023-10-11 19:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_like_like_unique_quip_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='quip',
            name='parent_quip',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.quip'),
        ),
    ]
