from rest_framework import serializers
from django.contrib.auth.models import User
from . models import Profile
from . utils import sendEmail


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email']

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSerializer()
        fields = ['fullname','gender','profile_pix']

class RegistrationSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    username = serializers.CharField(write_only=True)
    email = serializers.EmailField(write_only=True)
    class Meta:
        model = Profile
        fields = ['fullname','username','email','password1','password2','gender','profile_pix']

    def validate(self,data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError("Password does not match!")
        return data

    def create(self, validated_data):
        username = validated_data.pop('username')
        email = validated_data.pop('email')
        password = validated_data.pop('password1')

        user = User.objects.create_user(username=username,email=email,password=password)
        profile = Profile.objects.create(
            user = user,
            fullname = validated_data['fullname'],
            gender = validated_data['gender'],
            profile_pix = validated_data.get('profile_pix')
        )
        # function to send email after registering
        sendEmail(email,profile.fullname)
        return profile
        