import logging
import datetime as dt

import azure.functions as func


def main(timer: func.TimerRequest, msg: func.Out[func.QueueMessage]) -> None:
    utc_timestamp = dt.datetime.utcnow().replace(tzinfo=dt.timezone.utc).isoformat()
    if timer.past_due:
        logging.info('The timer is past due!')
    logging.info('Python timer trigger function ran at %s', utc_timestamp)
    logging.info("Triggering initial queue")
    q_text = f"rfaster_{dt.date.today()}_page_1"
    logging.info(f"Setting rfaster queue: {q_text}")
    msg.set(q_text)
    logging.info("Rentfaster queue set")