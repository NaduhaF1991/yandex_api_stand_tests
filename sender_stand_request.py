import requests
import configuration
import data

def get_docs():
    return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)
def get_logs():
    return requests.get(configuration.URL_SERVICE + configuration.LOG_MAIN_PATH, params={"count":20})

def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)

def post_new_user(body):
    return requests.post(url=configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=data.user_body,
                         headers=data.headers)

def post_products_kits(products_ids):
    return requests.post(url=configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH,
                         json=data.product_ids,
                         headers=data.headers)



