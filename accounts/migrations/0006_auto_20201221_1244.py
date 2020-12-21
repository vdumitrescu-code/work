# Generated by Django 3.1.4 on 2020-12-21 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_optimalsecurity'),
    ]

    operations = [
        migrations.CreateModel(
            name='SecurityBrowsers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('browser_name', models.TextField()),
                ('market_trust', models.FloatField()),
            ],
        ),
        migrations.DeleteModel(
            name='OptimalSecurity',
        ),
    ]
