from django.shortcuts import get_object_or_404, render
from rest_framework.response import Response

# Create your views here.
from .serializers import *
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework import viewsets
from .models import Portfolio

class GetStartedAPIView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated] #[AllowAny] #
    serializer_class = PortfolioSerializer
    queryset = Portfolio.objects.all()

    def get_queryset(self):
        return Portfolio.objects.filter(owner=self.request.user)
    
    def get_object(self):
        obj = get_object_or_404(self.queryset, owner=self.request.user)
        self.check_object_permissions(self.request, obj)
        return obj
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def perform_update(self, serializer):
        instance = self.get_object()  # instance before update
        if self.request.user.is_authenticated:
            serializer.save(owner=self.request.user)


class ListPortfolio(viewsets.ViewSet):
    serializer_class = PortfolioSerializer

    def list(self, request):
        queryset = Portfolio.objects.all()
        serializer = PortfolioSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Portfolio.objects.all()
        qre = get_object_or_404(queryset, pk=pk)
        serializer = PortfolioSerializer(qre)
        return Response(serializer.data)
