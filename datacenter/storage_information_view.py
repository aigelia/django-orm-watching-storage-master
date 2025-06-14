from datacenter.models import Visit
from datacenter.models import get_duration, format_duration
from django.shortcuts import render


def storage_information_view(request):
    visits = Visit.objects.filter(leaved_at=None)
    non_closed_visits = []
    for visit in visits:
        visit_data = {}
        duration = get_duration(visit)
        visit_data['who_entered'] = visit.passcard.owner_name
        visit_data['entered_at'] = visit.entered_at
        visit_data['duration'] = format_duration(duration)
        non_closed_visits.append(visit_data)

    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
