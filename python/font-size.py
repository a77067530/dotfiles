import tomlkit
import os
import sys

# ANSI 转义序列
GREEN = "\033[92m"
RESET = "\033[0m"

# 读取 Alacritty 配置文件
config_file = os.path.expanduser("~/.config/alacritty/alacritty.toml")

# 解析 TOML 文件
with open(config_file, 'r') as file:
    config = tomlkit.parse(file.read())

# 获取当前的 font size
current_size = config.get('font', {}).get('size')

# 打印当前的 font size
if current_size is not None:
    print(f"Current Font Size: {current_size}")
else:
    print("Font size not found in the configuration file.")

# 读取命令行参数
if len(sys.argv) > 1:
    new_size = float(sys.argv[1])
else:
    print("Usage: python font_size.py <new_size>")
    sys.exit(1)

# 检查输入的 size 是否有效
if new_size <= 0:
    print("Font size must be greater than 0.")
    sys.exit(1)

# 修改配置文件中的 font size
if 'font' in config:
    config['font']['size'] = new_size
else:
    config['font'] = {'size': new_size}

# 将修改后的配置写回文件
with open(config_file, 'w') as file:
    file.write(tomlkit.dumps(config))

# 打印修改后的 font size
print()  # 换行
print(f"{GREEN}New Font Size: {new_size}{RESET}")
