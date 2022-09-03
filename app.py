import streamlit as st
import matplotlib.pyplot as plt
import time
import pandas as pd
import numpy as np


st.set_page_config(layout="wide")
st.title('DATA ANALYSIS')

data_load_state = st.text('Loading...')
time.sleep(1)
data_load_state.text('Loaded Completely!')


# st.sidebar.title("Data Type Sidebar")

# st.sidebar.checkbox("Quantitative data")
# checkbox2 = st.sidebar.checkbox("Qualitative data")

st.subheader("Quantitative Data")
X_axis = np.arange(3)
X = ['Plug and Perf','Sliding Sleeve','Hydrajet']

# ###########################
# Fracturing Period Data     #
##############################

# data1 = {"Fields":['Permian Field', 'Ordos Field', 'Bakken Field'],'Plug and Perf': [64,68,60], "Sliding Sleeve":[12,13,12], "Hydrajet":[4,7,5]}
data1 = {"Fields":['Plug and Perf', "Sliding Sleeve", 'Hydrajet'], 'Permian Field': [64,12,4], 'Ordos Field':[68,13,7], 'Bakken Field':[60,12,5]}
df1 = pd.DataFrame(data=data1)
df1 = df1.set_index('Fields')

st.write("Fracturing Period (Hours)")
st.table(df1)

d1col1, d1col2, d1col3, d1col4, d1col5, d1col6 = st.columns(6)
if d1col6.button('Plot Data', key='d1'):
    # Y_ticks = data1['Plug and Perf'] + data1['Sliding Sleeve'] + data1['Hydrajet']
    fig, ax = plt.subplots()
    ax.plot(X_axis,data1['Permian Field'],'go', label="Permian Field")
    ax.plot(X_axis,data1['Ordos Field'],'bP', label="Ordos Field")
    ax.plot(X_axis,data1['Bakken Field'],'rD', label="Bakken Field")

    ax.legend()
    ax.set_xticks(X_axis, X)
    ax.set_yticks(np.arange(0,75,5))
    ax.set_title('Fracturing Period (Hours)')

    fig1, ax1 = plt.subplots()
    ax1.bar(X_axis,data1['Permian Field'], 0.25, label="Permian Field", color='g')
    ax1.bar(X_axis+0.25,data1['Ordos Field'], 0.25, label="Ordos Field", color='b')
    ax1.bar(X_axis+0.5,data1['Bakken Field'], 0.25, label="Bakken Field", color='r')
    ax1.legend()
    ax1.set_title('Fracturing Period (Hours)')
    ax1.set_xticks([x + 0.25 for x in X_axis], X)
    ax1.set_yticks(np.arange(0,75,5))


    pp_df = df1.iloc[0]
    pp_avg = (pp_df['Permian Field'] + pp_df['Ordos Field'] + pp_df['Bakken Field']) // 3


    ss_df = df1.iloc[1]
    ss_avg = (ss_df['Permian Field'] + ss_df['Ordos Field'] + ss_df['Bakken Field']) // 3

    h_df = df1.iloc[2]
    h_avg = (h_df['Permian Field'] + h_df['Ordos Field'] + h_df['Bakken Field']) // 3


    fig2, ax2 = plt.subplots()
    a = ax2.barh(X_axis,[float("{:.2f}".format(pp_avg/1)), float("{:.2f}".format(ss_avg/1)), float("{:.2f}".format(h_avg/1))], 0.4)
    # ax2.legend()
    ax2.set_title('Average Values')
    ax2.set_yticks([x for x in X_axis], X)
    ax2.set_xticks([pp_avg,ss_avg,h_avg])
    ax2.bar_label(a)

    p1col1, p1col2, p1col3 = st.columns(3)
    p1col1.pyplot(fig=fig)
    p1col2.pyplot(fig=fig1)
    p1col3.pyplot(fig=fig2)
    # st.pyplot(fig=fig)
    

##########################
# Cost of Operation Data #
##########################
st.write("")
data2 = {"Fields":['Plug and Perf', "Sliding Sleeve", 'Hydrajet'], 'Permian Field': [790000,680000,870000], 'Ordos Field':[820000,690000,895000], 'Bakken Field':[850000,700000,920000]}

df2 = pd.DataFrame(data=data2)
df2 = df2.set_index('Fields')

st.write("Cost Of Operation (US$)")
st.table(df2)

d2col1, d2col2, d2col3, d2col4, d2col5, d2col6 = st.columns(6)
if d2col6.button("Plot Data", key='d2'):
        # Y_ticks = data1['Plug and Perf'] + data1['Sliding Sleeve'] + data1['Hydrajet']
    fig2, ax2 = plt.subplots()
    ax2.plot(X_axis,data2['Permian Field'],'go', label="Permian Field")
    ax2.plot(X_axis,data2['Ordos Field'],'bP', label="Ordos Field")
    ax2.plot(X_axis,data2['Bakken Field'],'rD', label="Bakken Field")

    ax2.legend()
    ax2.set_xticks(X_axis, X)
    ax2.set_yticks(np.arange(650000,1000000,50000))
    ax2.set_title('Cost Of Operation (US$)')

    fig3, ax3 = plt.subplots()
    ax3.bar(X_axis,data2['Permian Field'], 0.25, label="Permian Field", color='g')
    ax3.bar(X_axis+0.25,data2['Ordos Field'], 0.25, label="Ordos Field", color='b')
    ax3.bar(X_axis+0.5,data2['Bakken Field'], 0.25, label="Bakken Field", color='r')
    ax3.legend()
    ax3.set_title('Cost Of Operation (US$)')
    ax3.set_xticks([x+0.25 for x in X_axis], X)


    pp_df = df2.iloc[0]
    pp_avg = (pp_df['Permian Field'] + pp_df['Ordos Field'] + pp_df['Bakken Field']) // 3


    ss_df = df2.iloc[1]
    ss_avg = (ss_df['Permian Field'] + ss_df['Ordos Field'] + ss_df['Bakken Field']) // 3

    h_df = df2.iloc[2]
    h_avg = (h_df['Permian Field'] + h_df['Ordos Field'] + h_df['Bakken Field']) // 3


    fig, ax = plt.subplots()
    a = ax.barh(X_axis,[float("{:.2f}".format(pp_avg/1)), float("{:.2f}".format(ss_avg/1)), float("{:.2f}".format(h_avg/1))], 0.4)
    # ax2.legend()
    ax.set_title('Average Values')
    ax.set_yticks([x for x in X_axis], X)
    ax.bar_label(a)
    # ax.set_xticks([pp_avg,ss_avg,h_avg])

    
    p2col1, p2col2, p1col3 = st.columns(3)
    p2col1.pyplot(fig=fig2)
    p2col2.pyplot(fig=fig3)
    p1col3.pyplot(fig=fig)

########################
# Shut in time          #
#########################
st.write("")
data3 = {"Fields":['Plug and Perf', "Sliding Sleeve", 'Hydrajet'],'Permian Field': [5,4,4], "Ordos Field":[6,5,2], "Bakken Field":[8,6,4]}

df3 = pd.DataFrame(data=data3)
df3 = df3.set_index('Fields')

st.write("Shut In Time (Hours)")
st.table(df3)

d3col1, d3col2, d3col3, d3col4, d3col5, d3col6 = st.columns(6)
if d3col6.button("Plot Data", key='d3'):
    # Y_ticks = data1['Plug and Perf'] + data1['Sliding Sleeve'] + data1['Hydrajet']
    fig2, ax2 = plt.subplots()
    ax2.plot(X_axis,data3['Permian Field'],'go', label="Permian Field")
    ax2.plot(X_axis,data3['Ordos Field'],'bP', label="Ordos Field")
    ax2.plot(X_axis,data3['Bakken Field'],'rD', label="Bakken Field")

    ax2.legend()
    ax2.set_xticks(X_axis, X)
    ax2.set_title('Shut In Time (Hours)')

    fig3, ax3 = plt.subplots()
    ax3.bar(X_axis,data3['Permian Field'], 0.25, label="Permian Field", color='g')
    ax3.bar(X_axis+0.25,data3['Ordos Field'], 0.25, label="Ordos Field", color='b')
    ax3.bar(X_axis+0.5,data3['Bakken Field'], 0.25, label="Bakken Field", color='r')
    ax3.legend()
    ax3.set_title('Shut In Time (Hours)')
    ax3.set_xticks([x+0.25 for x in X_axis], X)

    pp_df = df3.iloc[0]
    pp_avg = (pp_df['Permian Field'] + pp_df['Ordos Field'] + pp_df['Bakken Field']) / 3


    ss_df = df3.iloc[1]
    ss_avg = (ss_df['Permian Field'] + ss_df['Ordos Field'] + ss_df['Bakken Field']) / 3

    h_df = df3.iloc[2]
    h_avg = (h_df['Permian Field'] + h_df['Ordos Field'] + h_df['Bakken Field']) / 3


    fig, ax = plt.subplots()
    a = ax.barh(X_axis,[float("{:.2f}".format(pp_avg/1)), float("{:.2f}".format(ss_avg/1)), float("{:.2f}".format(h_avg/1))], 0.4)
    # ax2.legend()
    ax.set_title('Average Values')
    ax.set_yticks([x for x in X_axis], X)
    ax.bar_label(a)
    
    p2col1, p2col2, p2col3 = st.columns(3)
    p2col1.pyplot(fig=fig2)
    p2col2.pyplot(fig=fig3)
    p2col3.pyplot(fig=fig)


######################
# Water usage         #
#######################
st.write("")
data4 = {"Fields":['Plug and Perf', "Sliding Sleeve", 'Hydrajet'],'Permian Field': [2730000,1960000,1200000], "Ordos Field":[2620000,1855600,1130000], "Bakken Field":[2765300,1910700,1211000]}


df4 = pd.DataFrame(data=data4)
df4 = df4.set_index('Fields')

st.write("Water Usage (gal)")
st.table(df4)

d4col1, d4col2, d4col3, d4col4, d4col5, d4col6 = st.columns(6)
if d4col6.button("Plot Data", key='d4'):
    # Y_ticks = data4['Permian Field'] + data4["Ordos Field"] + data4["Bakken Field"]

    fig2, ax2 = plt.subplots()
    ax2.plot(X_axis,data4['Permian Field'],'go', label="Permian Field")
    ax2.plot(X_axis,data4['Ordos Field'],'bP', label="Ordos Field")
    ax2.plot(X_axis,data4['Bakken Field'],'rD', label="Bakken Field")

    ax2.legend()
    ax2.set_xticks(X_axis, X)
    ax2.set_title('Water Usage (gal)')

    fig3, ax3 = plt.subplots()
    ax3.bar(X_axis,data4['Permian Field'], 0.25, label="Permian Field", color='g')
    ax3.bar(X_axis+0.25,data4['Ordos Field'], 0.25, label="Ordos Field", color='b')
    ax3.bar(X_axis+0.5,data4['Bakken Field'], 0.25, label="Bakken Field", color='r')
    ax3.legend()
    ax3.set_title('Water Usage (gal)')
    ax3.set_xticks([x+0.25 for x in X_axis], X)
    

    pp_df = df4.iloc[0]
    pp_avg = (pp_df['Permian Field'] + pp_df['Ordos Field'] + pp_df['Bakken Field']) / 3


    ss_df = df4.iloc[1]
    ss_avg = (ss_df['Permian Field'] + ss_df['Ordos Field'] + ss_df['Bakken Field']) / 3

    h_df = df4.iloc[2]
    h_avg = (h_df['Permian Field'] + h_df['Ordos Field'] + h_df['Bakken Field']) / 3


    fig, ax = plt.subplots()
    a = ax.barh(X_axis,[float("{:.2f}".format(pp_avg/1)), float("{:.2f}".format(ss_avg/1)), float("{:.2f}".format(h_avg/1))], 0.4)
    # ax2.legend()
    ax.set_title('Average Values')
    ax.set_yticks([x for x in X_axis], X)
    ax.bar_label(a)


    p2col1, p2col2, p2col3 = st.columns(3)
    p2col1.pyplot(fig=fig2)
    p2col2.pyplot(fig=fig3)
    p2col3.pyplot(fig=fig)




