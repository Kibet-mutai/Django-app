from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

User = get_user_model()
class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'native_name', 'phone_no')
        extra_kwargs = {
            'native_name': {'required': True},
            'phone_no': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            native_name=validated_data['native_name'],
            phone_no=validated_data['phone_no']
        )

        
        user.set_password(validated_data['password'])
        user.save()

        return user



class TokenSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(TokenSerializer, cls).get_token(user)

        # Add custom claims
        token['email'] = user.email
        return token