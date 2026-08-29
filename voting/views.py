from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm
from .models import Election, Candidate, StudentProfile
from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            user = form.save()

            student_number = form.cleaned_data['student_number']

            student = StudentProfile.objects.get(
                student_number=student_number
            )

            student.user = user
            student.save()

            login(request, user)

            return redirect('dashboard')

    else:
        form = RegistrationForm()

    return render(
        request,
        'voting/register.html',
        {'form': form}
    )

@login_required(login_url='login')
def dashboard(request):
    return render(request, 'voting/dashboard.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)

            if user.is_staff:
                return redirect('admin_dashboard')

            return redirect('dashboard')

        return render(
            request,
            'voting/login.html',
            {'error': 'Invalid username or password.'}
        )

    return render(request, 'voting/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')    

def home(request):
    return render(request, 'voting/home.html')

def admin_dashboard(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if not request.user.is_staff:
        return redirect('dashboard')

    total_elections = Election.objects.count()
    total_candidates = Candidate.objects.count()
    total_voters = User.objects.filter(is_staff=False).count()

    return render(
        request,
        'voting/admin_dashboard.html',
        {
            'total_elections': total_elections,
            'total_candidates': total_candidates,
            'total_voters': total_voters,
        }
    )

def manage_elections(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if not request.user.is_staff:
        return redirect('dashboard')

    elections = Election.objects.all().order_by('-id')

    return render(
        request,
        'voting/manage_elections.html',
        {
            'elections': elections,
        }
    )

def create_election(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if not request.user.is_staff:
        return redirect('dashboard')

    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        status = request.POST.get('status')

        Election.objects.create(
            title=title,
            description=description,
            start_date=start_date,
            end_date=end_date,
            status=status
        )

        return redirect('manage_elections')

    return render(request, 'voting/create_election.html')