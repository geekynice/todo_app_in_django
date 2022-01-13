from django.shortcuts import redirect, render

from notes_app.models import Notes

# Create your views here.

def index(request):
    notes = Notes.objects.all()
    return render(request, 'notes_app/index.html', {'notes' : notes})

def delete(request, id):
    note = Notes.objects.get(id=id)
    note.delete()
    return redirect('index')

def add(request):
    if request.method == 'GET':
        return render(request, 'notes_app/add.html') 
    else:
        title = request.POST['title']
        description = request.POST['description']

        Notes.objects.create(title=title, description=description)

        return redirect('index')

def edit(request, id):
    note = Notes.objects.get(id=id)
    if request.method == 'GET':
        return render(request, 'notes_app/edit.html', {'note' : note} )
    else:
        note.title = request.POST['title']
        note.description = request.POST['description']
        note.save()
        
        return redirect('index', permanent=True)

def mark_complete(request, id):
    note = Notes.objects.get(id=id)
    note.is_completed = not note.is_completed
    note.save()

    return redirect('index')