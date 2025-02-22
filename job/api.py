## views 

from .models import Job
from .serializers import JobSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def joblist(request):
    job_api=Job.objects.all()
    jsondata=JobSerializer(job_api,many=True).data
    return Response({'data':jsondata})