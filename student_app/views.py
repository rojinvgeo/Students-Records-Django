from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import *
from django.core.paginator import Paginator

# Create your views here.

def student_form(request):
    if request.method == 'POST':
        # Process the form data here
        student_id = request.POST.get('student_id')
        name = request.POST.get('name')
        gender= request.POST.get('gender')
        batch = request.POST.get('batch')
        age = request.POST.get('age')
        address = request.POST.get('address')
        guardian = request.POST.get('guardian')
        phone = request.POST.get('phone')


        # Creating a new Student object
        student = Student(
            student_id=student_id,
            name=name,
            gender=gender,
            batch=batch,
            age=age,
            address=address,
            guardian=guardian,
            phone=phone
        )
        student.save()

        # Redirect or render success message after saving
        return redirect('student_details')
    # Show the form
    return render(request, 'student-record.html')


from django.db.models import Q  # at the top of your views.py file


def student_details(request):
    query = request.GET.get('q', '')  # get search text, empty string if none
    sort_by = request.GET.get('sort', '')  # Add this to get sorting field
    page_number = request.GET.get('page', 1)
    if query:
        students = Student.objects.filter(
            Q(name__icontains=query) | Q(student_id__icontains=query)
        )
    else:
        students = Student.objects.all()

    no_results = not students.exists() and query != ''  # True if no students found and query not empty

     # Sort the queryset based on the sort parameter
    if sort_by in ['name', 'batch', 'age']:
        students = students.order_by(sort_by)

    # Paginate : 4 students per page
    paginator = Paginator(students, 4)
    page_obj = paginator.get_page(page_number)


    return render(request, 'student-details.html', {
        'students': students,
        'query': query,
       'no_results': no_results,
        'page_obj': page_obj, 
         'sort': sort_by,
        # to keep the search input filled
    })






#orginal code

# def student_details(request):
#     students = Student.objects.all()  # Fetch all student records
#     return render(request, 'student-details.html', {'students': students})



# Edit View
def edit_student(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':
        student.student_id = request.POST.get('student_id')
        student.name = request.POST.get('name')
        student.gender = request.POST.get('gender')
        student.batch = request.POST.get('batch')
        student.age = request.POST.get('age')
        student.address = request.POST.get('address')
        student.guardian = request.POST.get('guardian')
        student.phone = request.POST.get('phone')
        student.save()

        return redirect('student_details')

    return render(request, 'student-edit.html', {'student': student})


# Delete View
def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('student_details')


def hello(request):
    return HttpResponse("Hello, world! This is the student")

