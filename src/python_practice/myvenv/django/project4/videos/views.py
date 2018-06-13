from django.urls import reverse_lazy
from django.views import generic
from .forms import VideoCreateForm
from .models import Video

class IndexView(generic.ListView):
    model = Video

class CreateView(generic.CreateVIew):
    model = Video
    form_class = VideoCreateForm
    success_url = reverse_lazt('videos:index')

class PlayVIew(generic.DetailView):
    model = Video
    