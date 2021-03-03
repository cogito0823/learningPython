import os
import re
from datetime import datetime

import schedule


def split_log():
    date_now = str(datetime.now().date())
    grep_today_result = os.popen(f"cat watch_stdout.log | grep -an '^{date_now}' | head -n 1").read()
    print(grep_today_result)
    LINE_NUM, LOG_INFO = grep_today_result.split(':', 1)
    print(LINE_NUM)
    TIME_RE_FORMAT = r'([0-9]{3}[1-9]|[0-9]{2}[1-9][0-9]{1}|[0-9]{1}[1-9][0-9]{2}|[1-9][0-9]{3})-(((0[13578]|1[02])-(0[1-9]|[12][0-9]|3[01]))|((0[469]|11)-(0[1-9]|[12][0-9]|30))|(02-(0[1-9]|[1][0-9]|2[0-8])))\s([0-1][0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9])'
    COPY_LINE_COMMAND = f"sed -n '1,{int(LINE_NUM) - 1}p' watch_stdout.log > old.log"
    DELETE_LINES_COMMAND = f"sed -i '1,{int(LINE_NUM) - 1}d' watch_stdout.log"
    if re.match(TIME_RE_FORMAT, LOG_INFO):
        print(os.popen(COPY_LINE_COMMAND).read())
        print(os.popen(DELETE_LINES_COMMAND).read())

def pprint():
    print(str(datetime.now()))

if __name__ == "__main__":
    schedule.every().minutes.do(split_log)
    
    while True:
        schedule.run_pending()
