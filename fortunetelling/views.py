from django.shortcuts import render
from django.views.generic.base import View

import random


class FortuneTelling(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'fortunetelling/fortunetelling.html')

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        random.seed(name)
        random_value = random.randint(0, 120)
        context = {
            'name': name,
            'value': random_value,
        }
        if random_value == 0:
            return render(request, 'fortunetelling/min.html', context)
        elif random_value == 120:
            return render(request, 'fortunetelling/max.html', context)
        else:
            return render(request, 'fortunetelling/result.html', context)
