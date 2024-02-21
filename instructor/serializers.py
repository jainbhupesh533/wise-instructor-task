# serializers.py
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import CheckInOut
from .models import Instructor


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['username', 'email', 'password']
		extra_kwargs = {'password': {'write_only': True}}  # Ensure password is write-only

	def create(self, validated_data):
		user = User.objects.create_user(**validated_data)
		return user


class InstructorSerializer(serializers.ModelSerializer):
	user = UserSerializer()  # Embed UserSerializer for handling user creation

	class Meta:
		model = Instructor
		fields = '__all__'

	def create(self, validated_data):
		user_data = validated_data.pop('user')  # Extract user data
		user = UserSerializer.create(UserSerializer(), validated_data=user_data)  # Create user
		instructor = Instructor.objects.create(user=user)  # Create instructor
		return instructor


class CheckInOutSerializer(serializers.ModelSerializer):
	class Meta:
		model = CheckInOut
		fields = '__all__'