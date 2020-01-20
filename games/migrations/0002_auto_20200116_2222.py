# Generated by Django 2.2.9 on 2020-01-16 13:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('games', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='challenge',
            name='attacker',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='attacker', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='challenge',
            name='attacker_choice',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pc_choice', to='games.Weapon'),
        ),
        migrations.AddField(
            model_name='challenge',
            name='defender',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='defender', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='challenge',
            name='defender_choice',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='human_choice', to='games.Weapon'),
        ),
        migrations.AddField(
            model_name='challenge',
            name='winner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='winner', to=settings.AUTH_USER_MODEL),
        ),
    ]