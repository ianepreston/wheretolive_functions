import logging
# import io
from .scraper import get_listings_page, listings_page_to_df
import azure.functions as func


def main(msg: func.QueueMessage, msgout: func.Out[func.QueueMessage], outputblob: func.Out[func.InputStream]) -> None:
    logging.info("Starting rentfaster queue")
    msg_in = msg.get_body().decode('utf-8')
    logging.info(f"Message received: {msg_in}")
    base, page = msg_in.split("page_")
    page_int = int(page)
    listings_json = get_listings_page(city_id=1, page=page_int)
    if not listings_json:
        logging.info(f"Page {page_int} is empty, no more listings")
    else:
        listings_page = listings_page_to_df(listings_json)
        logging.info(f"Retrieved listings page of shape {listings_page.shape}")
        listings_page.to_parquet("listing.pq", engine="fastparquet")
        with open("listing.pq", "rb") as file:
            outputblob.set(file.read())
        update_msg = f"{base}page_{page_int + 1}"
        msgout.set(update_msg)
