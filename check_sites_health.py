import requests
import argparse
import whois
import datetime
from datetime import timedelta
import os


def load_urls4check(path):
    if not os.path.exists(path):
        return None
    with open(path) as file:
        text = file.read()
        urls_list = text.split("\n")
    return urls_list


def get_server_respond_code(url):
    try:
        response_code = requests.get(url).status_code
        return response_code
    except requests.exceptions.RequestException:
        response_code = None
        return response_code


def get_domain_expiration_date(domain_name):
    domain_info = whois.query(domain_name)
    expiration_date = domain_info.expiration_date
    return expiration_date


def is_domain_prepaid(expiration_date, prepaid_for_days=30):
    today = datetime.datetime.today()
    if expiration_date:
        delta = expiration_date - today
    else:
        return None
    expiration_time = timedelta(days=prepaid_for_days)
    if expiration_time < delta:
        return True


def get_input_argument_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-f",
        "--file",
        required=False,
        default="urls_to_check.txt",
        help="Path to input file with urls"
    )
    return parser

if __name__ == "__main__":
    parser = get_input_argument_parser()
    args = parser.parse_args()
    filepath = args.file
    urls4check = load_urls4check(filepath)
    if not urls4check:
        exit("file not found")
    for url in urls4check:
        server_respond_status = get_server_respond_code(url)
        if not server_respond_status:
            print("error getting {} status".format(url))
        domain_expiration_date = get_domain_expiration_date(url)
        domain_payment_status = is_domain_prepaid(domain_expiration_date)
        print(
            "{} respond status: {}".format(
                url,
                server_respond_status
            )
        )
        print(
            "{} prepaid more than for a month: {}".format(
                url,
                domain_payment_status
            )
        )
