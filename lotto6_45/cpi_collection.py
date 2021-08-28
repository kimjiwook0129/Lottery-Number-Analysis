# https://www.index.go.kr/potal/stts/idxMain/selectPoSttsIdxSearch.do?idx_cd=1060&stts_cd=106001&freq=Y


import pandas as pd
import requests
import re
from bs4 import BeautifulSoup
import sqlite3


def recentDraw():
    request = requests.get(lotto_result_url)
    soup = BeautifulSoup(request.text, "lxml")
    content = soup.find("meta", {"id": "desc", "name": "description"})[
        'content']
    drawCount = re.compile(r'\d+회')
    mo = drawCount.search(content)
    return int(mo.group()[:-1])


if __name__ == "__main__":
    db_path = "cpi.db"
    mostRecentCPI = recentCPI()
    mostRecentCPIDB = recentCPIDB(db_path)

    # sql_draw_create = """CREATE TABLE IF NOT EXISTS `CPI`(date int, cpi int, UNIQUE(date))"""
