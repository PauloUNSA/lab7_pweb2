from rest_framework import serializers
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

class AcademicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Academic
        fields = ('academic_id', 'academic_name', 'academic_status', 'academic_created', 'academic_modified', 'department_id', 'organization_id')
        read_only_fields = ('academic_id', 'academic_created', 'academic_modified')

class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = ('assignment_id', 'assignment_status', 'assignment_created', 'assignment_modified', 'academic_id', 'teacher_id', 'course_id', 'organization_id')
        read_only_fields = ('assignment_id', 'assignment_created', 'assignment_modified')

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('course_id', 'course_name', 'course_status', 'course_created', 'course_modified', 'organization_id')

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('department_id', 'department_name', 'department_status', 'department_created', 'department_modified', 'organization_id')

class EnrollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enroll
        fields = ('enroll_id', 'enroll_status', 'enroll_created', 'enroll_modified', 'student_id', 'group_id', 'organization_id')
        read_only_fields = ('enroll_id', 'enroll_created', 'enroll_modified')

class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = ('faculty_id', 'faculty_name', 'faculty_status', 'faculty_created', 'faculty_modified', 'organization_id')

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('group_id', 'group_name', 'group_status', 'group_created', 'group_modified', 'assignment_id', 'teacher_id', 'organization_id')
        read_only_fields = ('group_id', 'group_created', 'group_modified')

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ('organization_id', 'organization_name', 'organization_status', 'organization_created', 'organization_modified')

class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = ('plan_id', 'plan_year', 'plan_status', 'plan_created', 'plan_modified', 'organization_id')

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ('school_id', 'school_name', 'school_status', 'school_created', 'school_modified', 'organization_id')

class SemesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Semester
        fields = ('semester_id', 'semester_name', 'semester_status', 'semester_created', 'semester_modified', 'organization_id')

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('student_id', 'student_status', 'student_created', 'student_modified', 'user_id', 'school_id', 'organization_id')

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('teacher_id', 'teacher_name', 'teahcer_email', 'teacher_status', 'teacher_created', 'teacher_modified', 'organization_id', 'user_id')

class User_TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Type
        fields = ('user_type_id', 'user_type_name', 'user_type_status', 'user_type_created', 'user_type_modified')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('user_id', 'user_dni', 'user_password', 'user_name', 'user_last_name', 'user_dob', 'user_email', 'user_type_id')
        extra_kwargs = {'user_password': {'write_only': True}}