# !/usr/bin/env python
# coding: utf-8

"""守护进程."""

# python模拟linux的守护进程
import sys
import os
import time
import atexit
from signal import SIGTERM

import run


class Daemon:
    """守护进程."""

    def __init__(self, pidfile, stdout='/tmp/watch_stdout.log',
                 stderr='/tmp/watch_error.log'):
        """守护进程.

        Args:
            pidfile (str): 存放进程号的文件
            stdout (str, optional): 存放 stdout 的文件.
            Defaults to '/tmp/watch_stdout.log'.
            stderr (str, optional): 存放 stderr 的文件.
            Defaults to '/tmp/watch_error.log'.

        """
        # 需要获取调试信息，改为stdout='/dev/stdout', stderr='/dev/stderr'，以root身份运行。
        self.stdout = stdout
        self.stderr = stderr
        self.pidfile = pidfile

    def _daemon(self):
        try:
            pid = os.fork()  # 第一次fork，生成子进程，脱离父进程
            if pid > 0:
                sys.exit(0)  # 退出主进程
        except OSError as exception:
            sys.stderr.write('fork #1 failed: %d (%s)\n' %
                             (exception.errno, exception.strerror))
            sys.exit(1)

        os.chdir("/")  # 修改工作目录
        os.setsid()  # 设置新的会话连接
        os.umask(0)  # 重新设置文件创建权限

        try:
            pid = os.fork()  # 第二次fork，禁止进程打开终端
            if pid > 0:
                sys.exit(0)
        except OSError as exception:
            sys.stderr.write('fork #2 failed: %d (%s)\n' %
                             (exception.errno, exception.strerror))
            sys.exit(1)

        # 重定向文件描述符
        sys.stdout.flush()
        sys.stderr.flush()
        stdin = open('/dev/null', 'r')
        stdout = open(self.stdout, 'ab+')
        stderror_file = open(self.stderr, 'ab+', 0)
        os.dup2(stdin.fileno(), sys.stdin.fileno())
        os.dup2(stdout.fileno(), sys.stdout.fileno())
        os.dup2(stderror_file.fileno(), sys.stderr.fileno())

        # 注册退出函数，根据文件pid判断是否存在进程
        atexit.register(self.delpid)
        pid = str(os.getpid())
        open(self.pidfile, 'w+').write('%s\n' % pid)

    def delpid(self):
        """Run your fun."""
        os.remove(self.pidfile)

    def start(self):
        """Run your fun."""
        # 检查pid文件是否存在以探测是否存在进程
        try:
            pid_file = open(self.pidfile, 'r')
            pid = int(pid_file.read().strip())
            pid_file.close()
        except IOError:
            pid = None

        if pid:
            message = 'pidfile %s already exist. Daemon already running!\n'
            sys.stderr.write(message % self.pidfile)
            sys.exit(1)

        # 启动监控
        self._daemon()
        self._run()

    def stop(self):
        """Run your fun."""
        # 从pid文件中获取pid
        try:
            pid_file = open(self.pidfile, 'r')
            pid = int(pid_file.read().strip())
            pid_file.close()
        except IOError:
            pid = None

        if not pid:  # 重启不报错
            message = 'pidfile %s does not exist. Daemon not running!\n'
            sys.stderr.write(message % self.pidfile)
            return

        # 杀进程
        try:
            while 1:
                os.kill(pid, SIGTERM)
                time.sleep(0.1)
                # os.system('hadoop-daemon.sh stop datanode')
                # os.system('hadoop-daemon.sh stop tasktracker')
                # os.remove(self.pidfile)
        except OSError as err:
            err = str(err)
            if err.find('No such process') > 0:
                if os.path.exists(self.pidfile):
                    os.remove(self.pidfile)
            else:
                print(str(err))
                sys.exit(1)

    def restart(self):
        """Run your fun."""
        self.stop()
        self.start()

    def _run(self):
        """Run your fun."""
        while True:
            # fp=open('/tmp/result','a+')
            # fp.write('Hello World\n')
            sys.stdout.write('%s:hello world\n' % (time.ctime(),))
            sys.stdout.flush()
            time.sleep(2)


class MyDaemon(Daemon):
    """定制类.

    Args:
        Daemon (Daemon): [description]

    """

    def _run(self):
        run.run()


if __name__ == '__main__':

    # 路径
    CURRENT_PATH = os.path.abspath('.')
    PID_PATH = os.path.join(CURRENT_PATH, '/tmp/watch_process.pid')
    STDOUT_PATH = os.path.join(CURRENT_PATH, '/tmp/watch_stdout.log')

    DAEMON = MyDaemon(pidfile=PID_PATH, stdout=STDOUT_PATH)

    if len(sys.argv) == 2:
        if sys.argv[1] == 'start':
            DAEMON.start()
        elif sys.argv[1] == 'stop':
            DAEMON.stop()
        elif sys.argv[1] == 'restart':
            DAEMON.restart()
        else:
            print('unknown command')
            sys.exit(2)
        sys.exit(0)
    else:
        print('usage: %s start|stop|restart' % sys.argv[0])
        sys.exit(2)
