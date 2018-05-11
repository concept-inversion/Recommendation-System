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

        # change ordered dict to dict
        user_dict = {k :int(v[0]) for k,v in dict(user_data_order_dict).items()}

        # change user dictionay to pandas dataframe
        pd_dataframe = pd.DataFrame.from_dict([user_dict])
        
        # get job from Recommend
        similar = Recommend(pd_dataframe)
        data= similar.getData()
        
        # retrive all data context data
        context = super().get_context_data()

        # context['similar_jobs']
        return self.render_to_response(context)
    



columns = ['Experience', 'php', 'python', 'qa', 'js', 'level', 'qualification', 'age',]
dictr = {'php': 1, 'python': 1, 'qualification': 2, 'experience': 5,'level': 2, 'age': 25}
frame = pd.DataFrame.from_dict([dictr])
