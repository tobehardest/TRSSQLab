from rest_framework import serializers
from api.models import *

class ChengduDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChengduData
        fields = '__all__'

class ChengduQuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = ChengduQuery
        fields = '__all__'

class ChengduResultsDTWSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChengduResultsDTW
        fields = '__all__'


class ChengduResultsEDRSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChengduResultsEDR
        fields = '__all__'
class ChengduResultsERPSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChengduResultsERP
        fields = '__all__'


class PortoDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PortoData
        fields = '__all__'


class PortoQuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = PortoQuery
        fields = '__all__'


class PortoResultsDTWSerializer(serializers.ModelSerializer):
    class Meta:
        model = PortoResultsDTW
        fields = '__all__'


class PortoResultsEDRSerializer(serializers.ModelSerializer):
    class Meta:
        model = PortoResultsEDR
        fields = '__all__'


class PortoResultsERPSerializer(serializers.ModelSerializer):
    class Meta:
        model = PortoResultsERP
        fields = '__all__'


class XianDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = XianData
        fields = '__all__'


class XianQuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = XianQuery
        fields = '__all__'


class XianResultsDTWSerializer(serializers.ModelSerializer):
    class Meta:
        model = XianResultsDTW
        fields = '__all__'


class XianResultsEDRSerializer(serializers.ModelSerializer):
    class Meta:
        model = XianResultsEDR
        fields = '__all__'


class XianResultsERPSerializer(serializers.ModelSerializer):
    class Meta:
        model = XianResultsERP
        fields = '__all__'
