# teams/views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import TeamForm

@csrf_exempt
def create_team(request):
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            team = form.save(commit=False)
            team.created_by = request.user
            team.save()
            return JsonResponse({'success': True, 'team': {'name': team.name, 'description': team.description}})
        else:
            return JsonResponse({'success': False, 'errors': form.errors}, status=400)
