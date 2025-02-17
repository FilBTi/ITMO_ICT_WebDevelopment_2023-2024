# Generated by Django 4.2.6 on 2023-10-15 19:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("project_first_app", "0003_alter_driver_date_of_birth_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="car",
            name="drivers",
            field=models.ManyToManyField(
                through="project_first_app.Ownership", to="project_first_app.driver"
            ),
        ),
        migrations.AddField(
            model_name="driver",
            name="cars",
            field=models.ManyToManyField(
                through="project_first_app.Ownership", to="project_first_app.car"
            ),
        ),
    ]
