import logging
import io
import azure.functions as func


def main(msg: func.QueueMessage, msgout: func.Out[func.QueueMessage], outputblob: func.Out[func.InputStream]) -> None:
    msg_in = msg.get_body().decode('utf-8')
    base, page = msg_in.split("page_")
    page_int = int(page)
    blob_body = io.StringIO(msg_in)
    outputblob.set(blob_body.getvalue())
    if page_int < 3:
        update_msg = f"{base}page_{page_int + 1}"
        msgout.set(update_msg)
