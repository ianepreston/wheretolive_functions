import logging
# import io
from .scraper import get_listings_page, listings_page_to_df
import azure.functions as func


def main(msg: func.QueueMessage, msgout: func.Out[func.QueueMessage], outputblob: func.Out[func.InputStream]) -> None:
    msg_in = msg.get_body().decode('utf-8')
    base, page = msg_in.split("page_")
    page_int = int(page)
    listings_page = listings_page_to_df(get_listings_page(city_id=1, page=page_int))
    # blob_body = io.BytesIO()
    listings_page.to_parquet("listing.pq", engine="fastparquet")
    with open("listing.pq", "rb") as file:
        outputblob.set(file.read())
    if len(listings_page) > 0:
        update_msg = f"{base}page_{page_int + 1}"
        msgout.set(update_msg)
