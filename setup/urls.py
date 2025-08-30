from django.contrib import admin
from django.urls import path, include
from school.views import StudentViewSet, CourseViewSet, \
RegistrationViewSet, ListRegistrationStudentViewSet, ListRegistrationCourseViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('students', StudentViewSet, basename='Students')
router.register('courses', CourseViewSet, basename='Courses')
router.register('registrations', RegistrationViewSet, basename='Registrations')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('students/<int:pk>/registrations/', ListRegistrationStudentViewSet.as_view()),
    path('courses/<int:pk>/registrations/', ListRegistrationCourseViewSet.as_view())
]
