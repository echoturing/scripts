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

#  按 部门和性别 取笛卡尔积 , 笛卡尔积作为过滤条件分别取 50% 后合并结果并返回
python random_excel_rows.py demo_input.xlsx output.xlsx --m 部门 性别 --frac 0.5

#  跟上边一样,只是在 过滤掉 out1.xlsx 和 out2.xlsx 在 demo_input.xlsx 里的索引(0 开始) 后再操作
python random_excel_rows.py demo_input.xlsx output.xlsx --m 部门 性别 --frac 0.5 --exclude out1.xlsx out2.xlsx
```
## 