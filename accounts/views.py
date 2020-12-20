import json
from django.db.models import Count, Q
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

from .models import HostRiskRating


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


def RiskRatingChart(request):
    dataset = HostRiskRating.objects.values().all()

    os_categories = list(set([k['os_name'] for k in dataset]))
    risk_incidents = [{k['risk_lvl']: k['nr_incidents']} for k in dataset]
    series_data = [{k: [d.get(k) for d in risk_incidents if d.get(k) is not None]} for k in
                   set().union(*risk_incidents)]

    chart = {
        'chart': {'type': 'bar'},
        'title': {'text': 'Host Risk Rating'},
        'xAxis': {'categories': os_categories},
        'yAxis': {'min': 0,
                  'title': {
                      'text': 'Total number of incidents reported'
                  }
                  },
        'legend': {'reversed': True},
        'plotOptions': {
            'series': {
                'stacking': 'normal'
            }
        },
        'series': series_data
    }

    dump = json.dumps(chart)
    print(chart)

    return render(request, 'home.html', {'chart': dump})
