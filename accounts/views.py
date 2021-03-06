import json
from operator import itemgetter

from django.db.models import Sum
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

from .models import HostRiskRating, SecurityRiskOrigin, SecurityBrowsers


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


def risk_rating_chart(request):
    dataset = HostRiskRating.objects.values().all()

    os_categories = list(set([k['os_name'] for k in dataset]))
    risk_incidents = [{k['risk_lvl']: k['nr_incidents']} for k in dataset]
    # Create list of dicts with risk_incidents['risk_lvl'] as the new key
    # and risk['nr_incidents'] as the value
    series_data = [{k: [d.get(k) for d in risk_incidents if d.get(k) is not None]} for k in
                   set().union(*risk_incidents)]  # return the keys from each dict
    # Prepare data for Highcharts
    series_data = [{'name': r, 'data': n} for d in series_data for r, n in d.items()]

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

    return dump


def risk_origin_chart(request):
    # Acquire total number of incidents
    # Used for calculating the percent value
    total_incidents = SecurityRiskOrigin.objects.aggregate(total_incidents=Sum('nr_incidents'))
    dataset = SecurityRiskOrigin.objects.values().all()

    risk_origin = [{k['risk_name']: k['nr_incidents']} for k in dataset]
    # Calculate the percent value for y key and round it to 2 decimals
    # Prepare data for Highcharts
    series_data = [{'name': rn, 'y': round((n / total_incidents['total_incidents']) * 100, 2)} for d in risk_origin
                   for rn, n in d.items()]

    chart = {
        'chart': {
            'plotBackgroundColor': None,
            'plotBorderWidth': None,
            'plotShadow': False,
            'type': 'pie'
        },
        'title': {
            'text': 'Security Risk Origin'
        },
        'tooltip': {
            'pointFormat': '{series.name}: <b>{point.percentage:.1f}%</b>'
        },
        'accessibility': {
            'point': {
                'valueSuffix': '%'
            }
        },
        'plotOptions': {
            'pie': {
                'allowPointSelect': True,
                'cursor': 'pointer',
                'dataLabels': {
                    'enabled': True,
                    'format': '<b>{point.name}</b>: {point.percentage:.1f} %'
                }
            }
        },
        'series': [{
            'name': 'Category',
            'colorByPoint': True,
            'data': series_data
        }]
    }

    dump = json.dumps(chart)

    return dump


def browser_security_chart(request):
    dataset = SecurityBrowsers.objects.values().all()

    browser_dict = [{k['browser_name']: k['market_trust']} for k in dataset]
    # Convert to list of lists for Highcharts
    browser_list = [[ln, lnr] for d in browser_dict for ln, lnr in d.items()]
    # Sort in reverse order
    # Prepare data for Highcharts
    data_list = sorted(browser_list, key=itemgetter(1), reverse=True)

    chart = {
        'chart': {
            'plotBackgroundColor': None,
            'plotBorderWidth': 0,
            'plotShadow': False
        },
        'title': {
            'text': 'Most<br>secure<br>browsers',
            'align': 'center',
            'verticalAlign': 'middle',
            'y': 60
        },
        'tooltip': {
            'pointFormat': '{series.name}: <b>{point.percentage:.1f}%</b>'
        },
        'accessibility': {
            'point': {
                'valueSuffix': '%'
            }
        },
        'plotOptions': {
            'pie': {
                'dataLabels': {
                    'enabled': True,
                    'distance': -50,
                    'style': {
                        'fontWeight': 'bold',
                        'color': 'white'
                    }
                },
                'startAngle': -90,
                'endAngle': 90,
                'center': ['50%', '75%'],
                'size': '110%'
            }
        },
        'series': [{
            'type': 'pie',
            'name': 'Market trust',
            'innerSize': '50%',
            'data': data_list
        }]
    }
    dump = json.dumps(chart)
    return dump


def vm_charts(request):
    chart_risk = risk_rating_chart(request)
    chart_origin = risk_origin_chart(request)
    chart_secure = browser_security_chart(request)

    return render(request, 'charts.html',
                  {'chart_risk': chart_risk, 'chart_origin': chart_origin, 'chart_secure': chart_secure})
