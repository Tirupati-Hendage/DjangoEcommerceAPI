from django.shortcuts import render
from .serializers import CategorySerializer, BookSerializer, ProductSerializer
from .models import Category, Book, Product
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
# Create your views here.

class CategoryModelViewSet(ModelViewSet):
	queryset = Category.objects.all()
	serializer_class = CategorySerializer
	authentication_classes = [SessionAuthentication]
	permission_classes = [IsAuthenticatedOrReadOnly]



class BookModelViewSet(ModelViewSet):
	queryset = Book.objects.all()
	serializer_class = BookSerializer
	authentication_classes = [SessionAuthentication]
	permission_classes = [IsAuthenticatedOrReadOnly]



class ProductModelViewSet(ModelViewSet):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer
	authentication_classes = [SessionAuthentication]
	permission_classes = [IsAuthenticatedOrReadOnly]