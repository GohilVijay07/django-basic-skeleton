from django.contrib import admin
from .models import (
    User,
    Resident,
    Visitor,
    Complaint,
    Facility,
    FacilityBooking,
    Maintenance,
    Payment,
    Expense,
    Notice,
    EmergencyAlert
)

admin.site.register(User)
admin.site.register(Resident)
admin.site.register(Visitor)
admin.site.register(Complaint)
admin.site.register(Facility)
admin.site.register(FacilityBooking)
admin.site.register(Maintenance)
admin.site.register(Payment)
admin.site.register(Expense)
admin.site.register(Notice)
admin.site.register(EmergencyAlert)
