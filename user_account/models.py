from django.db import models
from django.utils import timezone

GROUP_CHOICES = [
    ('development', 'Development'),
    ('commercial', 'Commercial'),
    ('production', 'Production'),
    ('service', 'Service'),
    ('users', 'Users'),
]

ROLE_CHOICES = [
    ('Viewer', 'Viewer'),
    ('Designer', 'Designer')
]

IP_CLEARANCE_LEVEL_CHOICES = [
    (1, 'Level 1'),
    (3, 'Level 3')
]

class UserData(models.Model):
    name = models.CharField(max_length=50, unique=True)
    user_id = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)  # Ensure email is unique
    group = models.CharField(max_length=20, choices=GROUP_CHOICES)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    employment_type = models.CharField(max_length=50)
    ip_clearance_level = models.IntegerField(choices=IP_CLEARANCE_LEVEL_CHOICES, blank=True, null=True)
    license_level = models.CharField(max_length=20, default='consumer')
    ip_clearance_status = models.CharField(max_length=20, blank=True, null=True)
    catalog_tasks_id = models.CharField(max_length=50, unique=True, blank=True, null=True)  # Ensure catalog_tasks_id is unique
    submission_date = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        # Set license level based on role
        self.license_level = 'consumer' if self.role == 'Viewer' else 'author'
        
        # Set ip_clearance_status based on employment_type and ip_clearance_level
        if self.employment_type == 'MSD' or self.ip_clearance_level == 3:
            self.ip_clearance_status = 'Restricted'
        else:
            self.ip_clearance_status = ''
        
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} - {self.user_id}"
