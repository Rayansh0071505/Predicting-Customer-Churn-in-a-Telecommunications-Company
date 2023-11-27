import matplotlib.pyplot as plt
import pandas as pd


def circle_draw(data_series,title):
    counts = data_series.value_counts()
    explode = [0.01] * len(data_series.unique())


    counts.plot(kind='pie', autopct='%1.1f%%', startangle=90,explode=explode);
    plt.axis('equal')
    plt.legend(counts.index, loc='center left', bbox_to_anchor=(1, 0.5))

    plt.title(title);

def circle_analysis(sizes,title,labels):
    # colors = ['#ff9999', '#66b3ff']  # Red and blue colors
    # Labels for the pie chart
    
    explode = [0.01] * len(sizes)

    plt.figure(figsize=(6, 6))
    plt.pie(sizes, labels=labels,autopct='%1.1f%%', startangle=90,explode=explode)
    # plt.legend(counts.index, loc='center left', bbox_to_anchor=(1, 0.5))

    plt.title(title)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.show()


def bar_plot(data_series,xlabel,ylabel,title,colors):
    data_series = data_series.value_counts()
   
    ax = data_series.plot(kind='bar',rot=0,color=colors)

    for i, count in enumerate(data_series):
        plt.text(i, count - 10, str(count), ha='center', va='bottom', fontsize=12)
    
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()