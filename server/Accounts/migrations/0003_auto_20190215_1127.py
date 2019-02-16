# Generated by Django 2.1.1 on 2019-02-15 08:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0002_auto_20190108_2019'),
        ('Accounts', '0002_auto_20190215_0935'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='avatar',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='images.Image'),
        ),
        migrations.AddField(
            model_name='account',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='surname',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
