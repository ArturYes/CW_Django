# Generated by Django 5.0.4 on 2024-05-31 03:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clients', '0001_initial'),
        ('messages_', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Logs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_last_mailing', models.DateTimeField(verbose_name='Дата последней попытки')),
                ('status_mailing', models.CharField(choices=[('Успешно', 'Успешно'), ('Безуспешно', 'Безуспешно'), ('Частично успешно', 'Частично успешно')], verbose_name='Статус рассылки')),
                ('response_mail_server', models.TextField(blank=True, null=True, verbose_name='Ответ почтового сервера')),
            ],
            options={
                'verbose_name': 'Попытка рассылки',
                'verbose_name_plural': 'Попытки рассылки',
                'db_table': '_ns_logs',
                'db_table_comment': 'Попытки рассылки',
                'ordering': ['newsletter', 'date_last_mailing'],
            },
        ),
        migrations.CreateModel(
            name='Newsletters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_newsletter', models.CharField(max_length=100, verbose_name='Название рассылки')),
                ('date_first_mailing', models.DateTimeField(verbose_name='Дата и время первой рассылки')),
                ('frequency_mailing', models.CharField(choices=[('D', 'Ежедневно'), ('W', 'Еженедельно'), ('M', 'Ежемесячно'), ('Y', 'Ежегодно')], default='D', max_length=1, verbose_name='Периодичность рассылки')),
                ('date_next_mailing', models.DateTimeField(blank=True, null=True, verbose_name='Дата и время следующей рассылки')),
                ('state_mailing', models.CharField(choices=[('C', 'Создана'), ('L', 'Запущена'), ('F', 'Завершена')], default='C', max_length=1, verbose_name='Состояние рассылки')),
                ('is_active', models.BooleanField(default=True, verbose_name='Статус рассылки')),
                ('clients', models.ManyToManyField(related_name='clients', to='clients.clients')),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='messages_.messages', verbose_name='Сообщение')),
            ],
            options={
                'verbose_name': 'Рассылка',
                'verbose_name_plural': 'Рассылки',
                'db_table': '_ns_newsletters',
                'db_table_comment': 'Рассылки',
                'ordering': ['date_first_mailing', 'name_newsletter'],
                'permissions': [('set_newsletters_deactivate', 'Can deacticate Рассылка'), ('view_all_newsletters', 'Can view all Рассылка')],
            },
        ),
    ]