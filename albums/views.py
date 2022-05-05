from django.shortcuts import render, redirect, get_object_or_404

import albums
from .models import Album
from .forms import AlbumForm
# Create your views here.
def list_albums(request):
    albums = Album.objects.all()
    return render(request, "albums/list_albums.html", {"albums": albums})

def album_detail(request, pk):
    contact = get_object_or_404(Album, pk=pk)
    # notes = Note.objects.filter(contact_id=contact.pk)
    form = AlbumForm()
    return render(request, "albums/album_detail.html", {"albums": albums })

def add_albums(request):
    if request.method == 'GET':
        form = AlbumForm()
    else:
        form = AlbumForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='list_albums')
            
    return render( request, "albums/add_album.html", {"form": form})

# def albums(request, pk):
#     contact = get_object_or_404(Album, pk=pk)
#     if request.method == 'GET':
#         form = AlbumForm()
#     else:
#         form = AlbumForm(data=request.POST)
#         if form.is_valid():
#             note = form.save(commit=False)
#             note.contact = contact
#             note.save()
#             return redirect(to='list_albums', pk=pk)
    