from itertools import chain
from django import template

register = template.Library()

# a = [{'Experience': 0, 'php': 0, 'python': 0, 'qa': 0, 'js': 1, 'level': 1, 'qualification': 1, 'company': 'Yomari', 'jobtitle': 'Web developer trainee', 'Jobid': 23, 'similarity': 0.9727701243282773}, ]

def data_unquantification(ls):

    job_qualification = ['+2', 'Bachelors', 'Masters']
    job_level = ['Entry Level', 'Mid Level', 'Senior Level', 'Top Level']

    # retrieve job id title and company from list
    job_id_title_company = ls[:3]

    # not required if experience 0 else experience
    experience = ['Not Required' if not ls[3] else f'{ls[3]} Years']

    # yes if skill has value 1 else no
    skills = ['Yes' if i==1 else 'No' for i in ls[4:8]]

    # not required if level 0 else level -1 to retrieve value using job_level list
    level = ['Not Required' if not ls[8] else f'{job_level[ls[8]-1]}']

    # not required if qualification is 0 else qualification -1 to retrieve value using job_qualification list
    qualification = ['Not Required' if not ls[9] else f'{job_qualification[ls[9]-1]}']

    # get similarity from list
    similarity = [ls[-1]]

    return list(chain(job_id_title_company, experience, skills, level, qualification, similarity))




@register.inclusion_tag('dict_table.html')
def order_items(data):
    reorder = [9, 8, 7, 0, 1, 2, 3, 4, 5, 6, 10]
    ls = [list(job_data.values()) for job_data in data]
    ordered_list = [[item[i] for i in reorder] for item in ls]
    final_data = [data_unquantification(item) for item in ordered_list]
    return {'data': final_data}