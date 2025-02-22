## views 

from .models import Job
from .serializers import JobSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics

@api_view(['GET'])
def joblist(request):
    job_api=Job.objects.all()
    jsondata=JobSerializer(job_api,many=True).data
    return Response({'data':jsondata})


@api_view(['GET'])
def job_details(request,id):
    job_details=Job.objects.get(id=id)
    jsondata=JobSerializer(job_details).data
    return Response({'data':jsondata})




class JobListApi(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer




class JobDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = JobSerializer
    queryset = Job.objects.all()
    lookup_field = 'id'