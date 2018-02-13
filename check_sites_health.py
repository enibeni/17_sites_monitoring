import requests
import argparse
import whois
import datetime
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
        pass


def get_domain_expiration_date(domain_name):
    domain_info = whois.whois(domain_name)
    expiration_date = domain_info.expiration_date
    return expiration_date


def is_domain_prepaid(expiration_date, prepaid_for_days=30):
    if type(expiration_date) is list:
        expiration_date = expiration_date[0]

    today = datetime.datetime.today()
    if expiration_date:
        delta = expiration_date - today
    else:
        return None
    if delta.days > prepaid_for_days:
        return delta.days
    else:
        return 0


def get_input_argument_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-f",
        "--file",
        required=True,
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
        domain_expiration_dates = get_domain_expiration_date(url)
        prepaid_days = is_domain_prepaid(domain_expiration_dates)
        print(
            "{} respond status: {}".format(
                url,
                server_respond_status
            )
        )
        print(
            "{} prepaid for {} days".format(
                url,
                prepaid_days
            )
        )
