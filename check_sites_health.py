import requests
import argparse
import whois
import datetime
import sys
import os


def load_urls4check(path):
    if not os.path.exists(path):
        return None
    with open(path, encoding="utf=8") as file:
        text = file.read()
        urls_list = text.split("\n")
    return urls_list


def is_server_respond_with_200(url):
    try:
        r = requests.get(url)
    except requests.exceptions.RequestException as e:
        sys.exit(e)
    return r.ok


def get_domain_expiration_date(domain_name):
    domain_info = whois.query(domain_name)
    expiration_date = domain_info.expiration_date
    return expiration_date


def is_domain_prepaid_more_than_for_a_month(expiration_date):
    today = datetime.datetime.today()
    if expiration_date:
        delta = expiration_date - today
    else:
        return None
    month_forward_date = datetime.datetime(
        today.year,
        today.month+1,
        today.day
    )
    domain_prepaid_time = today + delta
    if month_forward_date < domain_prepaid_time:
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

if __name__ == '__main__':
    parser = get_input_argument_parser()
    args = parser.parse_args()
    filepath = args.file
    urls4check = load_urls4check(filepath)
    if not urls4check:
        exit("file not found")
    for url in urls4check:
        print(
            "{} respond with 200: {}".format(
                url,
                is_server_respond_with_200(url)
            )
        )
        domain_expiration_date = get_domain_expiration_date(url)
        print(
            "{} prepaid more than for a month: {}".format(
                url,
                is_domain_prepaid_more_than_for_a_month(domain_expiration_date)
            )
        )
