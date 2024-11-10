from django.db import models
from django.utils import timezone

class UserAccount(models.Model):
    name = models.CharField(max_length=100)
    userid = models.CharField(max_length=100)
    email = models.EmailField()
    GROUP_CHOICES = [
        ('development', 'Development'),
        ('commercial', 'Commercial'),
        ('production', 'Production'),
        ('service', 'Service'),
        ('users', 'Users'),
        ('other', 'Other'),
    ]
    group = models.CharField(max_length=50, choices=GROUP_CHOICES)
    
    ROLE_CHOICES = [
        ('viewer', 'Viewer'),
        ('designer', 'Designer'),
        ('other', 'Other'),
    ]
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)
    licenselevel = models.CharField(max_length=50, editable=False)
    
    EMPLOYMENT_TYPE_CHOICES = [
        ('MSD', 'MSD'),
        ('other', 'Other'),
    ]
    employment_type = models.CharField(max_length=50, choices=EMPLOYMENT_TYPE_CHOICES)
    company_name = models.CharField(max_length=100, blank=True, null=True)
    IP_CLEARANCE_CHOICES = [
        ('Level 1', 'Level 1'),
        ('Level 3', 'Level 3'),
    ]
    ip_clearance_level = models.CharField(max_length=50, choices=IP_CLEARANCE_CHOICES, blank=True, null=True)
    ip_clearance = models.CharField(max_length=50, blank=True, editable=False)
    
    catalog_task_id = models.CharField(max_length=50, blank=True, null=True)
    submission_date = models.DateTimeField(default=timezone.now)
    
    def save(self, *args, **kwargs):
        # Automatically set licenselevel and ip_clearance based on conditions
        if self.role.lower() == 'viewer':
            self.licenselevel = 'consumer'
        else:
            self.licenselevel = 'author'
        
        if self.employment_type.lower() == 'msd' or self.ip_clearance_level == 'Level 3':
            self.ip_clearance = 'Restricted'
        else:
            self.ip_clearance = ''
        
        super(UserAccount, self).save(*args, **kwargs)
