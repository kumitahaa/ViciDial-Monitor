import requests
import warnings

# Ignore InsecureRequestWarning globally
warnings.filterwarnings("ignore", message="Unverified HTTPS request.*")


host = "https://dialer171.voiptech.cc"
user = "inteltech"
password = "0ldsai10r"
user_group = "IntelTech"
date_start = "2024-04-16"
date_end = "2024-04-19"

def fetch_real_time_data():
    url = f"{host}/vicidial/non_agent_api.php?source=test&user={user}&pass={password}&function=user_group_status&user_groups={user_group}&header=YES"
    response = requests.get(url, verify=False)
    if "ERROR" not in response.text:
        data = {}
        lines = response.text.strip().split('\n')
        usergroups = lines[0].split('|')
        values = lines[1].split('|')
        result = {usergroups[i]: values[i] for i in range(len(usergroups))}

        
        print(result)
        return result
    else:
        print(f'error: Failed to fetch data from API')
        return {'error': f'Failed to fetch data from API'}


def fetch_list_report(list_id):
    url = f"{host}/vicidial/non_agent_api.php?source=test&user={user}&pass={password}&function=list_info&list_id={list_id}&leads_counts=Y&header=YES"
    print(url)
    response = requests.get(url, verify=False)
    print(response.text)
    if "ERROR" not in response.text:
        data = {}
        lines = response.text.strip().split('\n')
        usergroups = lines[0].split('|')
        values = lines[1].split('|')
        result = {usergroups[i]: values[i] for i in range(len(usergroups))}
        print(result)
        return result
    else:
        print(f'error: Failed to fetch data from API')
        return {'error': f'Failed to fetch data from API'}

def fetch_logged_agents():
    url = f"{host}/vicidial/non_agent_api.php?source=test&user={user}&pass={password}&function=logged_in_agents&stage=csv&header=YES"
    response = requests.get(url, verify=False)
    if "ERROR" not in response.text:
        lines = response.text.strip().split('\n')
        headers = lines[0].split(',')
        result = []

        for line in lines[1:]:
            values = line.split(',')
            agent_info = {headers[i]: values[i] for i in range(len(headers))}
            result.append(agent_info)
        
        print(result)
        return result
    else:
        print(f'error: Failed to fetch data from API')
        return {'error': f'Failed to fetch data from API'}


def fetch_agent_stat_report(agent_id,a,b):
    if agent_id == "00000":
        url = f"{host}/vicidial/non_agent_api.php?DB=0&stage=pipe&user={user}&pass={password}&source=test&function=agent_stats_export&datetime_start={a}+00:00:00&datetime_end={b}+23:59:59&header=YES"
    else:
        url = f"{host}/vicidial/non_agent_api.php?source=test&function=agent_stats_export&time_format=M&stage=pipe&user={user}&pass={password}&agent_user={agent_id}&datetime_start={a}+00:00:00&datetime_end={b}+23:59:59&header=YES"
    response = requests.get(url, verify=False)
    if "ERROR" not in response.text:
        data = {}
        lines = response.text.strip().split('\n')
        usergroups = lines[0].split('|')
        values = lines[1].split('|')
        result = {usergroups[i]: values[i] for i in range(len(usergroups))}
        print(result)
        return result
    else:
        return {'error': f'Failed to fetch data from API'}
