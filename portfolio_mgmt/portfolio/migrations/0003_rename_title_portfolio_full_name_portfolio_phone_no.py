# Generated by Django 4.1.4 on 2023-01-02 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_category_portfolio_projects'),
    ]

    operations = [
        migrations.RenameField(
            model_name='portfolio',
            old_name='title',
            new_name='full_name',
        ),
        migrations.AddField(
            model_name='portfolio',
            name='phone_no',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
