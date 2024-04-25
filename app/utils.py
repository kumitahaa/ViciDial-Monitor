import requests
import warnings
from app.transformer import transform_real_time_data, transform_list_report, transform_logged_agents, transform_agent_stat_report

# Ignore InsecureRequestWarning globally
warnings.filterwarnings("ignore", message="Unverified HTTPS request.*")

host = "http://appelercom.i5.tel/"
user = "Aappelercom_Admin"
password = "Aappelercom_Admin"
user_group = "appelercom"
date_start = "2024-04-16"
date_end = "2024-04-19"

def fetch_real_time_data():
    url = f"{host}/vicidial/non_agent_api.php?source=test&user={user}&pass={password}&function=user_group_status&user_groups={user_group}&header=YES"
    response = requests.get(url, verify=False)
    if "ERROR" not in response.text:
        return transform_real_time_data(response.text)
    else:
        print(f'error: Failed to fetch data from API')
        return {'error': f'Failed to fetch data from API'}

def fetch_list_report(list_id):
    url = f"{host}/vicidial/non_agent_api.php?source=test&user={user}&pass={password}&function=list_info&list_id={list_id}&leads_counts=Y&header=YES"
    response = requests.get(url, verify=False)
    if "ERROR" not in response.text:
        return transform_list_report(response.text)
    else:
        print(f'error: Failed to fetch data from API')
        return {'error': f'Failed to fetch data from API'}

def fetch_logged_agents():
    url = f"{host}/vicidial/non_agent_api.php?source=test&user={user}&pass={password}&function=logged_in_agents&stage=csv&header=YES"
    response = requests.get(url, verify=False)
    if "ERROR" not in response.text:
        return transform_logged_agents(response.text)
    else:
        print(f'error: Failed to fetch data from API')
        return {'error': f'Failed to fetch data from API'}

def fetch_agent_stat_report(agent_id, a, b):
    if agent_id == "00000":
        url = f"{host}/vicidial/non_agent_api.php?DB=0&stage=pipe&user={user}&pass={password}&source=test&function=agent_stats_export&datetime_start={a}+00:00:00&datetime_end={b}+23:59:59&header=YES"
    else:
        url = f"{host}/vicidial/non_agent_api.php?source=test&function=agent_stats_export&time_format=M&stage=pipe&user={user}&pass={password}&agent_user={agent_id}&datetime_start={a}+00:00:00&datetime_end={b}+23:59:59&header=YES"
    response = requests.get(url, verify=False)
    if "ERROR" not in response.text:
        result =  transform_agent_stat_report(response.text)
        # print(f"Result : {result}")
        return result
    else:
        return {'error': f'Failed to fetch data from API'}
