# Welcome to MkDocs

For full documentation visit [mkdocs.org](https://www.mkdocs.org).

## 命令 

* `mkdocs new [dir-name]` - 创建一个项目.
* `mkdocs serve` - 开始本地服务 端口8000
* `mkdocs build` -构建项目 --clean 清除之前的缓存.
* `mkdocs -h` - 打印帮助信息.

## 路径

* `docs` - 存放文档的目录.
* `mkdocs.yml` - 配置文件.
* `site` - 构建文档的输出目录.

# **请去留言板留言。**
### 函数
```SQL
-- 需要设置 python的 PythonPath 参数 不然找不到模块 src.test
-- 设置方法 命令行执行 下面命令
$Env:PYTHONPATH="D:\Cloud\blog\mkdocs-prod\Hollon-git.github.io"
1. 拥有mkdocs环境
2. pip install mkdocstrings[python] 
3. 配置文件mkdocs.yml中添加mkdocstrings插件【一级标签】
plugins:
- mkdocstrings: 
    handlers: 
      python: 
        paths: [src]
4. 在md文件中添加::: src.test
5. 执行mkdocs serve
6. 访问http://127.0.0.1:8000/

```
::: src.test

--- 

::: src.mymodule
