from django.urls import path
from . import views
from .views import (
    candidate_list, add_candidate, add_mentor, mark_contacted,
    assign_mentor, edit_candidate, mentor_list, edit_mentor, delete_forever, statistics_view, action_history,
    mark_status, candidate_detail,

)

urlpatterns = [
    path('', candidate_list, name='candidate_list'),
    path('add_candidate/', add_candidate, name='add_candidate'),
    path('add_mentor/', add_mentor, name='add_mentor'),
    path('mark_contacted/<int:candidate_id>/', mark_contacted, name='mark_contacted'),
    path('assign_mentor/<int:candidate_id>/', assign_mentor, name='assign_mentor'),
    path('edit_candidate/<int:candidate_id>/', edit_candidate, name='edit_candidate'),
    path('mentors/', mentor_list, name='mentor_list'),
    path('edit_mentor/<int:mentor_id>/', edit_mentor, name='edit_mentor'),
    path('delete/<str:model_name>/<int:user_id>/', delete_forever, name='delete_permanently'),
    path('statistics/', statistics_view, name='statistics'),
    path('action_history/', action_history, name='action_history'),
    path('mark_status/<int:candidate_id>/<str:status>/', mark_status, name='mark_status'),
    path('candidate/<int:candidate_id>/', candidate_detail, name='candidate_detail'),


]
