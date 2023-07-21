from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .models.Academic import Academic
from .models.Assignment import Assignment
from .models.Course import Course
from .models.Department import Department
from .models.Enroll import Enroll
from .models.Faculty import Faculty
from .models.Group import Group
from .models.Organization import Organization
from .models.Plan import Plan
from .models.School import School
from .models.Semester import Semester
from .models.Student import Student
from .models.Teacher import Teacher
from .models.User_Type import User_Type
from .models.User import User
from rest_framework import viewsets, permissions, status
from .serializers import *

#ViewSets
class AcademicViewSet(viewsets.ModelViewSet):
    queryset = Academic.objects.all()
    serializer_class = AcademicSerializer
    permission_classes = [permissions.AllowAny]

class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = Assignment.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = Assignment

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CourseSerializer

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = DepartmentSerializer

class EnrollViewSet(viewsets.ModelViewSet):
    queryset = Enroll.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = EnrollSerializer

class FacultyViewSet(viewsets.ModelViewSet):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer
    permission_classes = [permissions.AllowAny]

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.AllowAny]

class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [permissions.AllowAny]

class PlanViewSet(viewsets.ModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer
    permission_classes = [permissions.AllowAny]

class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    permission_classes = [permissions.AllowAny]

class SemesterViewSet(viewsets.ModelViewSet):
    queryset = Semester.objects.all()
    serializer_class = SemesterSerializer
    permission_classes = [permissions.AllowAny]

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.AllowAny]

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [permissions.AllowAny]

class User_TypeViewSet(viewsets.ModelViewSet):
    queryset = User_Type.objects.all()
    serializer_class = User_TypeSerializer
    permission_classes = [permissions.AllowAny]

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]