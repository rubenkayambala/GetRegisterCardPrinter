# Generated by Django 4.2.7 on 2024-10-01 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_carte_filiere'),
    ]

    operations = [
        migrations.AddField(
            model_name='carte',
            name='qr_code',
            field=models.ImageField(blank=True, upload_to='qr_code'),
        ),
    ]
