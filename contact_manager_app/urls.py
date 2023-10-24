from django.urls import path
from . import views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

app_name = 'contact_manager_app'

schema_view = get_schema_view(
   openapi.Info(
      title="Contact Manager API",
      default_version='v1',
      description="A RESTful API for saving and managing contacts.",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('users/login/', views.UserLoginView.as_view(), name='user-login'),
    path('users/logout/', views.UserLogoutView.as_view(), name='user-logout'),
    path('users/create/', views.UserCreateView.as_view(), name='user-create'),
    path('contacts/create/', views.ContactCreateView.as_view(),
         name='contact-create'),
    path('contacts/list/', views.ContactListView.as_view(), name='contact-list'),
    path('contacts/detail/<int:pk>/',
         views.ContactDetailView.as_view(), name='contact-detail'),
    path('contacts/update/<int:pk>/',
         views.ContactUpdateView.as_view(), name='contact-update'),
    path('contacts/delete/<int:pk>/',
         views.ContactDeleteView.as_view(), name='contact-delete'),
    
     # Swagger 
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
]
