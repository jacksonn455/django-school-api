from school.models import Student, Course, Registration
from school.serializers import StudentSerializer, CourseSerializer, RegistrationSerializer, \
ListRegistrationStudentSerializer, ListRegistrationCourseSerializer
from rest_framework import viewsets, generics

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    
class RegistrationViewSet(viewsets.ModelViewSet):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
    
class ListRegistrationStudentViewSet(generics.ListAPIView):
    def get_queryset(self):
        queryset = Registration.objects.filter(student_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListRegistrationStudentSerializer
    
class ListRegistrationCourseViewSet(generics.ListAPIView):
    def get_queryset(self):
        queryset = Registration.objects.filter(course_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListRegistrationCourseSerializer