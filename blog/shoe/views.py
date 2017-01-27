from .models import Shoe
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ShoeSerializer

class ShoeList(APIView):

    def get(self, request):
        shoes = Shoe.objects.all()
        serializer = ShoeSerializer(shoes, many=True)
        return Response(serializer.data)


def shoe_list(request):
    queryset_list = Shoe.objects.all()
    query = request.GET.get("q")
    if query:
        queryset_list = queryset_list.filter(
            Q(brand__icontains=query) |
            Q(type__icontains=query) |
            Q(description__icontains=query)
        ).distinct()

    paginator = Paginator(queryset_list, 9)  # how many contacts per page

    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
          # If page is not an integer, deliver first page.
          queryset = paginator.page(1)
    except EmptyPage:
          # If page is out of range (e.g. 9999), deliver last page of results.
          queryset = paginator.page(paginator.num_pages)

    context = {
        "instance": queryset
    }
    return render(request, "shoe/shoe_list.html",context)

def shoe_adidas(request):
    queryset_list = Shoe.objects.all().filter(brand="Adidas")
    paginator = Paginator(queryset_list, 9)  # how many contacts per page

    page = request.GET.get('page')
    try:
        queryset_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset_list = paginator.page(paginator.num_pages)


    context = {
        "type": "adidas",
        "instance": queryset_list
    }
    return render(request, "shoe/shoe_list.html",context)

def shoe_nike(request):
    queryset_list = Shoe.objects.all().filter(brand="Nike")

    paginator = Paginator(queryset_list, 9)  # how many contacts per page

    page = request.GET.get('page')
    try:
        queryset_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset_list = paginator.page(paginator.num_pages)
    context = {
        "type": "nike",
        "instance": queryset_list
    }
    return render(request, "shoe/shoe_list.html",context)

def shoe_puma(request):
    queryset_list = Shoe.objects.all().filter(brand="Puma")

    paginator = Paginator(queryset_list, 9)  # how many contacts per page

    page = request.GET.get('page')
    try:
        queryset_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset_list = paginator.page(paginator.num_pages)
    context = {
        "type": "puma",
        "instance": queryset_list
    }
    return render(request, "shoe/shoe_list.html",context)

def shoe_detail(request, shoe_id):
    queryset_list = get_object_or_404(Shoe, id=shoe_id)
    context = {
        "sid": shoe_id,
        "type": "detail",
        "instance": queryset_list,
    }
    return render(request, "shoe/shoe_detail.html", context)


