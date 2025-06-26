from django.shortcuts import render,redirect
from .forms import StudentForm
from .models import Students
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def userLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist!')
            return redirect('login')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('home')
    return render(request, 'user/login_register.html')



def home(request):
    search = ''
    if request.GET.get('search'):
        search = request.GET.get('search')
    students = Students.objects.filter(
        Q(name__icontains=search) |
        Q(email__icontains=search) |
        Q(roll_number__icontains=search) |
        Q(departmet__icontains=search)
    )
    
    context = {'students': students}
    return render(request, 'user/home.html', context)


def addStudent(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student added successfully!')
            return redirect ('home')
    context = {'form': form}
    return render(request, 'user/add_students.html', context)   


def updateStudent(request,pk):
    student = Students.objects.get(id=pk)
    form = StudentForm(instance=student)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.info(request, 'Student updated successfully!')
            return redirect ('home')
    context = {'form': form}
    return render(request, 'user/add_students.html', context)   


def deleteStudent(request, pk):
    student = Students.objects.get(id=pk)
    if request.method == 'POST':
        student.delete()
        messages.warning(request, 'Student deleted successfully!')
        return redirect ('home')
    context = {'student': student}
    return render(request, 'user/delete_student.html', context)