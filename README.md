# Sites Monitoring Utility

Check site for positive response and domain payment status.

# Set up

Use pip to install dependencies
```bash
pip install -r requirements.txt
```

# Quickstart

Run this script with Python 3.x. As an required parameter -f, you should specify file with list of urls to check.
As an optional parameter -d, you can specify the amount of days to check domain prepaid status for.

Example of script launch on Linux, Python 3.5:

```bash
$ python check_sites_health.py -f urls_to_check.txt -d 90

https://www.github.com respond status: 200
https://www.github.com prepaid for period of 90 days: True
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
