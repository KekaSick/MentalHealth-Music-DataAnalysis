# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.16.0
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

import streamlit as st

# + [markdown] id="amXK4d3DMSqW"

st.title("A few words before code")

st.subheader('Data set - Music & Mental Health Survey Results')
st.write("I've decided to choose this dataset because music is a big part of my life. Every day I listen to my own and others play-lists, lo-fi and indie-rock radios and etc. Sometimes I even make my own riffs, melodies and rythms on the guitar in DAW.")
st.write("When i saw this dataset for the first time, I understood that it can be really interesting to find corellations between person's fav genre, age, fav platform and his mental health problems. How do musicians differ from non-musicians and etc. ")


# # Import libraries and show dataset (preparations before work)

# + colab={"base_uri": "https://localhost:8080/", "height": 694} id="jDaJIyV1JqU0" outputId="52107aec-6526-4967-c13f-b22e56aa233f"
import pandas as pd
from plotly.offline import plot
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# +
df = pd.read_csv('sample_data/mxmh_survey_results.csv') #read data

dfcop = df.copy(deep=True) #copy of dataset

#show df
st.dataframe(df.head())
# -

# # Cleaning

# + [markdown] id="scUKYGgfdVVB"
# #### Check data types in dataset
# Now we need to check if there is any damaged information in our dataset

# + colab={"base_uri": "https://localhost:8080/"} id="zp9YkcBZGxn1" outputId="4dc8801e-a7ed-46d8-e128-cd12b69be73e"
#we'll check our dataset for empty cells or NaN's or incorrect data
#as we can see there is only NaNs and no incorrect data
# -

# #### Work with NaN's
# I'll create two dataframes:
# with NaNs but changing them to 'NotStated' and without NaNs

# + id="6DmGkB1_yq5J"
#As you can see no NaNs
df = df.fillna('NotStated')

# + colab={"base_uri": "https://localhost:8080/"} id="dB1W-8hd123Y" outputId="a127f233-3d0f-4b35-c2ba-8495386969c9"
#that's all ellements what we have replaced with NotStated

# + colab={"base_uri": "https://localhost:8080/", "height": 694} id="K7uRbmrk53y5" outputId="73d549e2-6846-4cd7-ec6e-e6226519ae72"
#show df with NotStated
st.dataframe(df.head())
# -

#
# As you can see, I have replaced all the NaNs with str value = NotStated.
# And then i'll create dataframe without NaNs
#

dfcop = dfcop.dropna() #copy without nans and NotStated
st.dataframe(dfcop.head())

# + [markdown] id="nJVjJah46Ai5"
# # Now, when we've cleaned our dataset, we can start to analyze it
# -

# ## All people

# Here i'll check (Yes/No) information in my dataset. I think that this will be interesting. And i think that there is no need in analysis because it is obvious

# ### Check mean, median and standard deviation values for Mental health problems

# This shit was in criteria

# +
#mean
dfMentalMn = dfcop.loc[:,['Anxiety','OCD','Depression','Insomnia']]
dfMentalMn = dfMentalMn.assign(Sum=lambda x: x.OCD + x.Anxiety + x.Depression + x.Insomnia)
dfMentalMn = dfMentalMn.mean().round(2)

#Plot
fig = px.funnel(
    y=['Sum','Anxiety','Depression','Insomnia','OCD'],
    x=[dfMentalMn['Sum'],dfMentalMn['Anxiety'],dfMentalMn['Depression'],dfMentalMn['Insomnia'],dfMentalMn['OCD']],
    title = 'Mental Health problems<br>(Mean value)',
    template='simple_white'
)

fig.update_layout(
    yaxis_title=''
)

st.plotly_chart(fig, theme="streamlit", use_container_width=True)

#median
dfMentalMd = dfcop.loc[:,['Anxiety','OCD','Depression','Insomnia']]
dfMentalMd = dfMentalMd.assign(Sum=lambda x: x.OCD + x.Anxiety + x.Depression + x.Insomnia)
dfMentalMd = dfMentalMd.median()

#Plot
fig = px.funnel(
    y=['Sum','Anxiety','Depression','Insomnia','OCD'],
    x=[dfMentalMd['Sum'],dfMentalMd['Anxiety'],dfMentalMd['Depression'],dfMentalMd['Insomnia'],dfMentalMd['OCD']],
    title = 'Mental Health problems<br>(Median value)',
    template='simple_white'
)

fig.update_layout(
    yaxis_title=''
)

st.plotly_chart(fig, theme="streamlit", use_container_width=True)

#standart deviation
dfMentalSd = dfcop.loc[:,['Anxiety','OCD','Depression','Insomnia']]
dfMentalSd = dfMentalSd.assign(Sum=lambda x: x.OCD + x.Anxiety + x.Depression + x.Insomnia)
dfMentalSd = dfMentalSd.std().round(2)

#Plot
fig = px.funnel(
    y=['Anxiety','OCD','Depression','Insomnia','Sum'],
    x=[dfMentalSd['Anxiety'],dfMentalSd['OCD'],dfMentalSd['Depression'],dfMentalSd['Insomnia'],dfMentalSd['Sum']],
    title = 'Mental Health problems<br>(Standart deviation value)',
    template='simple_white'
)

fig.update_layout(
    yaxis_title=''
)

st.plotly_chart(fig, theme="streamlit", use_container_width=True)
# -

# ### Check binary data (Yes/No)
# Just information(no analysis)

# +
#Create new df with a new column 'Calc'
dfBoolean = dfcop.loc[:,['While working','Instrumentalist','Composer','Exploratory','Foreign languages']]
dfBoolean['Calc'] = 1

#Plot1
fig = px.treemap(
    dfBoolean, 
    path=['While working'],
    title='While working',
    values='Calc',
    color_discrete_sequence=[px.colors.qualitative.Plotly[0], px.colors.qualitative.Plotly[1]],
)
st.plotly_chart(fig, theme="streamlit", use_container_width=True)

#Plot2
fig = px.treemap(
    dfBoolean, 
    path=['Instrumentalist'],
    title='Instrumentalist',
    values='Calc',
    color_discrete_sequence=[px.colors.qualitative.Plotly[1], px.colors.qualitative.Plotly[0]]
)
st.plotly_chart(fig, theme="streamlit", use_container_width=True)

#Plot3
fig = px.treemap(
    dfBoolean, 
    path=['Composer'],
    title='Composer',
    values='Calc',
    color_discrete_sequence=[px.colors.qualitative.Plotly[1], px.colors.qualitative.Plotly[0]]
)
st.plotly_chart(fig, theme="streamlit", use_container_width=True)

#Plot4
fig = px.treemap(
    dfBoolean, 
    path=['Exploratory'],
    title='Exploratory',
    values='Calc',
    color_discrete_sequence=[px.colors.qualitative.Plotly[0], px.colors.qualitative.Plotly[1]]
)
st.plotly_chart(fig, theme="streamlit", use_container_width=True)

#Plot5
fig = px.treemap(
    dfBoolean, 
    path=['Foreign languages'],
    title='Foreign languages',
    values='Calc',
    color_discrete_sequence=[px.colors.qualitative.Plotly[0], px.colors.qualitative.Plotly[1]]
)
st.plotly_chart(fig, theme="streamlit", use_container_width=True)
# -

# ### Platform analyze

# #### Check the most popular platform and how much time people spend on different platforms

# My hypothesis that the most popular platform is Spotify because it is the most popular in the world.

# +
#Create a new groupedby df with a new column 'Calc' and then sort it by this column values
dfPopPlat = df.loc[:,['Primary streaming service']]
dfPopPlat['Calc']= 1 
dfPopPlat = dfPopPlat.groupby('Primary streaming service', as_index=False).sum().sort_values('Calc', ascending=False)

#Plot
fig = px.bar(
    dfPopPlat, 
    x='Primary streaming service',
    y='Calc', 
    color = 'Calc',
    title='The most popular platform',
    height=500,
    width=1000,
    template="simple_white"
)

st.plotly_chart(fig, theme="streamlit", use_container_width=True)
# -

# I was right

# Here i'll check the mean value of hours that people spend on music per day for different platforms

# + colab={"base_uri": "https://localhost:8080/", "height": 542} id="e5yBtLy0PI0R" outputId="c6f98ba6-cf9a-4bd3-8ccf-f136e911aa57"
#Create new df
dfHourPlat = dfcop.loc[:,['Primary streaming service','Hours per day']]

#Groupby and count mean value
dfHourMean = dfHourPlat.groupby("Primary streaming service", as_index = False).mean().round(2)

#Plot
fig = px.bar(
    dfHourMean, 
    y = 'Hours per day', 
    x = 'Primary streaming service', 
    text = 'Hours per day', 
    color = 'Primary streaming service', 
    title='Mean values of hours for each platform',
    height=500,
    width=1000,
    template="simple_white",
    color_discrete_sequence=px.colors.qualitative.Plotly
)

st.plotly_chart(fig, theme="streamlit", use_container_width=True)

# +
#Just show this df again (not necessary)
dfHourPlat = df.loc[:,['Primary streaming service','Hours per day']]

#Plot
fig = px.pie(
    dfHourPlat, 
    values='Hours per day', 
    names='Primary streaming service',
    title='Summary hours for each platform',
    hole=.4,
    width=1000,
    height=500
)
st.plotly_chart(fig, theme="streamlit", use_container_width=True)
# -

# #### Platforms and mental health problems

# In this dataset there are 4 columns with mental health problems: OCD, Depression, Anxiety and Insomnia.
# I'll combine them into one abstract "mental problem" by summarizing their values. This will help us to do "easy-to-analyze" plots

# +
#Creating dataframe dfMentalPlat with 5 columns and add another one - 'Sum' by summarazing OCD, Depression, Anxiety and Insomnia columns
dfMentalPlat = dfcop.loc[:,['Primary streaming service','OCD','Depression','Anxiety','Insomnia']]
dfMentalPlat = dfMentalPlat.assign(Sum=lambda x: x.OCD + x.Anxiety + x.Depression + x.Insomnia)

#There I've created new df - dfMentalPlatSum by using method .groupby on dfMentalPlat on "Primary streaming service" column
#and sum all values. Then i've sorted this df by .sort_values
dfMentalPlatSum = dfMentalPlat.groupby("Primary streaming service", as_index = False).sum()
dfMentalPlatSum.sort_values('Sum', ascending=False, inplace=True)

#The same as the previouse but instead of sum method I've used mean method
dfMentalPlatMean = dfMentalPlat.groupby("Primary streaming service", as_index = False).mean().round(2)
dfMentalPlatMean.sort_values('Sum', ascending=False, inplace=True)
# -

# I have the hypothesis that the most mental ill platform is a YouTube Music because there is a lot of live streams with different music genres to study. For example lo-fi radio to study and work(Lo-Fi Girl). Core audience of this translations is 15-26 years old people and I think that the most mental health problems pop up in the age of 18. So thats why i think YouTube Music has the vast majority of people with mental health problems.

# +
#first plot with sum values
fig = px.histogram(
    dfMentalPlatSum, 
    x='Primary streaming service', 
    y='Sum', 
    color='Primary streaming service'
)

fig.update_layout(
    title ='Mental Health problems and Platform<br>(sum values)', 
    xaxis_title='Primary streaming service',
    yaxis_title='Mental health problems',
    template='plotly_dark',
)

st.plotly_chart(fig, theme="streamlit", use_container_width=True)


#second plot with mean values
fig = px.histogram(
    dfMentalPlatMean, 
    x='Primary streaming service', 
    y='Sum', 
    color='Primary streaming service'
)

fig.update_layout(
    title ='Mental Health problems and Platform<br>(mean values)', 
    xaxis_title='Primary streaming service',
    yaxis_title='Mental health problems',
    template='plotly_dark',
)

st.plotly_chart(fig, theme="streamlit", use_container_width=True)
# -

# My hypothesis was wrong. Apple music has the vast majority of people with mental health problems in mean values. You can say that Spotify has the vast majority of people (in sum) with mental health problems but this is because it is the most popular platform in this dataset.

# ### Genre analyze

# #### Check the most popular genre

# There i'll check the most popular genre in dataset. My hypothesis is that this will be a Pop music

# + colab={"base_uri": "https://localhost:8080/", "height": 542} id="CYLPuE5xYUUO" outputId="f29868bb-82dd-461b-c791-55199a517877"
#Create new df with a new column 'Amount of people'
dfGen = df.loc[:,['Fav genre']]
dfGen['Amount of people'] = 1

#Just groupby
dfSumG2 = dfGen.groupby('Fav genre',as_index= False).sum()

#Plot
fig = px.bar(
    dfSumG2, 
    x='Fav genre',
    y='Amount of people', 
    color = 'Amount of people',
    title='The most favourite genre',
    height=500,
    width=1000,
    template="simple_white"
)

fig.update_layout(
    xaxis_title='<b>Genre</b>'
)

st.plotly_chart(fig, theme="streamlit", use_container_width=True)
# -

# My hypothesis was wrong. And it is really interesting that Rock is more popular than Pop in this dataset

# #### Trying to find correlations between favourite genre and mental health problems

# My hypothesis is that Lo-Fi genre has the most people with mental health problems in mean values. The reasons why i think this way were already told.

# +
#Create new df with a new column by summarazing next columns: Anxiety, Depression, Insomnia and OCD
df_3 = dfcop.loc[:,['Age','Fav genre', 'Anxiety','Depression','Insomnia','OCD','Hours per day']]
df_3 = df_3.assign(Sum=lambda x: x.OCD + x.Anxiety + x.Depression + x.Insomnia)

#Groupby and sort for sum
df_3S = df_3.groupby('Fav genre', as_index=False).sum()
df_3S.sort_values('Sum', ascending=False, inplace=True)

#Groupby and sort for mean
df_3M = df_3.groupby('Fav genre', as_index=False).mean().round(2)
df_3M.sort_values('Sum', ascending=False, inplace=True)

# +
#Plot1(Sum values)
fig = px.histogram(
    df_3S, 
    x='Fav genre', 
    y='Sum', 
    color='Fav genre'
)

fig.update_layout(
    title ='Mental Health problems and Fav genres<br>(sum values)', 
    xaxis_title='Fav genres',
    yaxis_title='Mental health problems (sum)',
    template='plotly_dark',
)

st.plotly_chart(fig, theme="streamlit", use_container_width=True)


#Plot2(Mean values)
fig = px.histogram(
    df_3M, 
    x='Fav genre', 
    y='Sum', 
    color='Fav genre'
)

fig.update_layout(
    title ='Mental Health problems and Fav genres<br>(mean values)', 
    xaxis_title='Fav genres',
    yaxis_title='Mental health problems (mean)',
    template='plotly_dark',
)

st.plotly_chart(fig, theme="streamlit", use_container_width=True)
# -

# My hypothesis was right, but you can notice that rock has the greates value in the sum chart. This is because it is the most popular genre in my dataset

# ### Age analyze

# #### Check amount of young, middle age and old people

# Here I'll create 3 dataframes with <u>Young</u>( < 30 y.o.), <u>Middle aged</u>( 50 < and >= 30 ) and <u>Old people</u>( >= 60) to compare their percentage in dataset. This will help us to understand the difference in quantity between all of these groups of people.

# +
#Here I'll create 3 dataframes with Young, Middle aged and Old people to compare their percentage in dataset

#I use dfcop df instead df because it is easier to work with it

#Create df with the Young people and a variable with their quatity
dfAgeY = dfcop.loc[dfcop['Age'] < 30]
Yl = len(dfAgeY)

#Create df with the Middle aged people and a variable with their quatity
dfAgeM = dfcop.loc[(dfcop['Age'] >= 30) & ( dfcop['Age'] < 50)]
Ml = len(dfAgeM)

#Create df with the Old people and a variable with their quatity
dfAgeO = dfcop.loc[(dfcop['Age'] >= 50)]
Ol = len(dfAgeO)

#Plot
fig = px.pie(
    dfHourPlat, 
    values=[Yl,Ml,Ol], 
    names=['Young','Middle age','Old'],
    title='Comparison between quantity of Young, Middle aged and Old people in dataframe<br>(dfcop)',
    width=1000,
    height=500,
    template='plotly_dark',
)

st.plotly_chart(fig, theme="streamlit", use_container_width=True)

#sum of all the people is 616
#print(Yl+Ml+Ol)
# -

# #### Correlation between age and mental health problems

# My hypothesis is that the most stressed year in person's life is 18-th year. It is quite logical because in this years there is alot of changes in person's life style in general. 

# ##### Sum(Age)

# +
#Create new df, add new column with a sum of mental problems and groupby it by age 
df3d = dfcop.loc[:,['Age','Anxiety','Depression','Insomnia','OCD']]
df3d = df3d.assign(Sum=lambda x: x.OCD + x.Anxiety + x.Depression + x.Insomnia)
df3d = df3d.groupby('Age', as_index= False).sum()

#fig = px.line_3d(df3d, x="Age", y='Hours per day'z="Anxiety")
#fig.show()

# +
#Here i'll create subplot with 4 figures (line graphs)

#First two figures
figures = [
    
    #Figure 1 (Corellation between Age and Anxiety)
    px.line(
        df3d, 
        x="Age",
        y=["Anxiety"],
        title='Corellation between age and Mental Health Poblems',
        width = 300,
        height = 300,
        color_discrete_sequence=[px.colors.qualitative.Plotly[0]],
    ),

    #Figure 2 (Corellation between Age and Depression)
    px.line(
        df3d, 
        x="Age",
        y=['Depression'],
        title='Corellation between age and Mental Health Poblems',
        width = 300,
        height = 300,
        color_discrete_sequence=[px.colors.qualitative.Plotly[1]],
    ),
]

#Second two figures
figures2 = [ 
    
    #Figure 3 (Corellation between Age and Insomnia)
    px.line(
        df3d, 
        x="Age",
        y=['Insomnia'],
        title='Corellation between age and Mental Health Poblems',
        width = 300,
        height = 300,
        color_discrete_sequence=[px.colors.qualitative.Plotly[2]]
    ),

    #Figure 4 (Corellation between Age and OCD)
    px.line(
        df3d, 
        x="Age",
        y=['OCD'],
        title='Corellation between age and Mental Health Poblems',
        width = 300,
        height = 300,
        color_discrete_sequence=[px.colors.qualitative.Plotly[3]]
    ),
]

#Creating subplot with 2 rows and 2 columns
fig = make_subplots(rows=len(figures), cols=2) 

#Filling up our subplot with first two figures
for i, figure in enumerate(figures):
    for trace in range(len(figure["data"])):
        fig.append_trace(figure["data"][trace], row=i+1, col=1)

#Filling up our subplot with second two figures
for i, figure in enumerate(figures2):
    for trace in range(len(figure["data"])):
        fig.append_trace(figure["data"][trace], row=i+1, col=2)


fig.update_layout(
    height=800, 
    width=1100, 
    title_text="Sublot with Corellation between Age and Mental Health Poblems<br>(differentiated)", 
    xaxis_title='Age',
    yaxis_title='Mental health problem',
    template='plotly_dark',
)
st.plotly_chart(fig, theme="streamlit", use_container_width=True)
# -

# <b>As we can see the highest point on each figure is 18 y.o.</b><br>Also we can notice small pick in 21 y.o.

# +
#Plot with a comparasion of mental problems
fig = px.line(
    df3d, 
    x="Age",
    y=["Anxiety", 'Depression','Insomnia','OCD'],
    title='Plot Corellation between Age and Mental Health Poblems<br>(comparison)',
    template='plotly_dark',
)

fig.update_layout(
    yaxis_title='Mental health problems',
)

st.plotly_chart(fig, theme="streamlit", use_container_width=True)
# -

# This is straight up comparison and of course 18 y.o. have the highest value

# +
#Histogram to show the sum
fig = px.histogram(
    df3d, 
    x='Age', 
    y=["Anxiety", 'Depression','Insomnia','OCD'],
    title='Corellation between age and Mental Health Poblems<br>(to show how they sum up in certain region)',
    template='plotly_dark'
    #barmode = 'overlay'
)

fig.update_layout(
    yaxis_title='Mental health problems',
)

st.plotly_chart(fig, theme="streamlit", use_container_width=True)
# -

# <b>Here we can see summarized regions for the period of 4 years.</b><br>The greates one is 15-19 y.o.<br>The second greatest is 20-24 y.o.

# +
#Line graph with a sum
fig = px.line(
    df3d, 
    x="Age",
    y=['Sum'],
    title='Corellation between Age and Mental Health Poblems<br>(sum)',
    template='plotly_dark',
)

fig.update_layout(
    yaxis_title='Mental health problems',
)

st.plotly_chart(fig, theme="streamlit", use_container_width=True)
# -

# <b>My hypothesis was right.</b><br>It is actually true that the most stressed year in person's life is the 18-th year. But this results can also appear because of the quantity of Young people( < 30 y.o.) in this dataset (75%). This is why this information may be false in general but for this exact dataset it is true

# ##### Mean(Age)

# <b>This is the same graphs but with mean values instead of sum values.</b><br>They are not so clear and evident as the previouse ones and this is why I won't analyse them, just show.

# +
df3d = dfcop.loc[:,['Age','Anxiety','Depression','Insomnia','OCD']]

# try to make a linear graph of hours and mental health problems

df3d = df3d.groupby('Age', as_index= False).mean()

#fig = px.line_3d(df3d, x="Age", y='Hours per day'z="Anxiety")
#fig.show()
# -

#Plot
fig = px.line(
    df3d, 
    x="Age",
    y=["Anxiety", 'Depression','Insomnia','OCD'],
    title='Plot Corellation between Age and Mental Health Poblems(mean)',
    template='plotly_dark'
)
st.plotly_chart(fig, theme="streamlit", use_container_width=True)

# As I said, they are not evident

#Plot
fig = px.histogram(
    df3d, 
    x='Age', 
    y=["Anxiety", 'Depression','Insomnia','OCD'],
    title='Corellation between age and Mental Health Poblems(mean)',
    template='plotly_dark'
    #barmode = 'overlay'
)
st.plotly_chart(fig, theme="streamlit", use_container_width=True)

# ### Hours per day analyze

# #### Check for the most popular amount of hours per day

# Here I'll find the most popular amount of time that people spend on music daily.<br>This will help us with the future graphs

# +
#Create new df with new column 'Sum'
dfH = dfcop.loc[:,['Hours per day']]
dfH['Sum'] = 1

#Groupby it by 'Hours per day', sum values and then sort
dfH = dfH.groupby('Hours per day', as_index= False).sum()
dfH.sort_values('Sum', ascending=False, inplace=True)

#Plot
fig = px.scatter(
    dfH, 
    x='Hours per day', 
    y='Sum',
    size='Sum',
    color='Sum'
)

fig.update_layout(
    yaxis_title ='Amount of People',
    title='Check for the most popular amount of hours per day'
)

st.plotly_chart(fig, use_container_width=True)
# -

# <b>The most popular amount of hours that people spend on music daily is <u>2</u></b><br>
# <b>Second</b> place holds <u>3 hours</u><br>
# <b>Third</b> one is for <u>1 hour</u><br>
# And <b>fourth</b> place is for <u>4 hours</u>

# #### Corellation between hours and mental health problems

# ##### Sum(Hours)

#Create new df and groupby it by 'Hours per day'
df3dH = dfcop.loc[:,['Anxiety','Depression','Insomnia','OCD','Hours per day']]
df3dH = df3dH.groupby('Hours per day', as_index= False).sum()

# +
#the same structure i've used in Age section
figures = [
    px.line(
        df3dH, 
        x="Hours per day",
        y=["Anxiety"],
        title='Corellation between age and Mental Health Poblems',
        width = 300,
        height = 300,
        color_discrete_sequence=[px.colors.qualitative.Plotly[0]],
    ),
    
    px.line(
        df3dH, 
        x="Hours per day",
        y=['Depression'],
        title='Corellation between age and Mental Health Poblems',
        width = 300,
        height = 300,
        color_discrete_sequence=[px.colors.qualitative.Plotly[1]],
    ),
]

figures2 = [ 
    px.line(
        df3dH, 
        x="Hours per day",
        y=['Insomnia'],
        title='Corellation between age and Mental Health Poblems',
        width = 300,
        height = 300,
        color_discrete_sequence=[px.colors.qualitative.Plotly[2]]
    ),
    
    px.line(
        df3dH, 
        x="Hours per day",
        y=['OCD'],
        title='Corellation between age and Mental Health Poblems',
        width = 300,
        height = 300,
        color_discrete_sequence=[px.colors.qualitative.Plotly[3]]
    ),
    ]

fig = make_subplots(rows=len(figures), cols=2) 


for i, figure in enumerate(figures):
    for trace in range(len(figure["data"])):
        fig.append_trace(figure["data"][trace], row=i+1, col=1)

for i, figure in enumerate(figures2):
    for trace in range(len(figure["data"])):
        fig.append_trace(figure["data"][trace], row=i+1, col=2)


fig.update_layout(
    height=800, 
    width=1100, 
    title_text="Sublot with Corellation between Hours per day and Mental Health Poblems<br>(sum)", 
    xaxis_title='Hours',
    yaxis_title='Mental health problem',
    template='plotly_dark',
)
st.plotly_chart(fig, theme="streamlit", use_container_width=True)
# -

# <b>As we can see</b>
# <br>2 hours per day have first place
# <br>3 hours have second
# <br>4 hours have 3rd
# <br>1 hour have 4th
# <b>
# <br>It is really interesting because there is more people who spend 1 hour than 4 hours daily on music.
# <br>But still, people who spend 4 hours have the sum with more mental health problems than people who spend 1 hour.
# </b>
# <br>Other places match with previouse plot
#

# ##### Mean(Hours)

# This graph is not for my analysis, i just want to show it

#Create df and groupby by 'Hours per day'
df3dH = dfcop.loc[:,['Anxiety','Depression','Insomnia','OCD','Hours per day']]
df3dH = df3dH.groupby('Hours per day', as_index= False).mean()

# +
#the same structure i've used in Age section
figures = [
    px.line(
        df3dH, 
        x="Hours per day",
        y=["Anxiety"],
        title='Corellation between age and Mental Health Poblems',
        width = 300,
        height = 300,
        color_discrete_sequence=[px.colors.qualitative.Plotly[0]],
    ),
    
    px.line(
        df3dH, 
        x="Hours per day",
        y=['Depression'],
        title='Corellation between age and Mental Health Poblems',
        width = 300,
        height = 300,
        color_discrete_sequence=[px.colors.qualitative.Plotly[1]],
    ),
]

figures2 = [ 
    px.line(
        df3dH, 
        x="Hours per day",
        y=['Insomnia'],
        title='Corellation between age and Mental Health Poblems',
        width = 300,
        height = 300,
        color_discrete_sequence=[px.colors.qualitative.Plotly[2]]
    ),
    
    px.line(
        df3dH, 
        x="Hours per day",
        y=['OCD'],
        title='Corellation between age and Mental Health Poblems',
        width = 300,
        height = 300,
        color_discrete_sequence=[px.colors.qualitative.Plotly[3]]
    ),
    ]

fig = make_subplots(rows=len(figures), cols=2) 


for i, figure in enumerate(figures):
    for trace in range(len(figure["data"])):
        fig.append_trace(figure["data"][trace], row=i+1, col=1)

for i, figure in enumerate(figures2):
    for trace in range(len(figure["data"])):
        fig.append_trace(figure["data"][trace], row=i+1, col=2)


fig.update_layout(
    height=800, 
    width=1100, 
    title_text="Sublot with Corellation between Hours per day and Mental Health Poblems(mean)", 
    xaxis_title='Hours',
    yaxis_title='Mental health problem',
    template='plotly_dark',
)
st.plotly_chart(fig, theme="streamlit", use_container_width=True)
# -

# ## Difference between musicians and non-musicans

# There I'll try to find some difference between musicians and not a musicians

# ### Separate musicians and non-muscians

#There I'll create df with only musician(df.Instrumentalist == 'Yes' or df.Composer == 'Yes')
dfArt1 = df.drop(df[(df.Instrumentalist == 'No')].index)
dfArt2 = df.drop(df[df.Composer == 'No'].index)
dfArt = pd.concat([dfArt1, dfArt2])


#Mental problems that musicians have
dfMentalA = dfArt.loc[:,['Anxiety','Depression','Insomnia','OCD']]
dfMentalA = dfMentalA.assign(Sum1=lambda x: x.OCD + x.Anxiety + x.Depression + x.Insomnia)
dfMentalAM = dfMentalA.mean().round(2)
dfMentalAS = dfMentalA.sum().round(2)

#There I'll create df with only non-musician(df.Instrumentalist == 'No' | df.Composer == 'No')
dfNoArt= df.drop(df[(df.Instrumentalist == 'Yes')|(df.Composer == 'Yes') ].index)


#Mental problems that non-musicians have
dfMentalNoA = dfNoArt.loc[:,['Anxiety','Depression','Insomnia','OCD']]
dfMentalNoA = dfMentalNoA.assign(Sum2=lambda x: x.OCD + x.Anxiety + x.Depression + x.Insomnia)
dfMentalNoAM = dfMentalNoA.mean().round(2)
dfMentalNoAS = dfMentalNoA.sum().round(2)

# ### Trying to find corelations and difference between Musicians and Non-Musicians

# There I'll compare favourite genres that musicians and non-musicians have

# #### Difference in favourite genres

# +
dfG = dfArt.loc[:,['Fav genre']]

dfG['Amount of people'] = 1

dfSumG = dfG.groupby('Fav genre',as_index= False).sum()
dfSumG.sort_values('Amount of people', ascending=False, inplace=True)

fig1 = px.bar(
    dfSumG, 
    x='Fav genre',
    y='Amount of people', 
    color = 'Amount of people',
    title='Favourite genres of musicians',
    height=500,
    width=1000,
    template="simple_white",
)
st.plotly_chart(fig1, theme="streamlit", use_container_width=True)


dfG2 = dfNoArt.loc[:,['Fav genre']]

dfG2['Amount of people'] = 1

dfSumG2 = dfG2.groupby('Fav genre',as_index= False).sum()
dfSumG2.sort_values('Amount of people', ascending=False, inplace=True)

fig2 = px.bar(
    dfSumG2, 
    x='Fav genre',
    y='Amount of people', 
    color = 'Amount of people',
    title='Favourite genres of non-musicians',
    height=500,
    width=1000,
    template="simple_white",
)
st.plotly_chart(fig2, theme="streamlit", use_container_width=True)
# -

# <b>There is interesting thing that Classical music is listened by only musician in this exact dataset</b>

# #### Difference in Mental health problems

# I have a hypothesis that musicians have more mental health problems than ordinary people
'''
print(dfMentalAM)
print(dfMentalAS)
print('____________________')
print(dfMentalNoAM)
print(dfMentalNoAS)
'''
#Plot
fig = px.pie(
    values=[17.58, 16.84], 
    names=['Musician','Non-Musician'],
    title='Who has more mental health problems?(mean value)',
    hole=.7,
    width=1000,
    height=500,
    template='plotly',
)
st.plotly_chart(fig, theme="streamlit", use_container_width=True)

# <b>I think my hypothesis was wrong because there is a so small difference(2.2%) that we can count it like a error</b>

# # Conclusion

# There is last column my dataset that I want to check. This column gives us information about music's help with mental health problems
# <br>My hypothesis that music will help the vast majority of people

# +
#Create df
dfHealth = dfcop.loc[:,['Music effects']]
dfHealth['Calc'] = 1

fig = px.pie(
    dfHealth, 
    values='Calc', 
    names='Music effects',
    title='How music has improved Mental Health',
    width=1000,
    height=500,
    color_discrete_sequence=[px.colors.qualitative.Plotly[7], px.colors.qualitative.Pastel1[1], px.colors.qualitative.Plotly[1]]
)
st.plotly_chart(fig, theme="streamlit", use_container_width=True)
# -

# <b>My hypothesis was right</b>
