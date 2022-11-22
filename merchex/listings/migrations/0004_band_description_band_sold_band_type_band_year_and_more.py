# Generated by Django 4.1.3 on 2022-11-22 09:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_band_active_band_biography_band_genre_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='band',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='band',
            name='sold',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='band',
            name='type',
            field=models.CharField(choices=[('R', 'Records'), ('c', 'Clothing'), ('P', 'Poster'), ('M', 'Miscellaneous')], default=' ', max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='band',
            name='year',
            field=models.IntegerField(default=2000, validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2022)]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='band',
            name='year_formed',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2022)]),
        ),
    ]
