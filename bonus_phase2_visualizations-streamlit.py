import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.io as pio
import plotly.graph_objects as go

#################################################

##### To run the file:
## 1- cd into project directory
## 2- run command : 'streamlit run bonus_phase2_visualizations-streamlit.py'

#################################################

st.set_page_config(
    page_title = 'Quera Project Phase 2',
    page_icon = 'random',
    layout = 'centered'
)

### Set Title
st.markdown('<div style="text-align: center; font-size: 45px; margin-bottom:30px">Quera Project - Phase 2</div>', unsafe_allow_html=True)

############################################################  Q1 Start ############################################################
st.markdown("<hr/>", unsafe_allow_html=True)
st.markdown('<div style="text-align: center; font-size: 25px; margin-bottom:30px">Question 1</div>', unsafe_allow_html=True)

Q1_data = pd.read_csv('./data_phase2/Q1_data.csv')
Q1_data.drop(columns=['Unnamed: 0'], inplace=True)
st.write(f"Here we will take a look at a sample of our data :")
st.dataframe(Q1_data.head())
st.write(f"And also its shape :")
st.write(Q1_data.shape)
st.write(f"So, how many unique coins do we have in this dataset?")
st.code(list(Q1_data['name'].value_counts().index))

st.write(f"We can also notice that we have a time series dataset.")
st.write(f"Also, what is our dataset's date range? Let's find out.")
Q1_data['time_stamp'] = pd.to_datetime(Q1_data['time_stamp'])
st.markdown(f"Minimum date is : <code>{Q1_data['time_stamp'].min().date()}</code>", unsafe_allow_html=True)
st.markdown(f"Maximum date is : <code>{Q1_data['time_stamp'].max().date()}</code>", unsafe_allow_html=True)

st.markdown('<div style="text-align: center; font-size: 25px">******</div>', unsafe_allow_html=True)
st.write(f"Let's see which coin has had the largest sum of Volume over this period.")

Q1_data_agg_vol = Q1_data.groupby(['name']).agg({'volume': 'sum'})
Q1_data_agg_vol = Q1_data_agg_vol.sort_values(by='volume', ascending=False)

st.dataframe(Q1_data_agg_vol)
st.markdown(f"As seen above, <code>{Q1_data_agg_vol.index[0]}</code> stands first.", unsafe_allow_html=True)

st.markdown('<div style="text-align: center; font-size: 25px">******</div>', unsafe_allow_html=True)

st.write(f"As our last peek of this dataset, let's see which coin has had the largest sum of Market Cap over this period.")
Q1_data_agg_mkcp = Q1_data.groupby(['name']).agg({'market_cap': 'sum'})
Q1_data_agg_mkcp = Q1_data_agg_mkcp.sort_values(by='market_cap', ascending=False)
st.dataframe(Q1_data_agg_mkcp)
st.markdown(f"Obviously, <code>{Q1_data_agg_mkcp.index[0]}</code> wins the prize.", unsafe_allow_html=True)
market_cap_quote = """
> The total market value of a cryptocurrency's circulating supply.
"""
st.markdown(f"And this was expected. Since the definition of Market Capitalization is : {market_cap_quote}")


############################################################  Q1 End ############################################################





############################################################  Q2 Start ############################################################
st.markdown("<hr/>", unsafe_allow_html=True)
st.markdown('<div style="text-align: center; font-size: 25px; margin-bottom:30px">Question 2</div>', unsafe_allow_html=True)

Q2_data = pd.read_csv('./data_phase2/Q2_data.csv')
st.write(f"Let's first take a look at a sample of our data :")
st.dataframe(Q2_data.head())
st.write(f"And also its shape :")
st.write(Q2_data.shape)
st.write(f"We can see that we have 20 different coins along with 5 features.")
st.write(f"Now, let's perform some analysis on these features using plots.")
st.markdown('<div style="text-align: center; font-size: 25px">******</div>', unsafe_allow_html=True)


### Plot Volume and MarketCap 
st.write(f"Distriution of Volume and MarketCap")
selected_col = st.selectbox('Select a feature :', ['Volume', 'MarketCap'])
st.bar_chart(data=Q2_data, x='Symbol', y=selected_col, color='Symbol')

st.markdown('<div style="text-align: center; font-size: 25px">******</div>', unsafe_allow_html=True)

### Plot PoW and Network 
st.write(f"Distriution of ProofType and Network")
selected_col = st.selectbox('Select a feature :', ['ProofType', 'Network'])
value_counts = Q2_data[selected_col].value_counts()
st.bar_chart(value_counts)

st.markdown('<div style="text-align: center; font-size: 25px">******</div>', unsafe_allow_html=True)    

############################################################  Q2 End ############################################################

############################################################  Q3 Start ############################################################

### Get Data
# df_gold = pd.read_csv('./data_phase2/Q3_Gold_data.csv')
# df_silver = pd.read_csv('./data_phase2/Q3_Silver_data.csv')
# df_copper = pd.read_csv('./data_phase2/Q3_Copper_data.csv')
# df_bitcoin = pd.read_csv('./data_phase2/Q3_Bitcoin_data.csv')
# df_bnb = pd.read_csv('./data_phase2/Q3_Binance Coin_data.csv')
# df_etheruem = pd.read_csv('./data_phase2/Q3_Etheruem_data.csv')
# df_sp500 = pd.read_csv('./data_phase2/Q3_S&P500_data.csv')
# df_tether = pd.read_csv('./data_phase2/Q3_Tether_data.csv')
# df_xrp = pd.read_csv('./data_phase2/Q3_XRP_data.csv')
# df_xmr = pd.read_csv('./data_phase2/Q3_XMR_data.csv')


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

st.markdown("<hr/>", unsafe_allow_html=True)

### Set sub-title
st.markdown('<div style="text-align: center; font-size: 25px; margin-bottom:30px">Question 3</div>', unsafe_allow_html=True)
st.write("##### Candlestick Chart")

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

st.markdown("<hr/>", unsafe_allow_html=True)

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

st.write(f"#### Keypoints :")
st.write(f"- Commodities above have been analysed in time period of  {start_Date.strftime('%Y-%m-%d')} and {end_Date.strftime('%Y-%m-%d')}")
st.markdown("- Tether was the only commodity to have a negative record in this period.", unsafe_allow_html=True)
st.markdown("- Clearly, BNB had the biggest change with an amazing 10,531 percent positive change.", unsafe_allow_html=True)
st.markdown("- The most profitable investment would've been by investing in Bitcoin.", unsafe_allow_html=True)
st.markdown("- Bitcoin was by far the most valuable asset at 7,143.58 per unit.", unsafe_allow_html=True)
st.markdown("- S&P500 (Standard & Poor's 500) index is informational only.", unsafe_allow_html=True)
st.markdown("- Least positive change of 16.08 belongs to Copper.", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

#################################################

### Plot Bollinger band Indicator and its upper/lower limits along with SMA and EMA indicators for Analysis purposes
 
####################### Plot data ###################

df_chart = df.set_index('Date')
df_chart = df_chart[['Close']]

sma = df_chart.rolling(window=20).mean().dropna()
rstd = df_chart.rolling(window=20).std().dropna()
ema = df_chart[['Close']].ewm(span=20, adjust=False).mean().dropna()

upper_band = sma + 2 * rstd
lower_band = sma - 2 * rstd

upper_band = upper_band.rename(columns={'Close': 'upper'})
lower_band = lower_band.rename(columns={'Close': 'lower'})
bb = df_chart.join(upper_band).join(lower_band)
bb = bb.dropna()

buyers = bb[bb['Close'] <= bb['lower']]
sellers = bb[bb['Close'] >= bb['upper']]




plot_width = 1400 
plot_height = 1200

####################### Plot data End ###################

# fig.show()

st.write(f"### Bollinger Band Plot  + EMA/SMA Indicators")
st.markdown(f"")

show_plot_option = st.selectbox("Show Or Hide BB Plot", ["Hide BB Plot", "Show BB Plot"])

st.markdown(f"")
st.write(f"###### Note: The Plot is Interactive.")
st.write(f"###### Note: This section is related to Question 3 (XMR-Monero Close Price Estimation)")

# if st.button("Show Bollinger Band Plot"):    
#     show_plot = not show_plot
    
if show_plot_option == 'Show BB Plot':

    ### Plot begins here

    pio.templates.default = "plotly_dark"

    ### Create figure
    fig = go.Figure()

    ### Add lower_band to figure
    fig.add_trace(go.Scatter(x=lower_band.index, 
                            y=lower_band['lower'], 
                            name='Lower Band', 
                            line_color='rgba(173,204,255,0.2)'
                            ))

    ### Add upper_band to figure
    fig.add_trace(go.Scatter(x=upper_band.index, 
                            y=upper_band['upper'], 
                            name='Upper Band', 
                            fill='tonexty', 
                            fillcolor='rgba(173,204,255,0.2)', 
                            line_color='rgba(173,204,255,0.2)'
                            ))

    ### Add actual close price to figure
    fig.add_trace(go.Scatter(x=df_chart.index, 
                            y=df_chart['Close'], 
                            name='Close', 
                            line_color='#636EFA'
                            ))

    ### Add SMA Indicator to figure
    fig.add_trace(go.Scatter(x=sma.index, 
                            y=sma['Close'], 
                            name='SMA', 
                            line_color='#FECB52'
                            ))

    ### Add EMA Indicator to figure
    fig.add_trace(go.Scatter(x=ema.index, 
                            y=ema['Close'], 
                            name='EMA', 
                            line_color='#FFFFFF'
                            ))

    ### Add buy oppurtunities to figure
    fig.add_trace(go.Scatter(x=buyers.index, 
                            y=buyers['Close'], 
                            name='Buyers', 
                            mode='markers',
                            marker=dict(
                                color='#00CC96',
                                size=10,
                                )
                            ))

    ### Add sell oppurtunities to figure
    fig.add_trace(go.Scatter(x=sellers.index, 
                            y=sellers['Close'], 
                            name='Sellers', 
                            mode='markers', 
                            marker=dict(
                                color='#EF553B',
                                size=10,
                                )
                            ))

    ### Limit X-axis to match our dataframe's date range (its index)
    fig.update_xaxes(range=[df_chart.index.min(), df_chart.index.max()])


    # Display the plot in a separate window
    st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})
    fig.update_layout(width=plot_width, height=plot_height)
    st.markdown(f"- Coin Data is derived from Yahoo API using yfinance module.")
    st.markdown(f"- Sell oppurtunities have been marked with Red which indicates there will probably be a decrease in price.")
    st.markdown(f"- Buy oppurtunities have been marked with Green which indicates there will probably be an increase in price.")
    st.markdown(f"- 'Close' indicates the Close Price of XMR-Monero Coin.")


st.markdown("<hr/>", unsafe_allow_html=True)

############################################################  Q3 End ############################################################

