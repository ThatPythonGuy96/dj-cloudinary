from django.shortcuts import render
from .models import Image
from .serializers import ImageSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class ImageUploadView(APIView):
    serializer_class = ImageSerializer

    def post(self, request, *args, **kwargs):
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
class ImageView(APIView):
    def get(self, request, *args, **kwargs):
        images = Image.objects.all()
        serializer = ImageSerializer(images, many=True)
        return Response(serializer.data)
