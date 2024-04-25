def transform_real_time_data(response_text):
    data = {}
    lines = response_text.strip().split('\n')
    usergroups = lines[0].split('|')
    values = lines[1].split('|')
    result = {usergroups[i]: values[i] for i in range(len(usergroups))}
    return result

def transform_list_report(response_text):
    data = {}
    lines = response_text.strip().split('\n')
    usergroups = lines[0].split('|')
    values = lines[1].split('|')
    result = {usergroups[i]: values[i] for i in range(len(usergroups))}
    return result

def transform_logged_agents(response_text):
    lines = response_text.strip().split('\n')
    headers = lines[0].split(',')
    result = []

    for line in lines[1:]:
        values = line.split(',')
        agent_info = {headers[i]: values[i] for i in range(len(headers))}
        result.append(agent_info)
    
    return result
    
def transform_agent_stat_report(response_text):
    display_names = {
        'user': 'User',
        'full_name': 'Full Name',
        'user_group': 'User Group',
        'calls': 'Calls',
        'login_time': 'Login Time',
        'total_talk_time': 'Total Talk Time',
        'avg_talk_time': 'Average Talk Time',
        'sessions': 'Sessions',
        'pauses': 'Pauses'
    }

    ordered_keys = [
        'user',
        'full_name',
        'user_group',
        'calls',
        'login_time',
        'total_talk_time',
        'avg_talk_time',
        'sessions',
        'pauses'
    ]

    data = {}
    lines = response_text.strip().split('\n')
    usergroups = lines[0].split('|')
    values = lines[1].split('|')
    result = {display_names.get(usergroups[i], usergroups[i]): values[i] for i in range(len(usergroups)) if usergroups[i] in display_names}
    print(result)
    # print(f"Result : {result}")
    return result
