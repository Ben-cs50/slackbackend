from  django.http import  JsonResponse
from  .models import slackdetaisl
from .serializers import slackdetaislSerializer


def slack_detaisl(request):
    slackdetails = slackdetaisl.objects.all()
    serial = slackdetaislSerializer(slackdetails, many=True)

    return JsonResponse(serial.data, safe=False)
