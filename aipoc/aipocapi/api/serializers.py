from rest_framework import serializers
from aipocapi.models import robo,ques


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = robo
        fields = ['id','status','temp','con_speed','cpu','camera','ir']

class Recent_questions(serializers.ModelSerializer):
    class Meta:
        model = ques
        fields = ['id','asked_ques']