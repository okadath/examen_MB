from django.urls import path 
from .views import CustomUserCreateView,CustomUserListByAge, CustomUserListByLastName, CustomUserListByAgeFilter, CustomUserUpdateView, CustomUserDeleteByEmailView, UserPDFView

urlpatterns = [
    path('create-user/', CustomUserCreateView.as_view(), name='create-user'),
    path('users/by-age/', CustomUserListByAge.as_view(), name='user-list-by-age'),
    path('users/filter-by-age/', CustomUserListByAgeFilter.as_view(), name='user-filter-by-age'),
    path('users/by-lastname/', CustomUserListByLastName.as_view(), name='user-list-by-lastname'),
    path('update-user/<str:email>/', CustomUserUpdateView.as_view(), name='update-user'),  
    path('delete-user/<str:email>/', CustomUserDeleteByEmailView.as_view(), name='delete-user-by-email'),
    path('generate-users-pdf/', UserPDFView.as_view(), name='generate_users_pdf'),
]