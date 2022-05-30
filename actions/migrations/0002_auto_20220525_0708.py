# Generated by Django 3.1.7 on 2022-05-25 07:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('comments', '0001_initial'),
        ('management', '0001_initial'),
        ('mediamanager', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('entity', '0001_initial'),
        ('actions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='action',
            name='action_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='actions_action_action_category', to='management.dropdown'),
        ),
        migrations.AddField(
            model_name='action',
            name='comments',
            field=models.ManyToManyField(blank=True, to='comments.Comment'),
        ),
        migrations.AddField(
            model_name='action',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='actions_action_created', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='action',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='actions_action_department', to='management.department'),
        ),
        migrations.AddField(
            model_name='action',
            name='entity',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='actions_action_entity', to='entity.entity'),
        ),
        migrations.AddField(
            model_name='action',
            name='media',
            field=models.ManyToManyField(blank=True, related_name='actions_action_media_attachment', to='mediamanager.MediaAttachment'),
        ),
        migrations.AddField(
            model_name='action',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='actions_action_owner', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='action',
            name='source',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='actions_action_source', to='management.source'),
        ),
        migrations.AddField(
            model_name='action',
            name='status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='actions_action_status', to='management.dropdown'),
        ),
        migrations.AddField(
            model_name='action',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='actions_action_updated', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='action',
            name='updates',
            field=models.ManyToManyField(blank=True, to='comments.ActionUpdate'),
        ),
    ]
