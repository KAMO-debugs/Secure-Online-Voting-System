from django.contrib import admin

from .models import (
    StudentProfile,
    Election,
    Candidate,
    Vote,
    AuditLog
)


@admin.register(Election)
class ElectionAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'election_type',
        'campus',
        'start_date',
        'end_date',
        'status',
    )

    list_filter = (
        'election_type',
        'campus',
        'status',
    )

    search_fields = (
        'title',
        'description',
        'campus',
    )

    ordering = (
        '-start_date',
    )


admin.site.register(Candidate)
admin.site.register(Vote)
admin.site.register(AuditLog)


@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):

    list_display = (
        'student_number',
        'full_name',
        'campus',
        'faculty',
        'registered',
        'eligible',
        'account_status',
        'user',
    )

    search_fields = (
        'student_number',
        'full_name',
        'user__username',
    )

    list_filter = (
        'campus',
        'faculty',
        'registered',
        'eligible',
        'account_status',
    )