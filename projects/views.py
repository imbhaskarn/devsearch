from django.shortcuts import render 



projectList = [
    {
        'id': '1',
        "title": 'Ecommerce Website',
        "description": "This is fully functional ecommerce website."
    },
    {
        'id': '2',
        "title": 'Portfolio Website',
        "description": "This is fully functional portfolio website."
    },
    {
        'id': '3',
        "title": 'Socila Media Website',
        "description": "This is fully functional Social Media website."
    }
]

def projects(request):
    context = {'projects': projectList}
    
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    return render(request, 'projects/single-project.html', )