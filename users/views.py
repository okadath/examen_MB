from django.shortcuts import render
from rest_framework import generics
from .models import CustomUser
from .serializers import UserSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
  
from rest_framework.permissions import IsAuthenticated
 
from rest_framework.response import Response
from rest_framework import status


class CustomUserCreateView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


def selection_sort_by_age(users):
    n = len(users)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if users[j].age and users[min_index].age and users[j].age < users[min_index].age:
                min_index = j
        users[i], users[min_index] = users[min_index], users[i]
    return users

def selection_sort_by_last_name(users):
    n = len(users)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if users[j].last_name and users[min_index].last_name and users[j].last_name.lower() < users[min_index].last_name.lower():
                min_index = j
        users[i], users[min_index] = users[min_index], users[i]
    return users

class CustomUserListByAge(generics.ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        users = list(CustomUser.objects.all())
        return selection_sort_by_age(users)


minimum_age_param = openapi.Parameter(
    'minimum_age', 
    openapi.IN_QUERY, 
    description="Filter users by minimum age",
    type=openapi.TYPE_INTEGER
)
class CustomUserListByAgeFilter(generics.ListAPIView):
    serializer_class = UserSerializer

    @swagger_auto_schema(manual_parameters=[minimum_age_param])
    def get(self, request, *args, **kwargs): 
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        min_age = self.request.query_params.get('minimum_age', None)
        if min_age is not None:
            users = list(CustomUser.objects.filter(age__gte=min_age))
        else:
            users = list(CustomUser.objects.all())        
        return selection_sort_by_age(users)

class CustomUserListByLastName(generics.ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        users = list(CustomUser.objects.all())
        return selection_sort_by_last_name(users)




class CustomUserUpdateView(generics.UpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class =  UserSerializer
    lookup_field = 'email'  
    # hay que agregar autenticacion, la desactive por comodidad
    # permission_classes = [IsAuthenticated]



class CustomUserDeleteByEmailView(generics.DestroyAPIView):
    queryset = CustomUser.objects.all()
    lookup_field = 'email'  

    def delete(self, request, *args, **kwargs):
        email = kwargs.get('email')
        try: 
            user = CustomUser.objects.get(email=email)
            user.delete()  
            return Response({"message": "User deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except CustomUser.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)



from django.http import HttpResponse
from rest_framework.views import APIView
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from django.contrib.auth import get_user_model

User = get_user_model()

class UserPDFView(APIView): 

    def get(self, request, *args, **kwargs): 
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="users_list.pdf"' 
        p = canvas.Canvas(response, pagesize=letter)
        width, height = letter 
        p.setFont("Helvetica-Bold", 16)
        p.drawString(100, height - 50, "List of Users") 
        users = User.objects.all() 
        p.setFont("Helvetica", 12)
        y_position = height - 100 
        for user in users:
            p.drawString(100, y_position, f"Username: {user.username}, Email: {user.email}")
            y_position -= 20 
            if y_position < 50:
                p.showPage()   
                y_position = height - 50 
        p.showPage()
        p.save()

        return response
