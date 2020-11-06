# Generated by Django 3.1.2 on 2020-10-15 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djconnectwise', '0132_activityudf_opportunityudf_projectudf_ticketudf'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityUDFTracker',
            fields=[
            ],
            options={
                'db_table': 'djconnectwise_activityudf',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('djconnectwise.activityudf',),
        ),
        migrations.CreateModel(
            name='OpportunityUDFTracker',
            fields=[
            ],
            options={
                'db_table': 'djconnectwise_opportunityudf',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('djconnectwise.opportunityudf',),
        ),
        migrations.CreateModel(
            name='ProjectUDFTracker',
            fields=[
            ],
            options={
                'db_table': 'djconnectwise_projectudf',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('djconnectwise.projectudf',),
        ),
        migrations.CreateModel(
            name='TicketUDFTracker',
            fields=[
            ],
            options={
                'db_table': 'djconnectwise_ticketudf',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('djconnectwise.ticketudf',),
        ),
    ]