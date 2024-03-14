from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets, generics, permissions
from rest_framework.generics import ListCreateAPIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


from .models import *
from .serializers import *
# Create your views here.

def sayHello(request):
    return HttpResponse('Hello World')

def index(request):
    return render(request, 'index.html', {})

class bookingview(APIView):
    
    def get(self,request):
        items = Booking.objects.all()
        serializer = bookingSerializer(items, many=True)
        return Response(serializer.data)
    
class menuview(APIView):
    
    def get(self,request):
        items = Menu.objects.all()
        serializer = menuSerializer(items, many=True)
        return Response(serializer.data)
    
    def port(self,request):
        serializer = menuSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'success', 'data': serializer.data})
        
class UserViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   permission_classes = [permissions.IsAuthenticated] 
    

class MenuItemsView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = menuSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = menuSerializer
    
    
class BookingViewSet(viewsets.ModelViewSet):
   Permission_classes = [IsAuthenticated]
   queryset = Booking.objects.all()
   serializer_class = bookingSerializer
   permission_classes = [permissions.IsAuthenticated] 
    
@api_view()
@permission_classes([IsAuthenticated])
#@authentication_classes([TokenAuthentication])
def msg(request):
    return Response({"message":"This view is protected"})    
        
        