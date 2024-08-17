{% docs __overview__ %}
# dbt 实验项目 1.1.0

本项目用于调研 dbt 的各种功能特性

为了更方便的演示，target 数据库使用的 [Duckdb](https://duckdb.org/) 。所以本项目没有任何数据库依赖，可以直接运行。

```shell
# 创建数据源
tox -e jafgen
# 创建开发环境
tox -e dev
# 设置.tox/dev/ 为 IDE 默认Python解释器或者
source .tox/dev/bin/activate
# 运行 dbt 项目
dbt run
# 本地查看当前版本文档
tox -e serve
```

- [CHANGELOG](https://github.com/JiaweiData/dbt-learning/blob/main/CHANGELOG.md)


{% enddocs %}
