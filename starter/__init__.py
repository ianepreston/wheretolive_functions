import logging
import datetime as dt

import azure.functions as func


def main(req: func.HttpRequest, msg: func.Out[func.QueueMessage]) -> str:
    logging.info("Triggering initial queue")
    q_text = f"rfaster_{dt.date.today()}_page_1"
    msg.set(q_text)
    return func.HttpResponse("Set initial queue counter")