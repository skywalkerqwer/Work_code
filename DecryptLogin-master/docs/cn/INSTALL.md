# 安装

## 测试环境
本人测试时使用的环境如下:
- 操作系统: Win10
- Python版本: 3.6.4

## 依赖包 
DecryptLogin相关依赖包需求如下:
```
rsa >= 4.0
requests >= 2.22.0
pycryptodome >= 3.8.1
PyExecJS >= 1.5.1 (测试时使用的Node.js版本为v10.15.3)
```

## PIP安装
在终端运行如下命令即可(请保证python在环境变量中):
```sh
pip install DecryptLogin --upgrade
```

## 源代码安装
#### 在线安装
运行如下命令即可在线安装:
```sh
pip install git+https://github.com/CharlesPikachu/DecryptLogin.git@master
```
#### 离线安装
利用如下命令下载DecryptLogin源代码到本地:
```sh
git clone https://github.com/CharlesPikachu/DecryptLogin.git
```
接着, 切到DecryptLogin目录下:
```sh
cd DecryptLogin
```
最后运行如下命令进行安装:
```sh
python setup.py install
```