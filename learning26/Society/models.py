from django.db import models

# =========================
# USER MODEL
# =========================
class User(models.Model):
    ROLE_CHOICES = (
        ('ADMIN', 'Admin'),
        ('RESIDENT', 'Resident'),
        ('SECURITY', 'Security'),
    )

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=15)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# =========================
# RESIDENT MODEL
# =========================
class Resident(models.Model):
    OWNERSHIP_CHOICES = (
        ('OWNER', 'Owner'),
        ('TENANT', 'Tenant'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    flat_no = models.CharField(max_length=10)
    wing = models.CharField(max_length=10)
    ownership = models.CharField(max_length=10, choices=OWNERSHIP_CHOICES)
    family_members = models.IntegerField()
    emergency_contact = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.flat_no} - {self.user.name}"


# =========================
# VISITOR MODEL
# =========================
class Visitor(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    flat_no = models.CharField(max_length=10)
    purpose = models.CharField(max_length=100)
    entry_time = models.DateTimeField(auto_now_add=True)
    exit_time = models.DateTimeField(null=True, blank=True)
    approval_status = models.BooleanField(default=False)

    def __str__(self):
        return self.name


# =========================
# COMPLAINT MODEL
# =========================
class Complaint(models.Model):
    STATUS_CHOICES = (
        ('PENDING', 'Pending'),
        ('IN_PROGRESS', 'In Progress'),
        ('RESOLVED', 'Resolved'),
    )

    resident = models.ForeignKey(Resident, on_delete=models.CASCADE)
    category = models.CharField(max_length=50)
    description = models.TextField()
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category


# =========================
# FACILITY MODEL
# =========================
class Facility(models.Model):
    name = models.CharField(max_length=100)
    charge = models.DecimalField(max_digits=8, decimal_places=2)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class FacilityBooking(models.Model):
    facility = models.ForeignKey(Facility, on_delete=models.CASCADE)
    resident = models.ForeignKey(Resident, on_delete=models.CASCADE)
    booking_date = models.DateField()
    time_slot = models.CharField(max_length=50)
    payment_status = models.BooleanField(default=False)


# =========================
# MAINTENANCE & PAYMENT
# =========================
class Maintenance(models.Model):
    resident = models.ForeignKey(Resident, on_delete=models.CASCADE)
    month = models.CharField(max_length=20)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateField()
    status = models.BooleanField(default=False)


class Payment(models.Model):
    maintenance = models.ForeignKey(Maintenance, on_delete=models.CASCADE)
    payment_date = models.DateTimeField(auto_now_add=True)
    mode = models.CharField(max_length=20)
    transaction_id = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)


class Expense(models.Model):
    category = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    expense_date = models.DateField()
    description = models.TextField()


# =========================
# NOTICE MODEL
# =========================
class Notice(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    posted_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# =========================
# EMERGENCY ALERT MODEL
# =========================
class EmergencyAlert(models.Model):
    alert_type = models.CharField(max_length=50)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.alert_type 