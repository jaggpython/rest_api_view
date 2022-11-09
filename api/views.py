from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from .models import *
from .serializer import TodoSerializer


class TodoView(APIView):
    def get(self, request):
        return Response({
            'status': 200,
            'message': 'yes django restframework is working!!',
            'method_called': 'you called GET method'    

        })

    def post(self, request):
        return Response({
            'status': 200,
            'message': 'yes django restframework is working!!',
            'method_called': 'you called POST method' 
        })



class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer