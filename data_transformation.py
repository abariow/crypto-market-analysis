import os
import pandas as pd
import datetime as dt


class CryptoDataTransformer:
    
    def __init__(self):
        
        self.currenct_dir = os.getcwd()
        self.raw_data_path = os.path.join(self.currenct_dir, 'data')
        self.transformed_data_path = os.path.join(self.currenct_dir, 'transformed_dataa')
        
        self.raw_data = {
            'CryptosTable': None, # a single table
            'CryptosHistoricalTables': [], # list of tables
        }
        
        self.transformed_data = {
            'Cryptocurrencies': None,
            'Tags': None,
            'CryptoTag': None,
            'Dates': None,
            'CryptoPriceTypes': None,
            'CryptoDailyHistory': None,
            'CryptoPriceTimes': None,
            'CryptoHistoricalPrices': None,
        }
        
        self.cryptocurrencies = pd.DataFrame(columns = [
            'crypto_id',
            'crypto_name',
            'symbol',
            'main_link',
            'historical_link',
            'github_link',
            'rnk',
        ])
        
        self.tags = pd.DataFrame(columns = [
            'tag_id',
            'tag_name',
        ])
        
        self.crypto_tag = pd.DataFrame(columns = [
            'crypto_id', 
            'tag_id',
        ])
        
        self.dates = pd.DataFrame(columns = [
            'date_id', 
            'date',
        ])
        
        self.crypto_price_types = pd.DataFrame({
            'crypto_price_type_id': [1, 2, 3, 4],
            'crypto_price_type_name': ['Open', 'Close', 'High', 'Low'],
        })
        
        
        self.crypto_daily_history = pd.DataFrame(columns = [
            'crypto_daily_id',
            'crypto_id',
            'date_id',
            'market_cap',
            'volume',
            'circulating_supply',
        ])
        
        self.crypto_price_times = pd.DataFrame(columns = [
            'crypto_price_time_id',
            'crypto_daily_id',
            'crypto_price_type_id',
            'crypto_price_time',
        ])
        
        self.crypto_historical_prices = pd.DataFrame(columns = [
            'id',
            'crypto_price_time_id',
            'crypto_price',  
        ])
                                                                            
    def read_raw_data(self, data_path=None):
        
        self.raw_data['CryptosTable'] = pd.read_csv(os.path.join(self.raw_data_path, 'Coins.csv'))
        
        file_name_template = '{}_9_5_2022-9_5_2023_historical_data_coinmarketcap.csv'
        path_template = os.path.join(self.raw_data_path, file_name_template)
        
        self.raw_data['CryptosHistoricalTables'] = []
        for _, row in self.raw_data['CryptosTable'].iterrows():
            path = path_template.format(row['Name'])
            crypto_historical_table = pd.read_csv(path, delimiter=';')
            self.raw_data['CryptosHistoricalTables'].append(crypto_historical_table)
            
    
    def write_transformed_data(self, data_path=None):
        if not os.path.exists(self.transformed_data_path):
            os.makedirs(self.transformed_data_path)
        for table_name in self.transformed_data:
            path = os.path.join(self.transformed_data_path, "{}.csv".format(table_name))
            self.transformed_data[table_name].to_csv(path, index=False)
    
    def transform(self):
        self.__transfrom_to_cryptocurrencies()
        self.__transform_to_tags()
        self.__transform_to_crypto_tag()
        self.__transform_to_dates()
        self.__transfrom_to_crypto_price_types()
        self.__transform_to_crypto_daily_history()
        self.__transform_to_crypto_price_times()
        self.__transform_to_crypto_historical_prices()
        
    def get_transformed_data(self):
        return self.transformed_data
        
    def get_cryptocurrencies(self):
        if self.cryptocurrencies.empty:
            self.__transfrom_to_cryptocurrencies()    
        return self.cryptocurrencies
        
    def get_tags(self):
        if self.tags.empty:
            self.__transform_to_tags()  
        return self.tags
    
    def get_crypto_tag(self):
        if self.crypto_tag.empty:
            self.__transform_to_crypto_tag()  
        return self.crypto_tag
    
    def get_dates(self):
        if self.dates.empty:
            self.__transform_to_dates()  
        return self.dates
    
    def get_crypto_price_types(self):
        if self.crypto_price_types.empty:
            self.__transfrom_to_crypto_price_types()  
        return self.crypto_price_types
    
    def get_crypto_daily_history(self):
        if self.crypto_daily_history.empty:
            self.__transform_to_crypto_daily_history()  
        return self.crypto_daily_history
    
    def get_crypto_price_times(self):
        if self.crypto_price_times.empty:
            self.__transform_to_crypto_price_times()  
        return self.crypto_price_times
    
    def get_crypto_historical_prices(self):
        if self.crypto_historical_prices.empty:
            self.__transform_to_crypto_historical_prices()  
        return self.crypto_historical_prices
    
    def __transfrom_to_cryptocurrencies(self):
        cryptocurrencies_data = []
        for index, row in self.raw_data['CryptosTable'].iterrows():  
            cryptocurrencies_data_row = (
                index + 1,
                row['Name'],
                row['Symbol'],
                row['MainLink'],
                row['HistoricalLink'],
                row['github_link'],
                row['Rank']
            )
            cryptocurrencies_data.append(cryptocurrencies_data_row)
        
        self.cryptocurrencies = pd.DataFrame(
            cryptocurrencies_data, 
            columns=self.cryptocurrencies.columns
        )  
        self.transformed_data['Cryptocurrencies'] = self.cryptocurrencies
        
        
    def __transform_to_tags(self):
        tag_names = []
        for index, row in self.raw_data['CryptosTable'].iterrows():
            tag_names += eval(row['tags'])
            
        tag_names = list(set(tag_names))
            
        tags_data = []
        for i, tag_name in enumerate(tag_names):
            tags_data_row = (
                i + 1,
                tag_name
            )
            tags_data.append(tags_data_row)

        self.tags = pd.DataFrame(tags_data, columns=self.tags.columns)
        self.transformed_data['Tags'] = self.tags

    def __transform_to_crypto_tag(self):
        crypto_tag_data = []
        for index, row in self.raw_data['CryptosTable'].iterrows():
            for tag_name in eval(row['tags']):
                crypto_tag_data_row = (
                    index + 1,
                    self.tags.loc[self.tags['tag_name'] == tag_name, 'tag_id'].values[0],
                )
                crypto_tag_data.append(crypto_tag_data_row)
        self.crypto_tag = pd.DataFrame(crypto_tag_data, columns=self.crypto_tag.columns)
        self.transformed_data['CryptoTag'] = self.crypto_tag


    def __transform_to_dates(self):
        dates_data = []
        for index, row in self.raw_data['CryptosHistoricalTables'][0].iterrows():
            date = dt.datetime.strptime(row['timeOpen'][:-1], '%Y-%m-%dT%H:%M:%S.%f').date()
            dates_data_row = (
                index + 1,
                date,
            )
            dates_data.append(dates_data_row)
        self.dates = pd.DataFrame(dates_data, columns=self.dates.columns)
        self.transformed_data['Dates'] = self.dates

    def __transfrom_to_crypto_price_types(self):
        self.transformed_data['CryptoPriceTypes'] = self.crypto_price_types
        
    
    def __transform_to_crypto_daily_history(self):
        crypot_daily_id = 0
        crypto_daily_history_data = []
        for crypto_index, _ in self.raw_data['CryptosTable'].iterrows():
            for history_index, history_row in self.raw_data['CryptosHistoricalTables'][crypto_index].iterrows():
                crypot_daily_id += 1
                crypto_daily_history_data_row = (
                    crypot_daily_id,
                    crypto_index + 1,
                    history_index + 1,
                    history_row['marketCap'],
                    history_row['volume'],
                    None, # histoery_row['circulatingSupply'],
                )
                crypto_daily_history_data.append(crypto_daily_history_data_row)

        self.crypto_daily_history = pd.DataFrame(
            crypto_daily_history_data, 
            columns=self.crypto_daily_history.columns,
        )
        self.transformed_data['CryptoDailyHistory'] = self.crypto_daily_history
        
    
    def __transform_to_crypto_price_times(self) -> None:
        crypot_daily_id = 0
        crypto_price_time_id = 0
        crypto_price_times_data = []
        for crypto_index, _ in self.raw_data['CryptosTable'].iterrows():
            for _, history_row in self.raw_data['CryptosHistoricalTables'][crypto_index].iterrows():
                crypot_daily_id += 1
                for price_types_index, price_types_row in self.transformed_data['CryptoPriceTypes'].iterrows():
                    crypto_price_type_id = price_types_index + 1
                    crypto_price_time_id += 1
                    price_type = price_types_row['crypto_price_type_name']
                    crypto_price_time = dt.datetime.strptime(history_row['time' + price_type][:-1], '%Y-%m-%dT%H:%M:%S.%f').time()
                    crypto_price_times_data_row = (
                        crypto_price_time_id,                
                        crypot_daily_id,
                        crypto_price_type_id,
                        crypto_price_time
                    )
                    crypto_price_times_data.append(crypto_price_times_data_row)

        self.crypto_price_times = pd.DataFrame(
            crypto_price_times_data, 
            columns=self.crypto_price_times.columns
        )  
        self.transformed_data['CryptoPriceTimes'] = self.crypto_price_times      
        
    
    def __transform_to_crypto_historical_prices(self):
        crypto_price_time_id = 0
        crypto_historical_prices_id = 0
        crypto_historical_prices_data = []
        for crypto_index, _ in self.raw_data['CryptosTable'].iterrows():
            for _, history_row in self.raw_data['CryptosHistoricalTables'][crypto_index].iterrows():
                for _, price_types_row in self.transformed_data['CryptoPriceTypes'].iterrows():
                    crypto_price_time_id += 1
                    price_type = price_types_row['crypto_price_type_name']
                    crypto_historical_prices_id += 1
                    crypto_price = history_row[price_type.lower()]   
                    crypto_historical_prices_data_row = (
                        crypto_historical_prices_id, 
                        crypto_price_time_id,
                        crypto_price,
                    )
                    crypto_historical_prices_data.append(crypto_historical_prices_data_row)

        self.crypto_historical_prices = pd.DataFrame(
            crypto_historical_prices_data, 
            columns=self.crypto_historical_prices.columns,
        )    
        self.transformed_data['CryptoHistoricalPrices'] = self.crypto_historical_prices      


def main():
    cdt = CryptoDataTransformer()
    cdt.read_raw_data()
    cdt.transform()
    cdt.write_transformed_data()

        
if __name__ == '__main__':
    main()