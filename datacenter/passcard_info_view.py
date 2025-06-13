from datacenter.models import Passcard
from datacenter.models import Visit
from  datacenter.models import get_duration, format_duration, is_visit_long
from django.shortcuts import render, get_object_or_404


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    employee_visits = Visit.objects.filter(passcard=passcard)
    this_passcard_visits = []
    for visit in employee_visits:
        visit_data = {}
        duration = get_duration(visit)
        visit_data['entered_at'] = visit.entered_at
        visit_data['duration'] = format_duration(duration)
        visit_data['is_strange'] = is_visit_long(duration)
        this_passcard_visits.append(visit_data)

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
