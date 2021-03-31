## 搭建Git环境
（1）Git全局设置
```
git config --global user.name "ASxx" 
git config --global user.email "123456789@qq.com"
```
（2）进入项目目录
```
cd tech-stack
```
（3）Git初期化
```
git init
```
（4）设置远程仓库地址
```
git remote add origin https://github.com/microzyw/soccer-data.git
```
（5）拉取代码
```
git pull https://github.com/microzyw/soccer-data.git master
```
（6）提交代码
```
git add README.md 
git commit -m "first commit" 
```
（7）上传代码
```
git push -u origin master
```