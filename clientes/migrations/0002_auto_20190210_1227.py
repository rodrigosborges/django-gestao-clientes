# Generated by Django 2.1.5 on 2019-02-10 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='age_name',
            new_name='age',
        ),
        migrations.AlterField(
            model_name='cliente',
            name='salary',
            field=models.DecimalField(decimal_places=2, max_digits=9),
        ),
    ]