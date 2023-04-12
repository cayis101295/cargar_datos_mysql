import read_data
import conn_data_base 

def run():
    data_amazon_reviews = read_data.parse_csv_data_frame("amazon_reviews.csv", ['reviewerName', 'overall', 'reviewText', 'reviewTime'])
    conn = conn_data_base.connect_data_base()
    conn_data_base.load_data_amazon()
    conn_data_base.load_data(data_amazon_reviews)
    data_amazon_ufo= read_data.parse_csv_data_frame("nuforc_reports.csv", ['level_0', 'index', 'text'])
    conn_data_base.load_data(data_amazon_reviews)

if __name__ == "__main__":
    run()

