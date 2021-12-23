import pandas as pd
import csv
import plotly.figure_factory as ff
import statistics
import random
import plotly.graph_objects as go

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].to_list()
p_mean = statistics.mean(data)
print("Population mean",p_mean)
pstd = statistics.stdev(data)
print("Population Std_dev",pstd)
def random_set_of_mean(counter):
    dataset = []
    for i in range(0,counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    std_dev = statistics.stdev(dataset)
    #print("Mean = ",mean)
    #print("Standard deviation = ",std_dev)
    return mean


    

def setup():
    mean_list = []
    for i in range(0,100):
        set = random_set_of_mean(30)
        mean_list.append(set)
    
    df = mean_list
    fig = ff.create_distplot([df],["Reading time"], show_hist=False)
    fig.show()
    
    mean = statistics.mean(mean_list)
    print(mean)
    std = statistics.stdev(mean_list)
    print("Std_dev",std)


    first_std_dev_start,first_std_dev_end = p_mean-pstd,p_mean+pstd
    second_std_dev_start,second_std_dev_end = p_mean-(2*pstd),p_mean+(2*pstd)
    third_std_dev_start,third_std_dev_end = p_mean-(3*pstd),p_mean+(3*pstd)

#fig = ff.create_distplot([dice_result],["Result"],show_hist=False)
    fig.add_trace(go.Scatter(x = [mean,mean], y = [0,0.17], mode = "lines", name = "MEAN"))
    z_score = (p_mean-mean)/pstd

setup()

