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

        # change ordered dict to dict and remove field with null value
        user_dict = {k :int(v[0]) for k,v in dict(user_data_order_dict).items() if v[0]}

        # change user dictionay to pandas dataframe
        pd_dataframe = pd.DataFrame.from_dict([user_dict])
        
        # get job from Recommend
        similar = Recommend(pd_dataframe)
        data= similar.getData()
        
        # retrive all data context data
        context = super().get_context_data()

        context['similar_jobs'] = data

        return render(self.request, self.template_name, context)
