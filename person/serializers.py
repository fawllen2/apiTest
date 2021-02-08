from rest_framework import serializers
from django.utils import timezone
from .models import Person


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'
        read_only_fields = ("created_at", "updated_at")

    def create(self, validated_data):
        obj = super().create(validated_data)

        obj.created_at = timezone.now()
        obj.save()
        return obj

    def update(self, instance, validated_data):
        old_created_at = instance.created_at

        obj = super().update(instance, validated_data)
        obj.created_at = old_created_at
        obj.updated_at = timezone.now()
        obj.save()
        return obj

