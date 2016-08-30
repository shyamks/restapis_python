from django.shortcuts import render

from .models import *
from .serializers import *
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser


@api_view(['GET', 'POST','PUT'])
def allArticles(request):
    if request.method == 'GET':
        a_list = Article.objects.all()
        json = ReporterSerializer(a_list, many=True)
        return Response(json.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ReporterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT','DELETE'])
def article_detail(request, _id):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Article.objects.get(id=_id)
    except Article.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ReporterSerializer(snippet)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ReporterSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)