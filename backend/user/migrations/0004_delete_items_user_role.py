# Generated by Django 4.2.7 on 2023-11-03 07:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0003_items"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Items",
        ),
        migrations.AddField(
            model_name="user",
            name="role",
            field=models.CharField(
                choices=[("S", "seller"), ("M", "manager")],
                default="seller",
                max_length=10,
                verbose_name="역할",
            ),
        ),
    ]
