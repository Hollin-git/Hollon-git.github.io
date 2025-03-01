---
title: 提交
---

项目部署
1. 下载本地项目 
git clone https://gitee.com/luhollin/svc-network.git


2. 安装python依赖包
安装mkdocs 和 主题  material mkdocs-material
还有python 注释解析包 mkdocstrings， "mkdocstrings[python]"

pip install mkdocs
pip install material
pip install mkdocs-material
pip install mkdocstrings 
pip install "mkdocstrings[python]"





```shell
1. 本地没有.git目录 远程服务器已创建项目 
cd project_dir
git init
git add .
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/Hollin-git/Hollon-git.github.io.git
git push -u origin main all


2. 本地有.git目录 远程服务器已创建项目 

git remote rename origin old-origin 
git remote add origin https://github.com/Hollin-git/Hollon-git.github.io.git
git push -u origin --all 
git push -u origin --tags




$ git config --global user.name "hollin"
$ git config --global user.email 329964085@qq.com





3. 本地有多个分支   远程服务器已创建项目main 
git remote add origin https://github.com/Hollin-git/Hollon-git.github.io.git
git branch -M main
git push -u origin main


4. ---
echo "# Hollon-git.github.io" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/Hollin-git/Hollon-git.github.io.git
git push -u origin main

```

// 书签
<!-- 
##超链接 到其他文档 
See my [About](/about/authorauthor.md) page for details. 

## 添加图片 其中 img 目录不会显示 可能是这个主题这样设定的 也可能是 mkdocs 预留目录img 
![tupian](img/ip2.png)

--> 
