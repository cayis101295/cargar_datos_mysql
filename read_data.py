import pandas as pd

def parse_csv_data_frame():
    data_amazon_reviews = pd.read_csv('amazon_reviews.csv', index_col=False, delimiter = ',')
    data_amazon_reviews = data_amazon_reviews[['reviewerName', 'overall', 'reviewText', 'reviewTime']]
    data_amazon_reviews = data_amazon_reviews.dropna()
    print(data_amazon_reviews.head())
    return data_amazon_reviews