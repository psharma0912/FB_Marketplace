#testing
import pandas as pd
#function
def new_func(__name__):
    
    def obtain_tabular_data(file_path: str=r'C:\Users\psharma\AI_Core\Facebook_Marketplace\Products.csv', line_terminator: str=',') -> pd.DataFrame:
        '''A function that imports data from a .cvs file to a pandas data frame, and deletes all incomplete rows.
    Args:
        file_path (str): path from where the data is to be imported
        line_terminator (str): line terminator of the .cvs file, by default a comma (',').
    Returns:
        pd.DataFrame: data frame of all complete contents from the .cvs file
    '''

        products_df = pd.read_csv(file_path,  engine='python')
        print(products_df.head()) # uncomment to see original panda frame
        print(products_df.info())

        products_df = products_df.dropna() # deletes rows where at least 1 item is missing
        products_df.drop(['Unnamed: 0'], inplace=True, axis=1)
        print(products_df.head())
        print(products_df.info())
        return products_df
    # Call the function to see the printed output
    #obtain_tabular_data()

    def clean_price_column(price_column: pd.Series) -> pd.Series:
        #     """A function that takes a pandas series containing prices, removes pound symbols (£) and commas, 
        # then convert all values to floats.
        # Args:
        #     price_column (pd.Series): pandas series of prices in string format
        # Returns:
        #     pd.Series: pandas series of clean price data in float format
        # """
        products_df = obtain_tabular_data()
        price_column = products_df['price']
        
        # # cleaning
        price_column = price_column.str.strip('£')
        price_column = price_column.replace(',','', regex=True) # commas need to go to convert price string to float
        price_column = price_column.astype('float64')
         # Replace existing 'price' column with cleaned prices
        products_df['price'] = price_column
        
        # Print cleaned results and DataFrame info
        print(price_column.head())
        print(products_df.info())
        print(products_df['price'].head())
    
   
   # clean_price_column(pd.Series())        

    if __name__ == "__main__":
        clean_price_column(pd.Series)
    

new_func(__name__)

