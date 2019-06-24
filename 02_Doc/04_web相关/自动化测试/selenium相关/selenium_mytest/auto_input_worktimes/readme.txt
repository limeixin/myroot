1、
下载浏览器驱动，放入此目录内。

如果使用Edge浏览器，则可以根据您电脑上的Edge浏览器版本号下载MicrosoftWebDriver.exe
MicrosoftWebDriver.exe下载地址：
https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/

如果是chrome浏览器：
http://chromedriver.storage.googleapis.com/index.html

如果是IE浏览器
IEdriver 下载地址：http://selenium-release.storage.googleapis.com/index.html


2、
设置cfg.ini配置
browser默认Edge，根据上边第一步的选择设置
账号密码请设置
[auto_level]中的stop_site可以设置，默认直接提交了，也可以设置成只填写而不提交。
datafile = ./worktimes.txt 默认用当前目录下worktimes.txt内容填写，你可以自己设置路径和文件名


3、
worktimes.txt文件中内容，请按格式填写。
如果填写错误，则会提交失败。
当前程序未做容错。

