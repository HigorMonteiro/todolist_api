# Generated by Django 3.0 on 2020-02-01 18:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='assignment',
            name='project_by',
            field=models.ForeignKey(default=6, on_delete=django.db.models.deletion.CASCADE, to='todolist.Project'),
            preserve_default=False,
        ),
    ]
