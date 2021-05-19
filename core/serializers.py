from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from core.models import Branch


class BranchSerializer(ModelSerializer):
    bank = serializers.CharField(label="bank", source="bank.name")

    class Meta:
        model = Branch
        fields = "__all__"
