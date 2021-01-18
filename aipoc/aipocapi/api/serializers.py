from rest_framework import serializers
from aipocapi.models import robo


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = robo
        fields = ['id','status','temp','con_speed','cpu','camera','ir']