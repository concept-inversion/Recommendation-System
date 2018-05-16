from django.shortcuts import render
from django.views.generic.base import TemplateView
import pandas as pd
from src.Recommend import Recommend
from django.http import JsonResponse, HttpResponse
import json

def home(request):
    return render(request, 'home.1.html')


class RecommendView(TemplateView):
    template_name = 'detail.html'
 
    def get(self, *args, **kwargs):

        user_data_order_dict = dict(self.request.GET)

        category = user_data_order_dict.pop('category')[0]

        user_dict = {
            k : 0 if not v[0] else self.quantify_age(int(v[0])) if k=='age' else int(v[0]) for k,v in dict(user_data_order_dict).items() if v[0]
        }

        # if not category == 'management':
        #     skill_set = ['php', 'python', 'qa', 'js']

        #     skill_dict = {k: user_dict.get(k, 0) for k in skill_set}

        #     final_dict = {**user_dict, **skill_dict}

        # change user dictionay to pandas dataframe
        pd_dataframe = pd.DataFrame.from_dict([user_dict])

        # get job from Recommend
        similar = Recommend(pd_dataframe,category)
        data= similar.getData()
        
        # retrive all data context data
        context = super().get_context_data()

        context['similar_jobs'] = data

        # import ipdb; ipdb.set_trace()
        return render(self.request, self.template_name, context)
        # return JsonResponse(json.dumps('heheh'), safe=False)
    
    def quantify_age(self, age):
        return 1 if age > 40 else 2 if age > 35 else 3 if age > 30 else 4 if age > 25 else 5


    
def quantify_age(age):
    return 1 if age > 40 else 2 if age > 35 else 3 if age > 30 else 4 if age > 25 else 5


def reco(request):
    if request.method == 'GET':
        user_data_order_dict = dict(request.GET)

        category = user_data_order_dict.pop('category')[0]

        user_dict = {
            k : 0 if not v[0] else quantify_age(int(v[0])) if k=='age' else int(v[0]) for k,v in dict(user_data_order_dict).items() if v[0]
        }

        # if not category == 'management':
        #     skill_set = ['php', 'python', 'qa', 'js']

        #     skill_dict = {k: user_dict.get(k, 0) for k in skill_set}

        #     final_dict = {**user_dict, **skill_dict}

        # change user dictionay to pandas dataframe
        pd_dataframe = pd.DataFrame.from_dict([user_dict])

        # get job from Recommend
        similar = Recommend(pd_dataframe,category)
        data= similar.getData()
        
        new_data = json.dumps(data, default=str)
        # retrive all data context data
        # import ipdb; ipdb.set_trace()
        # return JsonResponse(json.dumps('heheh'), safe=False)
        return JsonResponse(new_data, safe=False)
        