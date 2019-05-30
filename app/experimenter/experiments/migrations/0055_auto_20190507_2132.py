# Generated by Django 2.1.7 on 2019-05-07 21:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("experiments", "0054_experiment_risk_revision"),
    ]

    operations = [
        migrations.AddField(
            model_name="experiment",
            name="subscribers",
            field=models.ManyToManyField(
                blank=True,
                related_name="subscribed_experiments",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="experiment",
            name="owner",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="owned_experiments",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]