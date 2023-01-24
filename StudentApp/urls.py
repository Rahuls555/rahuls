from django.urls import path
from . import views

urlpatterns = [
    path('',views.openIndexPage),
    path('save-students',views.savestudents),
    path('students-list',views.getAllstudents),
    path('students-form',views.openstudents),
    path('remove-students/<int:id>',views.removestudents),
    path('edit-students/<int:id>',views.editstudent),
    path('update-students/<int:id>',views.updatestudents)


]
