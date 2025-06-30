#!/usr/bin/env python3
import pandas as pd
import openpyxl
import argparse
import itertools
import math


def run(args):
    filtered_index_list = []
    if args.exclude:
        for exclude in args.exclude:
            exclude_df = pd.read_excel(exclude)
            indexes = exclude_df.iloc[:, 0]
            filtered_index_list.extend(filter(lambda x: x != "" and x is not None, indexes))

    df = pd.read_excel(args.input)
    if args.filter is not None:
        df = df.query(args.filter)
        print(f"after filtered, we have {len(df)} rows")

    if filtered_index_list:
        df = df.drop(index=filtered_index_list)
        print(f"after filtered {len(filtered_index_list)} index, we have {len(df)} rows")

    filters = []
    if args.m:
        for m in args.m:
            filters.append([f'{m}=="{e}"' for e in set(df[m])])

    if not filters:
        random_rows = df.sample(n=args.n) if args.n else df.sample(n=min(len(df), math.ceil(len(df) * args.frac)))
        random_rows.to_excel(args.output, index=True)
    else:
        cartesian_filters = list(itertools.product(*filters))
        print(cartesian_filters)
        res_list = []
        for f in cartesian_filters:
            f = " and ".join(f)
            filtered_df = df.query(f)
            random_rows = filtered_df.sample(n=args.n) if args.n else filtered_df.sample(n=min(len(filtered_df), math.ceil(len(filtered_df) * args.frac)))
            res_list.append(random_rows)
        res = pd.concat(res_list)
        res.to_excel(args.output, index=True)


def main():
    parser = argparse.ArgumentParser(description="从Excel文件中提取随机行")
    parser.add_argument("input", type=str, help="输入Excel文件的路径")
    parser.add_argument("output", type=str, help="输出Excel文件的路径")
    parser.add_argument("--m", nargs='*', help="多列笛卡尔积")
    parser.add_argument("--exclude", nargs='*', help="多列的时候是否把结果分开")
    parser.add_argument("--n", type=int, help="要提取的随机行数")
    parser.add_argument("--frac", type=float, help="要提取的随机行比例")
    parser.add_argument("--filter", type=str, help=r"过滤: 比如 A>10 and B=='abc' or 部门.str.contains('部')")
    args = parser.parse_args()
    if args.n is None and args.frac is None:
        parser.error("至少需要提供一个参数: --n 或 --frac")
    run(args)


if __name__ == "__main__":
    main()
