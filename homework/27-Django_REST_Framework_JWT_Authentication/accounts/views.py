from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegisterSerializer, ProfileSerializer


@api_view(["POST"])
def register(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        username = serializer.validated_data["username"]

        if User.objects.filter(username=username).exists():
            return Response(
                {"error": "Username already exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer.save()
        return Response(
            {"message": "User created successfully"},
            status=status.HTTP_201_CREATED
        )
    return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST
    )


@api_view(["POST"])
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")

    user = authenticate(
        username=username,
        password=password
    )
    if user is None:
        return Response(
            {"error": "Wrong username or password"},
            status=status.HTTP_401_UNAUTHORIZED
        )
    refresh = RefreshToken.for_user(user)

    return Response({
        "refresh": str(refresh),
        "access": str(refresh.access_token)
    })


@api_view(["GET", "PUT", "DELETE"])
@permission_classes([IsAuthenticated])
def profile(request):
    user = request.user
    if request.method == "GET":
        serializer = ProfileSerializer(user)
        return Response(serializer.data)
    
    elif request.method == "PUT": 
        if "username" in request.data:
            user.username = request.data["username"]
        if "email" in request.data:
            user.email = request.data["email"]
        if "password" in request.data:
            user.set_password(request.data["password"])
        user.save()

        serializer = ProfileSerializer(user)
        return Response(serializer.data)

    elif request.method == "DELETE":
        user.delete()
        return Response(
            {"message": "Account deleted successfully"},
            status=status.HTTP_200_OK
        )