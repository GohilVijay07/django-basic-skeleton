from django.shortcuts import render

from .models import Resident, Notice, Facility, Visitor, Complaint


def index(request):
	residents = Resident.objects.select_related('user').all()
	notices = Notice.objects.select_related('posted_by').order_by('-posted_on')[:5]
	facilities = Facility.objects.all()
	visitors = Visitor.objects.order_by('-entry_time')[:5]
	complaints = Complaint.objects.order_by('-created_at')[:5]
	

	context = {
		'residents': residents,
		'notices': notices,
		'facilities': facilities,
		'visitors': visitors,
		'complaints': complaints,
		
	}

	return render(request, 'society/society.html', context)
#select * from society where age > 20
