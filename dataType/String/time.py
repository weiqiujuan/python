import time

print(time.time())  # 时间戳
print(time.ctime())  # 时间
print(time.gmtime())  # 其他程序可利用的

t = time.gmtime()
print(time.strftime("%Y-%m-%d %H:%M:%S", t))

timeStr = '2018-11-03 06:35:59'
print(time.strptime(timeStr))
