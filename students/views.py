from django.http import JsonResponse
from .models import Student
import json
from django.views.decorators.csrf import csrf_exempt

# GET all students
@csrf_exempt
def get_students(request):
    students = list(Student.objects.values())
    return JsonResponse(students, safe=False)

# CREATE student
@csrf_exempt
def add_student(request):
    if request.method == "POST":
        data = json.loads(request.body)

        student = Student.objects.create(
            name=data['name'],
            email=data['email'],
            age=data['age']
        )

        return JsonResponse({"message": "Student created", "id": student.id})

# UPDATE student
@csrf_exempt
def update_student(request, id):
    if request.method == "PUT":
        data = json.loads(request.body)

        student = Student.objects.get(id=id)
        student.name = data['name']
        student.email = data['email']
        student.age = data['age']
        student.save()

        return JsonResponse({"message": "Student updated"})

# DELETE student
@csrf_exempt
def delete_student(request, id):
    if request.method == "DELETE":
        student = Student.objects.get(id=id)
        student.delete()

        return JsonResponse({"message": "Student deleted"})