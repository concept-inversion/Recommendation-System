from itertools import chain
from django import template
from operator import itemgetter

register = template.Library()

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

    # reorder values to display
    reorder = [9, 8, 7, 0, 1, 2, 3, 4, 5, 6, 10]

    # create list of tuples of keys and values
    lat_ls = [list(zip(job.keys(), job.values())) for job in data]
        
    # order value with respect to reorder list
    ordered_list = [[item[i] for i in reorder] for item in lat_ls]

    # get keys
    key_list = [ list(map(lambda x: x[0], k)) for k in ordered_list ][0]

    # get values
    value_list = [ list(map(lambda x: x[1], v)) for v in ordered_list ]

    # unquantify values
    final_data = [data_unquantification(item) for item in value_list]

    # unquantify datas
    # final_data = [data_unquantification(item) for item in ordered_list]
    # combine = [ list(zip(k, v)) for k,v in(key_list,value_list) ]
    # sort data on basis of similarity which is last item in list 
    return { 'keys': key_list,
        'values': sorted(final_data, key=itemgetter(-1), reverse=True)
    }
