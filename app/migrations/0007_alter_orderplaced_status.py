# Generated by Django 3.2.19 on 2023-05-30 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20230530_1031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderplaced',
            name='status',
            field=models.CharField(choices=[('Packed', 'Packed'), ('On the way', 'on the way'), ('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Deliverd', 'Deliverd'), ('Cancel', 'Cancel')], default='Pending', max_length=50),
        ),
    ]