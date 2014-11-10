from nvd3 import *
from nvd3.multiBarChart import multiBarChart
import json


def plot_nvd3(data_json):
    """
    Uses data in json format to plot bar charts using D3.js
    """

    output_file = open('multiBarChart.html', 'w')
    type = "multiBarChart"

    chart = multiBarChart(name=type, height=400, width=800, x_is_date=False)

    xdata = [data[i]['SEM'] for i in range(39)]
    ydata = [data[i]['SEO'] for i in range(39)]

    extra_serie = {"tooltip": {"y_start": "", "y_end": " "}}
    chart.add_serie(y=ydata, x=xdata, extra=extra_serie, color='red')
    chart.buildhtml()
    output_file.write(chart.htmlcontent)
    output_file.close()


with open("data/sample_data_Oct.json") as json_file:
    data = json.load(json_file)

plot_nvd3(data)
