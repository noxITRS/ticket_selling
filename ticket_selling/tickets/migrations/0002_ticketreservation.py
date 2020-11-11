# Generated by Django 3.1.3 on 2020-11-10 21:07

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
        ('tickets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TicketReservation',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('ticket_type', models.CharField(max_length=20)),
                ('status', models.CharField(choices=[('R', 'Reserved'), ('P', 'Paid'), ('E', 'Expired')], default='R', max_length=1)),
                ('reserved_time', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('event', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='events.event')),
            ],
        ),
    ]