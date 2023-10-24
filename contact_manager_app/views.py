from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .serializers import UserSerializer, ContactSerializer
from .models import Contact
from django.http import JsonResponse

# View for creating a new user (user registration)


class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def create(self, request, *args, **kwargs):
        # Check if a user with the same username already exists
        existing_user_username = User.objects.filter(username=request.data.get('username')).first()
        
        # Check if a user with the same email already exists
        existing_user_email = User.objects.filter(email=request.data.get('email')).first()

        if existing_user_username or existing_user_email:
            # Return a 400 Bad Request response if the user already exists
            return Response({"error": "User with this username or email already exists."}, status=status.HTTP_400_BAD_REQUEST)

        # If the user doesn't exist, proceed with the registration
        return super().create(request, *args, **kwargs)


# View for logging user in

class UserLoginView(ObtainAuthToken, APIView):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)

        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        }, status=status.HTTP_200_OK)


# View for logging user out

class UserLogoutView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Check if the user is authenticated and has a token
        if request.auth:
            request.auth.delete()
            return Response(status=status.HTTP_200_OK)
        else:
            # User is not authenticated
            return Response(status=status.HTTP_401_UNAUTHORIZED)


# View for creating a new contact


class ContactCreateView(CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

# View for listing all contacts


class ContactListView(ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    
    def get_queryset(self):
        # Check if the user is authenticated
        if self.request.user.is_authenticated:
            # Filter contacts by the currently authenticated user
            return Contact.objects.filter(user=self.request.user)
        else:
            # User is not authenticated, return a handle as needed
            return JsonResponse({"message": "User is not authenticated."}, status=400)

# View for retrieving details of a single contact


class ContactDetailView(RetrieveAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

# View for updating a contact


class ContactUpdateView(UpdateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticated]

# View for deleting a contact


class ContactDeleteView(DestroyAPIView):
    queryset = Contact.objects.all()
