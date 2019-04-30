# Generated by Django 2.2 on 2019-04-26 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kadhia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=100)),
                ('Description', models.TextField(blank=True, max_length=100, null=True)),
                ('Price', models.DecimalField(decimal_places=2, max_digits=1000)),
                ('StartingPlace', models.TextField(max_length=100)),
                ('Destination', models.TextField(max_length=100)),
                ('Recommended', models.BooleanField(default=True, null=True)),
            ],
        ),
    ]
