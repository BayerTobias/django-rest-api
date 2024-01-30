from django.shortcuts import render
from rest_framework import permissions, viewsets
from .models import Todo
from .serializers import TodoSerializer
from django.core import serializers
from django.http import HttpResponse


class TodoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Todo.objects.all().order_by("-created_at")
    serializer_class = TodoSerializer
    permission_classes = []  # permissions.IsAuthenticated

    def create(self, request):
        todo = Todo.objects.create(
            title=request.data.get("title", ""),
            description=request.data.get("description", ""),
            user=request.user,
        )
        # POST statt data wenn form data
        serialized_obj = serializers.serialize("json", [todo])
        return HttpResponse(serialized_obj, content_type="application/json")
