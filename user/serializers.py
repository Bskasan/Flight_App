from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(
        required=True,
        # Check the email is unique.
        validators = [UniqueValidator(queryset=User.objects.all())]
    )

    class Meta:
        model = User
        exclude = [
            # Don't show them on admin panel
            # "password",
            "last_login",
            "date_joined",
            "groups",
            "user_permissions",
        ]
    
    # Validation for new Users
    def validate(self, attrs):
        if attrs.get('password', False):
            from django.contrib.auth.password_validation import validate_password
            from django.contrib.auth.hashers import make_password
            password = attrs['password']
            validate_password(password)
            attrs.update({'password': make_password(password)})
        return super().validate(attrs)
