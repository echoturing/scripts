try:
    import pandas as pd
    import openpyxl
except ImportError as e:
    missing_pkg = str(e).split(' ')[-1].strip("'")
    print(f"缺少依赖包 {missing_pkg}，请运行命令：pip install pandas openpyxl")
    exit(1)

import argparse
import random


def main():
    parser = argparse.ArgumentParser(description="从Excel文件中提取随机行")
    parser.add_argument("input", type=str, help="输入Excel文件的路径")
    parser.add_argument("output", type=str, help="输出Excel文件的路径")
    parser.add_argument("--n", type=int, help="要提取的随机行数")
    parser.add_argument("--frac", type=float, help="要提取的随机行比例")
    parser.add_argument("--filter", type=str, help=r"""过滤: 比如 A>10 and B=='abc' or 部门.str.contains("部")""")
    args = parser.parse_args()
    if args.n is None and args.frac is None:
        parser.error("至少需要提供一个参数: --n 或 --frac")
    f = args.filter
    df = pd.read_excel(args.input)
    if filter is not None:
        df = df.query(args.filter)
        print("after filted , we have {} rows".format(len(df)))
    if args.n is not None:
        random_rows = df.sample(n=args.n)
    else:
        random_rows = df.sample(frac=args.frac)
    if len(df) == 0:
        print("no rows after filtered")
        return
    print(random_rows)
    random_rows.to_excel(args.output, index=False)


if __name__ == "__main__":
    main()
