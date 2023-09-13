import re

def shortest_time(time_list):

    times = []
    for i,t in enumerate(time_list):
        exp = re.search(r'(\d+)\s*hr\s*(\d+)\s*min|(\d+)\s*hr|(\d+)\s*min', t)
        times.append(0)
        if(exp.group(1) is not None):
            times[i] += (int(exp.group(1)) * 60)
        if(exp.group(2) is not None):
            times[i] += (int(exp.group(2)))
        if(exp.group(3) is not None):
            times[i] += (int(exp.group(3)) * 60)
        if(exp.group(4) is not None):
            times[i] += (int(exp.group(4)))

    shortest_time =  (6000, 0)
    for i,time in enumerate(times):
        if(time < shortest_time[0]):
            shortest_time = (time, i)
    return time_list[shortest_time[1]]

deez = '2 hr 5 min', '12 hr 8 min', '3 hr 24 min', '16 hr 45 min', '4 hr', '11 hr', '50 min', '9 min'

print(shortest_time(deez))