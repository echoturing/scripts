## 安装 python



## 安装 pandas 和 openpyxl

```bash
pip install pandas openpyxl
```


## 使用
``` shell
#  获取表格里面 年龄>30 and 部门=="销售部" 的随机 5 行
python random_excel_rows.py demo_input.xlsx output.xlsx  --n 5 --filter '年龄>30 and 部门=="销售部"'

#  获取表格里面 部门 包含 销售 的随机 20% 数据
python random_excel_rows.py demo_input.xlsx output.xlsx  --frac 0.2 --filter '部门.str.contains("销售")'
```
## 