#Final Assignment
#Federico Ferrero
#2/5/2024

#1.1 line chart

df_line = df.groupby(df['Year'])['Automobile_Sales'].mean()

plt.figure(figsize=(10,6))
df_line.plot(kind='line')
plt.xticks(list(range(1980,2024)), rotation = 75)
plt.xlabel('Years')
plt.ylabel('Automobile Sales (mean)')
plt.title('Automoblie Sales during Recession')
plt.text(1982,650,'1981-82 Recession')
plt.text(1991,650,'1991 Recession')
plt.text(2007,650,'2007-2009 Recession')
plt.text(2020,650,'Covid-19 Impact')
plt.legend()
plt.show()




#1.2 Different lines

df_Mline = df.groupby(['Year', 'Vehicle_Type'], as_index=False)['Automobile_Sales'].sum()
df_Mline.set_index('Year', inplace=True)
df_Mline = df_Mline.groupby(['Vehicle_Type'])['Automobile_Sales']

df_Mline.plot(kind='line')
plt.xlabel('...')
plt.ylabel('....')
plt.title('Sales Trend Vehicle-wise during Recession')
plt.legend()
plt.show()

#1.3 compare sale trend per vehicle for a recession with a non-recession period

new_df = df.groupby('Recession')['Automobile_Sales'].mean().reset_index()

plt.figure(figsize=(10,6))
sns.barplot(x='Recession', y='Automobile_Sales', hue='Recession', data=new_df)
plt.xlabel('Years')
plt.ylabel('....')
plt.title('Average Automobile Sles Recession and Non-Recession')
plt.xticks(ticks=[0,1], labels=['Non-Recession', 'Recession'])
plt.show()

#another one

recession_data=df[df['Recession']==1]
dd=df.groupby(['Recession', 'Vehicle_Type'])['Automobile_Sales'].mean().reset_index()
sales_by_vehicle_type = recession_data.groupby('Vehicle_Type')['Automobile_Sales'].sum().reset_index()

plt.figure(figsize=(10,6))
sns.barplot(x='Recession', y='Automobile_Sales', hue='Vehicle_Type', data=dd)
plt.xticks(ticks=[0,1], labels=['Non-Recession', 'Recession'])
plt.xlabel('....')
plt.ylabel('....')
plt.title('Vehicle-Wise Sales during Recession and Non-Recession Period')

plt.show()

#1.4 subplotting

rec_data = df[df['Recession']==1]
non_rec_data = df[df['Recession']==0]

fig=plt.figure(figsize=(12,6))

ax0=fig.add_subplot(1,2,1)
ax1=fig.add_subplot(1,2,2)

sns.lineplot(x='Year', y='GDP', data=rec_data, label='Recession', ax=ax0)
ax0.set_xlabel('Year')
ax0.set_ylabel('GDP')
ax0.set_title('GDP Variation During Recession Period')


sns.lineplot(x='Year', y='GDP', data=non_rec_data, label='Recession', ax=ax1)
ax1.set_xlabel('Year')
ax1.set_ylabel('GDP')
ax1.set_title('GDP Variation During Non-Recession Period')

plt.tight_layout()
plt.show()

#1.5 bubble plot
non_rec_data = df[df['Recession']==0]

size=non_rec_data['Seasonality_Weight']

sns.scatterplot(data=non_rec_data, x='Month', y='Automobile_Sales', size=size, hue= 'Seasonality_Weight', legend=False)

plt.xlabel('Month')
plt.ylabel('Automobile Sales')
plt.title('Seasonality Impact on Automobile Sles')

plt.show()

#1.6 correlation in  a scatterplot


rec_data = df[df['Recession']==1]
plt.scatter(recession_data['Price'], rec_data['Automobile_Sales'])

plt.xlabel('Price')
plt.ylabel('Automobile Sales')
plt.title('Relationship between Average Vehicle Price and Sales during Recessions')

plt.show()

#1.7 chart pie

Rdata = df[df['Recession']==1]
NRdata = df[df['Recession']==0]

RAtotal = Rdata['Advertising_Expenditure'].sum()
NRtotal = NRdata['Advertising_Expenditure'].sum()

fig=plt.figure(figsize=(12,6))

labels = ['Recession', 'Non-Recession']
sizes = [RAtotal, NRtotal]
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title('Advertising Expenditures of XYZAutomotives during Recession and Non-Recession periods')
plt.show()

#1.8 pie hart 2


Rdata = df[df['Recession']==1]

VTsales = Rdata.groupby('Vehicle_Type')['Automobile_Sales'].sum()

plt.figure(figsize=(12,6))

labels = VTsales.index
sizes = VTsales.values
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title('Total Advertising Expenditures for each Vehicle Type during Recession periods')
plt.show()

#1.9  line plot

Rdata = df[df['Recession']==1]
sns.lineplot(data=Rdata, x='unemployment_rate', y='Automobile_Sales', hue='Vehicle_Type', style='Vehicle_Type', markers='+',err_style=None)

plt.figure(figsize=(12,6))
plt.ylabel(0,850)
plt.title('Effect of Unemployment Rate on Vehicle Type and Sales')
plt.legend(loc=(0.05,.3))
plt.show()



#10 create a map

recession_data=df[df['Recession']==1]
sales_by_city=recession_data.groupby('City')['Automobile_Sales'].sum().reset_index()
map1=folium.Map(location=[37.0902, -95.7129], zoom_start=4)

choropleth = folium.Choropleth(
	geo_data='us-states.json', 
	data=sales_by_city,
	columns=['City', 'Automobile_Sales'],
	key_on='feature.properties.name',
	fill_color='YlOrRd',
	fill_opacity=0.7,
	line_opacity= 0.2,
	legend_name='Automobile Sales during Recession',
).add_to(map1)

choropleth.geojson.add_child(
	folium.features.GeoJsonTooltip(['name'], labels=True)
)

map1
