import pandas as pd


class TransformedData:
    cryptocurrencies_df = pd.read_csv('transformed_data/cryptocurrencies.csv')
    crypto_daily_history_df = pd.read_csv('transformed_data/crypto_daily_history.csv')
    crypto_tag_df = pd.read_csv('transformed_data/crypto_tags.csv')
    tags_df = pd.read_csv('transformed_data/tags.csv')
    dates_df = pd.read_csv('transformed_data/dates.csv')
    crypto_price_times_df = pd.read_csv('transformed_data/crypto_price_times.csv')
    crypto_price_types_df = pd.read_csv('transformed_data/crypto_price_types.csv')
    crypto_historical_prices_df = pd.read_csv('transformed_data/crypto_historical_prices.csv')


