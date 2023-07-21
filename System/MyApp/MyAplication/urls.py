from rest_framework import routers
from .api import *

router = routers.DefaultRouter()
    
router.register('api/academic', AcademicViewSet, 'academic')
router.register('api/assignment', AssignmentViewSet, 'assignment')
router.register('api/course', CourseViewSet, 'course')
router.register('api/group', GroupViewSet, 'group')
router.register('api/department', DepartmentViewSet, 'department')
router.register('api/enroll', EnrollViewSet, 'enroll')
router.register('api/faculty', FacultyViewSet, 'faculty')
router.register('api/organization', OrganizationViewSet, 'organization')
router.register('api/plan', PlanViewSet, 'plan')
router.register('api/school', SchoolViewSet, 'school')
router.register('api/semester', SemesterViewSet, 'semester')
router.register('api/student', StudentViewSet, 'student')
router.register('api/teacher', TeacherViewSet, 'teacher')
router.register('api/user_type', User_TypeViewSet, 'user_type')
router.register('api/user', UserViewSet, 'user')

urlpatterns = router.urls 