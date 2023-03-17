# MassLandlords Scraper

<img width="421" alt="mll_screenshot" src="https://user-images.githubusercontent.com/10646361/225936089-c8fa5233-72bd-46c2-b211-99d2ddf37e51.png">

An exremely simple Python scraper to collect weekly [eviction filing counts from MassLandlords](https://masslandlords.net/policy/eviction-data/). We use these counts to validate the number of filings we're retrieving using our [filing downloader tool](https://github.com/Unnamed-Lab-DUSP/filing_downloader). 

It fetches all counts starting from the week ending 10-24-2020 and continuing through the most recent available week.

It's extremely simple---its only requirement is the `requests` library. Per usual, get started by creating a python environment, activating it, and installing requirements.

```bash
python -m venv ./venv
source ./venv
python -m pip install -r requirements.txt
python ./scraper.py
```
