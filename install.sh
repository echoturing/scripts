#!/bin/bash

# 自动检测Mac芯片类型并安装对应版本的Miniconda
echo "正在检测系统架构..."

# 检测CPU架构
ARCH=$(uname -m)

# 根据架构选择下载链接
if [ "$ARCH" = "arm64" ]; then
    echo "检测到Apple Silicon (ARM64) 芯片"
    DOWNLOAD_URL="https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-arm64.sh"
    FILENAME="Miniconda3-latest-MacOSX-arm64.sh"
elif [ "$ARCH" = "x86_64" ]; then
    # 检查是否为Rosetta 2环境
    if [ "$(sysctl -in sysctl.proc_translated)" = "1" ]; then
        echo "检测到Intel芯片 (运行在Rosetta 2环境下)"
    else
        echo "检测到Intel芯片"
    fi
    DOWNLOAD_URL="https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh"
    FILENAME="Miniconda3-latest-MacOSX-x86_64.sh"
else
    echo "错误：不支持的架构 $ARCH"
    exit 1
fi

# 下载Miniconda安装脚本
echo "开始下载Miniconda安装程序..."
curl -O "$DOWNLOAD_URL"

# 验证下载是否成功
if [ ! -f "$FILENAME" ]; then
    echo "下载失败，无法找到安装脚本"
    exit 1
fi

# 添加执行权限
chmod +x "$FILENAME"

# 执行安装（自动模式，无需用户交互）
echo "开始安装Miniconda..."
bash "$FILENAME" -b -p "$HOME/miniconda"

# 添加到PATH环境变量
echo "配置环境变量..."
echo 'export PATH="$HOME/miniconda/bin:$PATH"' >> "$HOME/.bashrc"  # 针对bash

# 初始化conda
echo "初始化conda..."
"$HOME/miniconda/bin/conda" init bash

# 清理安装文件
echo "清理安装文件..."
rm "$FILENAME"

source ~/.bashrc

pip install pandas openpyxl

ln -s $PWD/random_excel_rows.py /usr/local/bin/random_excel_rows || true
chmod +x /usr/local/bin/random_excel_rows || true
echo "random_excel_rows install success"

random_excel_rows -h