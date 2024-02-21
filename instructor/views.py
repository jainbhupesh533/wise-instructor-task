# views.py
from django.db.models import Sum, Count
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from .models import CheckInOut
from .serializers import CheckInOutSerializer, InstructorSerializer
from .utils import validate_check_in_out_times


class CreateInstructorAPIView(generics.CreateAPIView):
	serializer_class = InstructorSerializer

	def create(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response(serializer.data, status=status.HTTP_201_CREATED)


class CheckInAPIView(generics.CreateAPIView):
	serializer_class = CheckInOutSerializer
	permission_classes = [IsAuthenticated]

	def create(self, request, *args, **kwargs):
		# Validate input data
		instructor = request.user.instructor.id
		checkin_time = request.data.get('check_time')
		data = {
			'check_type': CheckInOut.CHECK_IN,
			'check_time': checkin_time,
			'instructor': instructor
		}
		valid_data, error_message = validate_check_in_out_times(data)
		if not valid_data:
			return Response({"error": error_message}, status=status.HTTP_400_BAD_REQUEST)

		serializer = self.get_serializer(data=data)
		serializer.is_valid(raise_exception=True)
		serializer.save(check_type=CheckInOut.CHECK_IN)
		return Response(serializer.data, status=status.HTTP_201_CREATED)


class CheckOutAPIView(generics.CreateAPIView):
	serializer_class = CheckInOutSerializer
	permission_classes = [IsAuthenticated]

	def create(self, request, *args, **kwargs):
		# Validate input data
		instructor = request.user.instructor.id
		checkin_time = request.data.get('check_time')
		data = {
			'check_type': CheckInOut.CHECK_OUT,
			'check_time': checkin_time,
			'instructor': instructor
		}
		valid_data, error_message = validate_check_in_out_times(data)
		if not valid_data:
			return Response({"error": error_message}, status=status.HTTP_400_BAD_REQUEST)

		serializer = self.get_serializer(data=data)
		serializer.is_valid(raise_exception=True)
		serializer.save(check_type=CheckInOut.CHECK_OUT)
		return Response(serializer.data, status=status.HTTP_201_CREATED)


from django.db.models import Sum
from datetime import timedelta


class MonthlyReportAPIView(APIView):
	def get(self, request):
		month = request.query_params.get('month')
		year = request.query_params.get('year')

		# Fetch check-in records for the given month and year
		queryset = CheckInOut.objects.filter(
			check_time__month=month,
			check_time__year=year,
			check_type=CheckInOut.CHECK_IN
		).values('instructor').annotate(checkin_count=Count('instructor'))

		# Create a dictionary to store instructor-wise check-in count
		monthly_report = {}
		for item in queryset:
			instructor_id = item['instructor']
			checkin_count = item['checkin_count']
			monthly_report[instructor_id] = checkin_count

		return Response(monthly_report, status=status.HTTP_201_CREATED)