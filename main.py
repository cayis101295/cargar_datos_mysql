import read_data
import conn_data_base 

def run():
    data_amazon_reviews = read_data.parse_csv_data_frame()
    conn = conn_data_base.connect_data_base()
    conn_data_base.create_data_base()
    conn_data_base.load_data( data_amazon_reviews)

if __name__ == "__main__":
    run()

