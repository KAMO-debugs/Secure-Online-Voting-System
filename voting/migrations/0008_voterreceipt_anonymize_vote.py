from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0007_remove_vote_one_vote_per_voter_per_election_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        # 1. Create VoterReceipt — the identified "has this person
        #    voted in this category" record, separate from the
        #    anonymous ballot. Mirrors Vote's current
        #    (voter, election, src_category) uniqueness exactly.
        migrations.CreateModel(
            name='VoterReceipt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('src_category', models.CharField(choices=[('INSTITUTIONAL', 'Institutional SRC'), ('CAMPUS', 'Campus SRC')], max_length=20)),
                ('voted_at', models.DateTimeField(auto_now_add=True)),
                ('election', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='voter_receipts', to='voting.election')),
                ('voter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='voter_receipts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddConstraint(
            model_name='voterreceipt',
            constraint=models.UniqueConstraint(fields=('voter', 'election', 'src_category'), name='one_receipt_per_category_per_election'),
        ),

        # 2. Drop the constraint on Vote — it references 'voter',
        #    which is about to be removed.
        migrations.RemoveConstraint(
            model_name='vote',
            name='one_vote_per_category_per_election',
        ),

        # 3. Remove the identifying field from Vote. This is the
        #    anonymity fix itself.
        migrations.RemoveField(
            model_name='vote',
            name='voter',
        ),
    ]
