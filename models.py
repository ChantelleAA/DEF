from django.db import models

class Client(models.Model):
    CLAIM_TYPES = [
        ('appeals', 'Appeals'),
        ('aviation', 'Aviation'),
        ('business_dispute', 'Business Dispute'),
        ('chancery', 'Chancery'),
        ('clinical_negligence', 'Clinical Negligence'),
        ('construction', 'Construction'),
        ('costs', 'Costs'),
        ('employment', 'Employment'),
        ('family_children', 'Family – Children'),
        ('family_divorce', 'Family – Divorce'),
        ('family_financial', 'Family – Financial'),
        ('family_inheritance', 'Family – Inheritance Act'),
        ('fire_damage', 'Fire damage'),
        ('flood_damage', 'Flood damage'),
        ('personal_injury_abuse_claims', 'Personal Injury - Abuse claims'),
        ('personal_injury_cica', 'Personal Injury - CICA'),
        ('personal_injury_employer_liability', 'Personal Injury - Employer Liability'),
        ('personal_injury_mib_untraced', 'Personal Injury - MIB untraced'),
        ('personal_injury_military', 'Personal Injury - Military'),
        ('personal_injury_occupational_disease', 'Personal Injury - Occupational disease'),
        ('personal_injury_public_liability', 'Personal Injury - Public Liability (PL)'),
        ('personal_injury_road_traffic_whiplash', 'Personal injury - Road Traffic and Whiplash'),
        ('personal_injury_travel', 'Personal injury - Travel'),
        ('planning', 'Planning'),
        ('property_non_fire_flood', 'Property (non-fire/flood)'),
        ('shipping', 'Shipping'),
        ('travel_abta', 'Travel – ABTA'),
        ('travel_non_abta', 'Travel – non-ABTA'),
        ('workplace_issues', 'Workplace issues (not personal injury)')
    ]

    name = models.CharField(max_length=100)
    contact_info = models.TextField()
    claims = models.TextField()
    claim_type = models.CharField(max_length=50, choices=CLAIM_TYPES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Mediator(models.Model):
    name = models.CharField(max_length=100)
    contact_info = models.TextField()
    expertise = models.JSONField()  # List of expertise areas
    experience = models.TextField()
    membership = models.TextField()
    style_approach = models.TextField()
    availability = models.JSONField()  # List of available days and times
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Case(models.Model):
    clients = models.ManyToManyField(Client, through='CaseClient')
    title = models.CharField(max_length=200)
    description = models.TextField()
    case_type = models.CharField(max_length=50, choices=Client.CLAIM_TYPES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class CaseClient(models.Model):
    case = models.ForeignKey(Case, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Appointment(models.Model):
    case = models.ForeignKey(Case, on_delete=models.CASCADE)
    mediator = models.ForeignKey(Mediator, on_delete=models.CASCADE)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Keyword(models.Model):
    word = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class CaseKeyword(models.Model):
    case = models.ForeignKey(Case, on_delete=models.CASCADE)
    keyword = models.ForeignKey(Keyword, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class MediatorKeyword(models.Model):
    mediator = models.ForeignKey(Mediator, on_delete=models.CASCADE)
    keyword = models.ForeignKey(Keyword, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
