import time
from mods import web

a = 5

def main():
    global a
    b = input('[timo]请输入指令:')

    if b == 't.exit':
        for c in range(5):
            print('[timo]还有' + str(a) + '秒关闭timo')
            time.sleep(1)
            a -= 1
    elif b == 't.stytime':
        print('[timo]现在的sky时间是:' + time.asctime())
        main()
    elif b == 't.time':
        print('[timo]现在的时间是:' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
        main()
    elif b == 'w.github':
        web.github()
        main()
    elif b == 'w.other':
        d = input('[timo]请问您要访问什么:')
        web.other(d)
        main()
main()