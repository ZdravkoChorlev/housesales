# Generated by Django 3.1.3 on 2020-11-29 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('apartment', 'Apartment'), ('mansion', 'Mansion'), ('villa', 'Villa'), ('small house', 'Small House'), ('unknown', 'Unknown')], default='unknown', max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('size', models.IntegerField()),
                ('description', models.TextField()),
                ('owner_name', models.CharField(max_length=40)),
                ('image', models.ImageField(upload_to='houses')),
            ],
        ),
    ]
