from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import list
from .forms import ListForm
from django.contrib import messages

from .serializers import listserializer


def home(request):
    if request.method == 'POST':
        form = ListForm(request.POST or None)
        if form.is_valid():
            form.save()
            all_items = list.objects.all()
            messages.success(request, 'item has been added to list!')
            return render(request, 'home.html', {'all_items': all_items})
    else:
        all_items = list.objects.all()
        return render(request, 'home.html', {'all_items': all_items})


def delete(request, list_id):
    item = list.objects.get(pk=list_id)
    item.delete()
    messages.success(request, 'item has been successfully deleted!')
    return redirect('home')


def crossoff(request, list_id):
    item = list.objects.get(pk=list_id)
    item.completed = True
    item.save()
    return redirect('home')


def uncross(request, list_id):
    item = list.objects.get(pk=list_id)
    item.completed = False
    item.save()
    return redirect('home')


@api_view(['GET'])
def getlist(request):
    List = list.objects.all()
    serializer = listserializer(List, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def Postlist(request):
    serializer = listserializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def deletelist(request, pk):
    List = list.objects.get(id=pk)
    List.delete()
    return Response('item delete successfull')


class GETLIST(APIView):
    def get(self, request):
        List = list.objects.all()
        serializer = listserializer(List, many=True)
        return Response(serializer.data)


class DELETEVIEW(APIView):
    def delete(self, request, List_id, format=None):
        List = list.objects.get(pk=List_id)
        List.delete()
        return Response('item delete successfull')


class postview(APIView):
    def post(self, request, format=None):
        serializer = listserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
