from rest_framework import serializers
from .models import User, VerificationCode
import random

class PhoneSerializer(serializers.Serializer):
    phone = serializers.CharField()

    def create(self, validated_data):
        phone = validated_data['phone']
        user, created = User.objects.get_or_create(phone=phone, username=phone)
        code = ''.join(random.choices('0123456789', k=4))
        VerificationCode.objects.create(user=user, code=code)
        return {'phone': phone, 'code': code}

class VerifySerializer(serializers.Serializer):
    phone = serializers.CharField()
    code = serializers.CharField()
    invite_code = serializers.CharField(required=False)

    def validate(self, data):
        phone = data['phone']
        code = data['code']
        invite_code = data.get('invite_code')

        try:
            user = User.objects.get(phone=phone)
        except User.DoesNotExist:
            raise serializers.ValidationError("User not found")

        if not VerificationCode.objects.filter(user=user, code=code).exists():
            raise serializers.ValidationError("Invalid code")

        user.is_verified = True
        if invite_code:
            inviter = User.objects.filter(invite_code=invite_code).first()
            if inviter:
                user.invited_by = inviter
        user.save()
        return data

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'phone', 'invite_code']

