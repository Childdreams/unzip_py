# -
因为电脑是debian的其他同事电脑是windows
windows zip和debian的编码存在误差unzip命令没有-O命令
又不想多花时间去搞这个所以用python构建了一个解压包
- path 
    `/usr/sbin/unzip_py`
    
    mv ./unzip.py /usr/sbin/unzip_py
     
    chmod +x unzip_py
- 使用方式

    sudo sh install.sh
    
    unzip_py xxx.zip