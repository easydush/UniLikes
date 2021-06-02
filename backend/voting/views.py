from django.db.models import Q
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response

from .models import RateFact
from .serializers import RateFactSerializer, NewRateFactSerializer
from teacher.models import Teacher

from account.utils import get_semester

from teacher.serializers import TeacherSerializer


class VotingViewSet(viewsets.ModelViewSet):
    serializer_class = TeacherSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user:
            semester = get_semester(self.request.user.admission_year)
            return Teacher.objects.filter(Q(subjects_semesters__semester=semester) &
                                          ~Q(ratefact__student=self.request.user) & ~Q(ratefact__semester=semester))
        else:
            return Teacher.objects.none()

    def create(self, request):
        serializer = NewRateFactSerializer(data=request.data)
        if serializer.is_valid():
            teacher_id = serializer.data.get('teacher_id')
            rate = serializer.data.get('rate')
            semester = get_semester(request.user.admission_year)
            student = request.user
            try:
                teacher = Teacher.objects.get(id=teacher_id)
                if rate != -1:
                    teacher.vote_counts += 1
                    teacher.rating = (teacher.rating * teacher.vote_counts + float(rate)) / float(teacher.vote_counts)
                    teacher.save()
                RateFact.objects.create(student=student, semester=semester, teacher=teacher)
                return Response(status=status.HTTP_200_OK)
            except Teacher.DoesNotExist:
                return Response(f'Teacher with id {teacher_id} has not found',
                                status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        response = {'message': 'Put function is prohibited for voting.'}
        return Response(response, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def destroy(self, request, pk=None):
        response = {'message': 'Delete function is prohibited for voting.'}
        return Response(response, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def partial_update(self, request, pk=None):  # just in case
        response = {'message': 'Patch function is prohibited for voting.'}
        return Response(response, status=status.HTTP_405_METHOD_NOT_ALLOWED)
