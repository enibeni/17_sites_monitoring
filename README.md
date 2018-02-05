# Sites Monitoring Utility

Check site for positive response and domain payment status.

# Set up

Use pip to intall dependencies
```bash
pip install -r requirements.txt
```

# Quickstart

Run this script with Python 3.x. As an optional parameter -f, you could specify file with list of urls to check.
By default script reads the file in it's directory.

Example of script launch on Linux, Python 3.5:

```bash
$ python check_sites_health.py

http://www.vk.com respond status: 200
http://www.vk.com prepaid more than for a month: True
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
