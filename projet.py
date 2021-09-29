import pandas as pd
import csv
import statistics
import plotly.figure_factory as ff
import random
import plotly.graph_objects as go

df = pd.read_csv('data.csv')
data = df["reading_time"].tolist()

mean = statistics.mean(data)
std_deviation = statistics.stdev(data)

print("Mean is " + str(mean))
print("Standard Deviation is " + str(std_deviation))


def meanOfRandomSet(counter):
    data_set = []
    for i in range(0,counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        data_set.append(value)

    mean_sample = statistics.mean(data_set)

    return mean_sample

def show_figure(mean_list): 
    df = mean_list
    mean = statistics.mean(df)
    fig = ff.create_distplot([df],["reading_time"], show_hist=False)
    fig.add_trace(go.Scatter(x= [mean,mean], y= [0,1],mode="lines",name="MEAN"))
    fig.show()

def setup():
    mean_list = []

    for i in range(0,1000):
        set_of_means = meanOfRandomSet(100)
        
        mean_list.append(set_of_means)
    
    
    standardDeviation_mean = statistics.stdev(mean_list)
    print("The standard dev of the means of samples is " + str(standardDeviation_mean))
    show_figure(mean_list)

setup()

