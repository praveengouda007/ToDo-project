# Generated by Django 3.2.9 on 2021-11-15 06:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ToDoApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ToDoTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Task', models.CharField(max_length=20)),
                ('created_by', models.CharField(max_length=20)),
            ],
        ),
        migrations.RenameField(
            model_name='taskstatus',
            old_name='statusoftask',
            new_name='status',
        ),
        migrations.RemoveField(
            model_name='taskstatus',
            name='tasks',
        ),
        migrations.DeleteModel(
            name='ToDoTasks',
        ),
        migrations.AddField(
            model_name='todotask',
            name='Status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ToDoApp.taskstatus'),
        ),
    ]
