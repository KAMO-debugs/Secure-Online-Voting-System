from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import StudentProfile


class RegistrationForm(UserCreationForm):

    student_number = forms.CharField(
        max_length=50,
        required=True,
        label='Student Number'
    )

    email = forms.EmailField(
        required=True
    )

    class Meta:
        model = User
        fields = [
            'student_number',
            'username',
            'email',
            'password1',
            'password2',
        ]

    def clean_student_number(self):
        student_number = self.cleaned_data['student_number'].strip()

        try:
            student = StudentProfile.objects.get(
                student_number=student_number
            )
        except StudentProfile.DoesNotExist:
            raise forms.ValidationError(
                'Student number was not found in the official student records.'
            )

        if not student.registered:
            raise forms.ValidationError(
                'You are not currently registered and cannot create a voting account.'
            )

        if student.account_status != 'ACTIVE':
            raise forms.ValidationError(
                'Your student account is not active.'
            )

        if student.user_id is not None:
            raise forms.ValidationError(
                'An account already exists for this student.'
            )

        return student_number