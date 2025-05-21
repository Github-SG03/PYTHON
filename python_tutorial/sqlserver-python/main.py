import logging, sys
from procedure import count_customer_by_email_domain


# config logging to console
logging.basicConfig(
    stream=sys.stdout, 
    encoding='utf-8', 
    format='%(levelname)s:%(message)s',
    level=logging.DEBUG
)

customer_count = count_customer_by_email_domain('gmail.com')
logging.info(customer_count)