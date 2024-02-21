# utils.py
from datetime import timedelta

from django.core.exceptions import ValidationError
from django.utils import timezone
from .models import CheckInOut


def validate_check_in_out_times(data):
	try:
		check_time = timezone.datetime.strptime(data['check_time'], "%Y-%m-%d %H:%M:%S")
		check_type = data['check_type']
		previous_entry_time = check_time - timedelta(minutes=5)
		# Check if the instructor has already checked in/out at the provided time

		existing_check = CheckInOut.objects.filter(instructor_id=data['instructor'], check_time__gte=previous_entry_time,
            check_time__lte=check_time, check_type=check_type).exists()
		if existing_check:
			return False, f"Instructor already checked {'in' if check_type == CheckInOut.CHECK_IN else 'out'} at the provided time"

		return True, None
	except KeyError:
		return False, "Missing required fields"
	except ValueError:
		return False, "Invalid date/time format"