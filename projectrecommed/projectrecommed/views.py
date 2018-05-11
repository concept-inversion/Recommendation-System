from django.shortcuts import render
from django.views.generic.base import TemplateView
import pandas as pd

def home(request):
    return render(request, 'home.html')

class RecommendView(TemplateView):
    template_name = 'detail.html'

    # def get_context_data(self, *args, **kwargs):
    #     req_list = ['Experience', 'php', 'python', 'qa', 'js', 'level', 'qualification', 'age', 'Jobid']
    #     user_data_dict = self.request.GET
    #     import ipdb; ipdb.set_trace()
    #     user_data = {req_item : user_data_dict.get(req_item)[0] for req_item in req_list }

    def get(self, *args, **kwargs):
        # req_list = ['Experience', 'php', 'python', 'qa', 'js', 'level', 'qualification', 'age',]
        user_data_order_dict = self.request.GET
        user_dict = {k :v[0] for k,v in dict(user_data_order_dict).items()}
        pd_dataframe = pd.DataFrame.from_dict(user_dict)