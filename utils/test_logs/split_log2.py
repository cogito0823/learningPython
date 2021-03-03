import os
import re
import time

from datetime import datetime, timedelta

from apscheduler.schedulers.background import BackgroundScheduler


def split_log(log_path):
    log_path = os.path.abspath(log_path)
    LOG_DIR = os.path.dirname(log_path)
    LOG_NAME = os.path.basename(log_path)
    date_now = datetime.now()
    date_yestoday = date_now - timedelta(days=1)
    yestoday_log_name = f"{str(date_yestoday.date())}.log"
    yestoday_log_path = os.path.join(LOG_DIR, yestoday_log_name)

    grep_today_result = os.popen(f"cat {log_path} | grep -an '^{str(date_now.date())}' | head -n 1").read()
    print(f"cat {log_path} | grep -an '^{str(date_now.date())}' | head -n 1")
    print(grep_today_result)
    if ':' in grep_today_result:
        LINE_NUM, LOG_INFO = grep_today_result.split(':', 1)
        if LINE_NUM == '1':
            print("没有更早日期的日志，无须分割文件")
            return False
    else:
        print("文件错误，没有今天的日志信息")
        return False
    
    TIME_RE_FORMAT = r'([0-9]{3}[1-9]|[0-9]{2}[1-9][0-9]{1}|[0-9]{1}[1-9][0-9]{2}|[1-9][0-9]{3})-(((0[13578]|1[02])-(0[1-9]|[12][0-9]|3[01]))|((0[469]|11)-(0[1-9]|[12][0-9]|30))|(02-(0[1-9]|[1][0-9]|2[0-8])))\s([0-1][0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9])'
    COPY_LINE_COMMAND = f"sed -n '1,{int(LINE_NUM) - 1}p' {log_path} > {yestoday_log_path}"
    DELETE_LINES_COMMAND = f"sed -i '1,{int(LINE_NUM) - 1}d' {log_path}"
    
    if re.match(TIME_RE_FORMAT, LOG_INFO):
        print(os.popen(COPY_LINE_COMMAND).read())
        print(os.popen(DELETE_LINES_COMMAND).read())
    else:
        print("日志内容匹配错误，切割失败")


def job():
    split_log("watch_stdout.log")

if __name__ == "__main__":
    split_log("watch_stdout.log")
    sched = BackgroundScheduler(timezone="MST")
    sched.add_job(job, 'interval', id='3_second_job', seconds=3)
    sched.start()

    while True:
        print('main 1s')
        time.sleep(1)
