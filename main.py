import read_data
import conn_data_base 

def run():
    data_amazon_reviews = read_data.parse_csv_data_frame("amazon_reviews.csv", ['reviewerName', 'overall', 'reviewText', 'reviewTime'])
    conn = conn_data_base.connect_data_base()
    conn_data_base.load_data_amazon(data_amazon_reviews)
    data_amazon_ufo = read_data.parse_csv_data_frame("nuforc_reports.csv", ['level_0', 'text', 'stats'])
    conn_data_base.load_data_ufo(data_amazon_ufo)

if __name__ == "__main__":
    run()

