from django.db import models

# Create your models here.
class Region(models.Model):
    region_name = models.CharField(max_length=200, null=True)
    region_id = models.CharField(max_length=20, null=True, unique=True)

    def __str__(self):
        return self.region_name

class Candidate(models.Model):
    candidate_id = models.CharField(max_length=10, blank=True, unique=True)
    region = models.ForeignKey(Region, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=200, null=True)
    party_name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class Admin(models.Model):
    name = models.CharField(max_length=200, null=True)
    admin_id = models.CharField(max_length=10, null=True, unique=True)
    region = models.OneToOneField(Region, null=True, on_delete = models.DO_NOTHING)
    password = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name

class Voter(models.Model):
    CATEGORY = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )
    admin = models.ForeignKey(Admin, blank = True, on_delete = models.CASCADE, default=None)
    name = models.CharField(max_length=200, null=True)
    father_name = models.CharField(max_length=200, null=True)
    aadhar_no = models.CharField(max_length=20, null=True, unique=True)
    gender = models.CharField(max_length=200, null=True, choices=CATEGORY)
    voter_id = models.CharField(max_length=10, blank=True, unique=True)
    date_of_birth = models.DateField(null=True)
    age = models.PositiveIntegerField(blank=True)
    region = models.ForeignKey(Region, null=True, on_delete=models.SET_NULL)
    vote = models.CharField(max_length=200, blank=True)
    election = models.CharField(max_length=200, blank=True)
    password = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name


class Election(models.Model):
    election_id = models.CharField(max_length=200, blank=True)
    admin = models.ForeignKey(Admin, null=True, on_delete=models.SET_NULL)
    region_name = models.ForeignKey(Region, null=True, on_delete=models.SET_NULL)
    region_id = models.CharField(max_length=200, null=True)
    date_created = models.DateField(null=True)
    start_time = models.TimeField(null=True)
    end_time = models.TimeField(null=True)
    candidates = models.ManyToManyField(Candidate)
    winner = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.election_id

class History(models.Model) : 
    election_id = models.CharField(max_length = 200, blank = True)
    date_created = models.DateField(blank=True)
    region_id = models.CharField(max_length = 200, blank = True)
    winner_id = models.CharField(max_length = 200, blank = True)
    winner_name = models.CharField(max_length = 200, blank = True)
    winner_party = models.CharField(max_length = 200, blank = True)
    votes = models.CharField(max_length = 200, blank = True)

    def __str__(self) : 
        return self.election_id 