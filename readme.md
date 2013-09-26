#IP修改器
##使用方法
###由于本应用程序为windows应用程序，因此需要安装python调用windows系统函数的模块 wmi 和 pywin32
##用途
###可以识别电脑的多块网卡，并可以分别对每块网卡常用的IP地址进行记录。IP的记录结果保存在与IPAdapter.py同级目录下的ipcfg文本中。
###程序可以判断网络当前的连接状态
##适用人群
###如果你经常需要更改IP，而又觉得windows设置IP的过程比较繁琐，那么相信我这款IP修改器一定能够帮你减少一些麻烦
##有待改进
###本程序界面部分采用wxpython，而主要逻辑部分则是依赖wmi模块，本人对于wmi的使用主要来自网络分享，因此有许多理解不透彻的地方，代码里关于网络连接状态的判断也比较暴力，就是开一个线程不停地判断连接状态，如果您有好的意见和建议，欢迎随时指教，谢谢大家！
###这个工具大约是我一年前开发的，今天第一次把它放到github里，一来是受开源魅力的吸引，二来也是给我的技术生活添彩。本人能力有限，有不当之处还请多多包涵赐教。