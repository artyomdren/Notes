from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView
from .models import NoteModel
from .forms import NoteForm


# Create your views here.

def notice(request):
    notes = NoteModel.objects.all()
    context = {
        'message': notes,
    }
    return render(request, 'note/note-list.html', context=context)


class NoteCreateView(CreateView):
    model = NoteModel
    fields = "head", "memo"
    success_url = reverse_lazy("note:notice")
    template_name = 'note/note-create.html'


class NoteDeleteView(DeleteView):
    model = NoteModel
    success_url = reverse_lazy("note:notice")
    template_name = 'note/note-delete.html'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return HttpResponseRedirect(self.get_success_url())


class NoteDetailsView(DetailView):
    model = NoteModel
    template_name = "note/note-details.html"
    context_object_name = "message"


class NoteUpdateView(UpdateView):
    model = NoteModel
    template_name_suffix = "_update_form"
    form_class = NoteForm
    template_name = "note/note-update.html"

    def get_success_url(self):
        return reverse(
            "note:note_details",
            kwargs={"pk": self.object.pk},
        )