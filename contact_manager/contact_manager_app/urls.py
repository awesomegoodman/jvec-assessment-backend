from django.urls import path
from . import views

app_name = 'contact_manager_app'

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
]
