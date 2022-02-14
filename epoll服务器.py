
"""
实现epoll服务器
"""

import select
from socket import *


# 套接字设置
s=socket.socket(AF_INET,SOCK_STREAM)
# 创建套接字
s.bind(('',1000)) # 套接字绑定
s.listen(120) # 设置监听

# epoll 对象的设置
epoll_list=select.epoll() # 创建epoll对象
epoll_list.register(s.fileno(),# 套接字的fd传入参数
select.EPOLLIN # EPOLLIN 表示 等待写入
)

# 注册套接字进入epoll检测对象
fd_sock={}
while True:
    list_fd_e=epoll_list.poll() # 阻塞 等待事件发生，并返回事件与fd
    for fd,e in list_fd_e:
        if s.fileno()==fd: # 如果是主套接字
            new,_ =s.accept()
            # 获取服务套接字
            epoll_list.register(new.fileno(),select.EPOLLIN) # 服务套接字加入epoll对象
            fd_sock[new.fileno()]=new 
        else:
            info=fd_sock[fd].recv(1024).decode('gbk')# 接受信息
            if info: # 信息不为空
                print(info)
            else:
                fd_sock[fd].close() # 关闭套接字
                epoll_list.unregister(fd) # 注销套接字
                del fd_sock[fd]
