import pandas as pd

def parse_csv_data_frame(name, columns):
    data_amazon_reviews = pd.read_csv(name, index_col=False, delimiter = ',')
    data_amazon_reviews = data_amazon_reviews[columns]
    data_amazon_reviews = data_amazon_reviews.dropna()
    print(data_amazon_reviews.head())
    return data_amazon_reviews