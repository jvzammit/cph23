# Generated by Django 4.2.5 on 2023-10-01 09:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("orders", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="customer",
            name="code",
            field=models.CharField(default="test", max_length=16, unique=True),
            preserve_default=False,
        ),
    ]