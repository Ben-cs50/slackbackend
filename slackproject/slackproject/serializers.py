from  rest_framework import  serializers
from .models import slackdetaisl
class slackdetaislSerializer(serializers.ModelSerializer):
    class Meta:
        model = slackdetaisl
        fields = ['slackUsername','backend','age','bio']