from django.shortcuts import render #old
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .serializers import FileSerializer
# from .detect.functionBaseOut import detectImg
from functionBase import detectImg
# import functionBase as fn
# from .functionBase import detectImg
import os

class FileView(APIView):
  parser_classes = (MultiPartParser, FormParser)

  def post(self, request, *args, **kwargs):
    # a = "abc " +
    # !python detect.py --weights finel.pt --conf 0.4 --img-size 640 --source .\upload\+request.data['file']
    # print(request.data)
    file_serializer = FileSerializer(data=request.data)
    if file_serializer.is_valid():
      file_serializer.save()
      # # detectImg(w=r'.\file_app\detect\finel.pt',s=r'.\media\\'+ str(request.data['file']),i=640,c=0.25,io=0.45,d='',v=False,st=True,sc=True,ns=False,cls='',ag='',au='',upd='',pr='runs/detect',na='exp',ex='',no='')
      cmd = r"python .\file_app\detect\detect.py --weights .\file_app\detect\finel.pt --conf 0.4 --img-size 640 --source .\media\\" + str(request.data['file'])
      # print(cmd)
      os.system(cmd)

      f = open(r"A:\yolo7\api\fileupload\file_app\data.txt", "r")
      # print(f.read())

      return Response(f.read())
      # return Response(file_serializer.data, status=status.HTTP_201_CREATED)
    else:
      return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# Create your views here.
