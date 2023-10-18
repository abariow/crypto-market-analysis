import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go

#################################################

##### To run the file:
## 1- cd into project directory
## 2- run command : 'streamlit run bonus_phase2_visualizations-streamlit.py'

#################################################

### Get Data
df_gold = pd.read_csv('./data_phase2/Q3_Gold_data.csv')
df_silver = pd.read_csv('./data_phase2/Q3_Silver_data.csv')
df_copper = pd.read_csv('./data_phase2/Q3_Copper_data.csv')
df_bitcoin = pd.read_csv('./data_phase2/Q3_Bitcoin_data.csv')
df_bnb = pd.read_csv('./data_phase2/Q3_Binance Coin_data.csv')
df_etheruem = pd.read_csv('./data_phase2/Q3_Etheruem_data.csv')
df_sp500 = pd.read_csv('./data_phase2/Q3_S&P500_data.csv')
df_tether = pd.read_csv('./data_phase2/Q3_Tether_data.csv')
df_xrp = pd.read_csv('./data_phase2/Q3_XRP_data.csv')
df_xmr = pd.read_csv('./data_phase2/Q3_XMR_data.csv')


#################################################

### Read csv files for each commodity
crypto_data = {
    'Gold': pd.read_csv('./data_phase2/Q3_Gold_data.csv'),
    'Silver': pd.read_csv('./data_phase2/Q3_Silver_data.csv'),
    'Copper': pd.read_csv('./data_phase2/Q3_Copper_data.csv'),
    'Bitcoin': pd.read_csv('./data_phase2/Q3_Bitcoin_data.csv'),
    'BNB': pd.read_csv('./data_phase2/Q3_Binance Coin_data.csv'),
    'Etheruem': pd.read_csv('./data_phase2/Q3_Etheruem_data.csv'),
    'S&P500': pd.read_csv('./data_phase2/Q3_S&P500_data.csv'),
    'Tether': pd.read_csv('./data_phase2/Q3_Tether_data.csv'),
    'XRP': pd.read_csv('./data_phase2/Q3_XRP_data.csv'),
    'XMR-Monero': pd.read_csv('./data_phase2/Q3_XMR_data.csv'),
}

### Set Title
st.title("Commodity Analysis")

### Set sub-title
st.write("### Candlestick Chart")

### Create a dropdown to select the cryptocurrency
selected_coin = st.selectbox("Select a commodity", list(crypto_data.keys()))

### Create a figure and axis
fig, ax = plt.subplots()

### Get the selected cryptocurrency's dataframe
df = crypto_data[selected_coin]
df.index = pd.to_datetime(df.index)


fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                open=df['Open'],
                high=df['High'],
                low=df['Low'],
                close=df['Close'])])
### Plot the figure
st.plotly_chart(fig)

#################################################

# selected_coins = st.multiselect("Select Commodity to Plot", 
#                                 [
#                                     'Bitcoin',
#                                     'BNB',
#                                     'Etheruem',
#                                     'S&P500',
#                                     'Tether',
#                                     'XRP',
#                                     'XMR-Monero',
#                                     'Gold',
#                                     'Silver',
#                                     'Copper'
#                                 ])

start_Date = pd.to_datetime('2017-11-09 00:00:00')
end_Date = pd.to_datetime('2023-10-01 00:00:00')

### Set title and subtitle
st.write(f"## Comparison of Price Change")
st.write(f"#### Between {start_Date.strftime('%Y-%m-%d')} and {end_Date.strftime('%Y-%m-%d')}")

### df to be displayed on steamlit
df_1 = pd.DataFrame(columns=['Name', 'Starting_Price', 'End_Price', 'Change(%)'])

for name, df in crypto_data.items():
    starting_price = df.iloc[0]['Close']
    end_price = df.iloc[len(df) - 1]['Close']

    ### Calculate change percentage
    change = (end_price - starting_price) / np.abs(starting_price) * 100
    new_row = {
        'Name' : name,
        'Starting_Price' : starting_price,
        'End_Price': end_price,
        'Change(%)': change
    }

    ### Create a DataFrame for the new row
    new_row_df = pd.DataFrame([[name, starting_price, end_price, change]], columns=['Name', 'Starting_Price', 'End_Price', 'Change(%)'])

    ### Concatenate the new row DataFrame with the original DataFrame
    df_1 = pd.concat([df_1, new_row_df], ignore_index=True)

### Show df_1 in streamlit App
st.write(df_1)