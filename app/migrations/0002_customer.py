# Generated by Django 3.2.16 on 2023-02-14 10:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('locality', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=50)),
                ('mobile', models.IntegerField(default=0)),
                ('zipcode', models.IntegerField()),
                ('state', models.CharField(choices=[('Andaman & Nicobar', 'Andaman & Nicobar'), ('Andrapradesh', 'Andrapradesh'), ('Karanataka', 'Karanataka'), ('Tamil Nadu', 'Tamil Nadu'), ('Kerala', 'Kerala'), ('Bihar', 'Bihar'), ('Telangana', 'Telangana'), ('Punjab', 'Punjab'), ('Maharastra', 'Maharastra'), ('Delhi', 'Delhi'), ('Gujrat', 'Gujat'), ('Harayana', 'Harayana'), ('Goa', 'Goa'), ('Assam', 'Assam'), ('Jammu & Kashmir', 'Jammu & Kashmir ')], max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]