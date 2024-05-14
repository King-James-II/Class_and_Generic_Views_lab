from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from .models import Course, Lesson, Enrollment
from django.urls import reverse
from django.views import generic, View
from django.http import Http404

# Generic class-based views

class CourseListView(generic.ListView):
    """
    Display a list of courses sorted by total enrollment.
    """
    template_name = 'onlinecourse/course_list.html'
    context_object_name = 'course_list'

    def get_queryset(self):
        """
        Get the queryset of courses sorted by total enrollment.
        """
        return Course.objects.order_by('-total_enrollment')[:10]


class CourseDetailsView(generic.DetailView):
    """
    Display details of a specific course.
    """
    model = Course
    template_name = 'onlinecourse/course_detail.html'


# Class-based views

class EnrollView(View):
    """
    Handle course enrollment.
    """
    def post(self, request, *args, **kwargs):
        """
        Handle POST request for course enrollment.
        """
        course_id = kwargs.get('pk')
        course = get_object_or_404(Course, pk=course_id)
        course.total_enrollment += 1
        course.save()
        return HttpResponseRedirect(reverse(viewname='onlinecourse:course_details', args=(course.id,)))

# Function-based views

# The function-based views are commented out below for reference.
# These were likely replaced by the class-based views above.

# Function-based course list view
# def popular_course_list(request):
#     """
#     Display a list of courses sorted by total enrollment.
#     """
#     context = {}
#     if request.method == 'GET':
#         course_list = Course.objects.order_by('-total_enrollment')[:10]
#         context['course_list'] = course_list
#         return render(request, 'onlinecourse/course_list_no_css.html', context)

# Function-based course_details view
# def course_details(request, course_id):
#     """
#     Display details of a specific course.
#     """
#     context = {}
#     if request.method == 'GET':
#         try:
#             course = Course.objects.get(pk=course_id)
#             context['course'] = course
#             return render(request, 'onlinecourse/course_detail.html', context)
#         except Course.DoesNotExist:
#             raise Http404("No course matches the given id.")

# Function-based enroll view
# def enroll(request, course_id):
#     """
#     Handle course enrollment.
#     """
#     if request.method == 'POST':
#         course = get_object_or_404(Course, pk=course_id)
#         course.total_enrollment += 1
#         course.save()
#         return HttpResponseRedirect(reverse(viewname='onlinecourse:course_details', args=(course.id,)))