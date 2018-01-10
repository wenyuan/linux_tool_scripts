# linux\_tool\_scripts
## 简单介绍
一些在Linux环境下运行的工具脚本</br>

## 测试环境
Ubuntu 14.04.2</br>
python 2.7</br>
Centos 没验证过,后面看是否能用,如果不能用再做支持</br>


## 项目依赖
所有需要运行脚本的服务器都要安装
### ubuntu:

    python环境
    sudo apt-get install python-pip python-dev
    pip包
    sudo pip install -r requirements.txt

## 脚本功能以及使用方法
1.disk_check.py</br>
    功能: 检查服务器的磁盘使用状况,超出阈值(70%)后发送邮件产生告警</br>
    使用方法:

        fab -f disk_check.py check_disk

## 加入定时任务
### ubuntu:

    编辑定时任务
    crontab -e
    添加要执行的脚本
    0 */6 * * *  fab -f /{file_path}/linux_tool_scripts/disk_check.py check_disk &    # 每隔6小时执行一次disk_check.py
    运行定时任务
    sudo /etc/init.d/cron restart
    查看定时任务列表
    crontab -l
    查看定时任务日志
    tail cron /var/log/syslog


## 更新进度

-----------------------------2018-1-10----------------------------
<br/>
1.提交初期代码
<br/>
