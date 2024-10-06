
from django.urls import path
from .views import (notice,
                    NoteCreateView,
                    NoteDeleteView,
                    NoteDetailsView,
                    NoteUpdateView
                    )


app_name = 'note'

urlpatterns = (
    path('', notice, name='notice'),
    path('create/', NoteCreateView.as_view(), name='note_create'),
    path('details/<int:pk>/', NoteDetailsView.as_view(), name='note_details'),
    path('delete/<int:pk>/', NoteDeleteView.as_view(), name='note_delete'),
    path('update/<int:pk>/', NoteUpdateView.as_view(), name='note_update'),
)
