from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

# Define the namespace for the app
app_name = 'onlinecourse'

# Define the urlpatterns for the app
urlpatterns = [
    # Define the URL pattern for enrolling in a course, specifying the primary key (pk) of the course
    # Note that for the view argument, we actually added the as_view() method for CourseListView class.
    path(route='course/<int:pk>/enroll/', view=views.EnrollView.as_view(), name='enroll'),
    # Define the URL pattern for the popular course list view
    path(route='', view=views.CourseListView.as_view(), name='popular_course_list'),
    # Define the URL pattern for viewing course details, specifying the primary key (pk) of the course
    path(route='course/<int:pk>/', view=views.CourseDetailsView.as_view(), name='course_details'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)