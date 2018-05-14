from django.shortcuts import render
from django.views.generic.base import TemplateView
import pandas as pd
from src.Recommend import Recommend


def home(request):
    return render(request, 'home.html')


class RecommendView(TemplateView):
    template_name = 'detail.html'

    def get(self, *args, **kwargs):
        user_data_order_dict = self.request.GET

        user_dict = {
            k :self.quantify_age(int(v[0])) if k=='age' else int(v[0]) for k,v in dict(user_data_order_dict).items() if v[0]
        }

        # change user dictionay to pandas dataframe
        pd_dataframe = pd.DataFrame.from_dict([user_dict])
        
        # get job from Recommend
        similar = Recommend(pd_dataframe)
        data= similar.getData()
        
        # retrive all data context data
        context = super().get_context_data()

        context['similar_jobs'] = data

        return render(self.request, self.template_name, context)
    
    def quantify_age(self, age):
        return 1 if age > 40 else 2 if age > 35 else 3 if age > 30 else 4 if age > 25 else 5
