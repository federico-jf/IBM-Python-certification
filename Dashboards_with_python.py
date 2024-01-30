
#import libraries
import piplite
import pandas as pd
import numpy as np
import plotly.express as px
import plortly.graph_objects as go

#scaterplot
fig=go.Figure()
fig.add_trace(go.Scatter(x=data['Distance'], y=data['DepTime'], mode = 'markers', marker=dict(color='blue')))
fig.update_layout(title='Distance vs Departure Time', xaxis_title='Distance', yaxis_title='DepTime')
fig.show()

#lineplot
fig=go.Figure()
fig.add_trace(go.Scatter(x=line_data['Month'], y=line_data['ArrDelay'], mode = 'lines', marker=dict(color='red')))
fig.update_layout(title='Month vs Average Flight Delay Time', xaxis_title='Month', yaxis_title='ArrDelay')
fig.show()

#Barchart
fig=px.bar(bar_data, x="DestState", y="Flights", title='Total number of flights to the destination state split by reporting airline')
fig.show()

#Histogram
fig=px.histogram(data, x="ArrDelay", title='Total number of flights to the destination state split by reporting airline')
fig.show()

#bublue chart
fig=px.scatter(bub_data, x="Reporting_Airline", y="Flights", size="Flights", hover_name="Reporting_Airline", title='Reporting Airline vs Number of Flights', size_max=60)
fig.show()

#PIE chart
fig=px.pie(data, values='Flights', names='DistanceGroup', title='Flight proportion by Distance Group')
fig.show()

#PIE chart
fig=px.sunburst(data, path=['Month', 'DestStateName'], values='Flights', title='Flight Distribution Hierarchy')
fig.show()
