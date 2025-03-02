from django.urls import path
from .views import ClientCourseProgressView
from .views import ClientIsAdminView
from .views import CourseListView
from .views import ClientListView
from .views import CurrentCourseCreateView
from .views import CurrentCourseDeleteView
from .views import CourseDeleteView
from .views import CourseCreateView
from .views import ModuleCreateView
from .views import BlockCreateView
from .views import BlockTestCreateView
from .views import CourseModulesView
from .views import ModuleBlocksView
from .views import BlockQuestionsView

urlpatterns = [
    path('client/<int:client_id>/course-progress/', ClientCourseProgressView.as_view(), name='client-course-progress'),
    path('client/<int:client_id>/is-admin/', ClientIsAdminView.as_view(), name='client-is-admin'),
    path('courses/', CourseListView.as_view(), name='course-list'),
    path('clients/', ClientListView.as_view(), name='client-list'),
    path('current-course/create/', CurrentCourseCreateView.as_view(), name='current-course-create'),
    path('current-course/delete/', CurrentCourseDeleteView.as_view(), name='current-course-delete'),
    path('course/delete/<int:course_id>/', CourseDeleteView.as_view(), name='course-delete'),
    path('course/create/', CourseCreateView.as_view(), name='course-create'),
    path('module/create/', ModuleCreateView.as_view(), name='module-create'),
    path('block/create/', BlockCreateView.as_view(), name='block-create'),
    path('block/<int:block_id>/test/create/', BlockTestCreateView.as_view(), name='block-test-create'),
    path('course/<int:course_id>/modules/', CourseModulesView.as_view(), name='course-modules'),
    path('module/<int:module_id>/blocks/', ModuleBlocksView.as_view(), name='module-blocks'),
    path('block/<int:block_id>/questions/', BlockQuestionsView.as_view(), name='block-questions'),
]