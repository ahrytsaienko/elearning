from django.shortcuts import render
from courses.models import Course
from courses.form import CourseForm
from django.http import HttpResponseRedirect


# Create your views here.

def course_detail(request, course_id):
    course = Course.objects.get(id=course_id)
    return render(request, 'courses/detail.html', {
        'course': course,
    })


def course_list(request):
    course_list = Course.objects.all()
    return render(request, 'courses/course_list.html', {'course_list': course_list})


def course_add(request):
    if request.POST:
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect()
    else:
        form = CourseForm()
    return render(request, 'course/course_form.html', {
        'form': form,
    })
