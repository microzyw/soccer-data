### install ###
install python-3.6.5-amd64
    must include pip
pip config list
    pip.ini -> 保存位置为%USERPROFILE%\pip\pip.ini(%USERPROFILE%具体指的是什么目录，可以cmd命令行中输入set查看)
        [global]
        index-url = http://mirrors.aliyun.com/pypi/simple/
        [install]
        trusted-host = mirrors.aliyun.com
pip install Flask

### use inner server ###
set FLASK_APP=index.py
set FLASK_ENV=development
flask run --host=0.0.0.0
http://127.0.0.1:5000/

### UI Template
https://weui.shanliwawa.top/weui/
https://weui.io/

### use Apache server ###
1.判断python版本和vc版本关系
    用Python命令查看MSC对应的版本，去下载对应VC程序
        Visual C++ 2005  (8.0)   MSC_VER=1400
        Visual C++ 2008  (9.0)   MSC_VER=1500
        Visual C++ 2010 (10.0)   MSC_VER=1600
        Visual C++ 2012 (11.0)   MSC_VER=1700
        Visual C++ 2013 (12.0)   MSC_VER=1800
        Visual C++ 2015 (14.0)   MSC_VER=1900
        Visual C++ 2017 (15.0)   MSC_VER=1910
2.安装Apache，直接选择编译好的windows版本
  https://www.apachehaus.com/cgi-bin/download.plx
  ※选择对应VC版本、64位版本
  将压缩包下载到本机，解压到需要的目录：D:\Apache24
  启动服务：httpd
  输入地址访问：http://localhost/，查看是否安装成功
  ※cd /d D:\Apache24\bin
  ※httpd
3.安装mod_wsgi
  下载编译好的 mod_wsgi 
    https://www.lfd.uci.edu/~gohlke/pythonlibs/#mod_wsgi
    mod_wsgi-4.7.1-cp36-cp36m-win_amd64.whl
  把下载的.whl文件复制到python\Scripts下,用pip进行安装
    pip install "mod_wsgi-4.7.1-cp36-cp36m-win_amd64.whl"
  安装成功后在python的安装目录的\scripts文件夹下运行
    mod_wsgi-express module-config
  将执行mod_wsgi-express module-config后控制台中显示的这三行内容拷贝到 http.conf 中，添加到其他的 loadmodule后
  重新启动Apache
修改apache配置
  打开 httpd.conf 文件，在最后添加虚拟环境：
    <VirtualHost *>
  	    ServerName example.com
  	    WSGIScriptAlias / D:/SVN/source/python/soccer-data-scan/index.wsgi
        <Directory D:/SVN/source/python/soccer-data-scan>
            Require all granted
        </Directory>
    </VirtualHost>
  重启Apache
  
### backup ###
$.ajax({
    async : false,
    type : "post",
    url : "/login/submitlogin",
    dataType : "json",
    success: function (data) {
         $.hideLoading();
    },
    error:function (data) {
         $.hideLoading();
    }
}); 