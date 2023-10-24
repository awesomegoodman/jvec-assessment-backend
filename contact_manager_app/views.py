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

# View for creating a new user (user registration)


class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


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
