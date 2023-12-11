from .models import RelaxedFit, RegularFit

from rest_framework import serializers


class RelaxedFitSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelaxedFit
        fields = ('fabric', 'ideal_for')


class RegularFitSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegularFit
        fields = ('fabric', 'ideal_for')
