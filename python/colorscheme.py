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

# 获取当前使用的主题
current_theme = None
imports = config.get('import', [])
for import_path in imports:
    if 'themes' in import_path:
        current_theme = os.path.basename(import_path).replace('.toml', '')
        break

# 打印当前使用的主题
if current_theme:
    print(f"{GREEN}Current Theme: {current_theme}{RESET}")
else:
    print("No theme is currently set.")

# 主题文件目录
themes_dir = os.path.expanduser("~/.config/alacritty/themes/themes")

# 列出目录中的所有 .toml 文件
theme_files = [f.replace('.toml', '') for f in os.listdir(themes_dir) if f.endswith('.toml')]

# 检查是否找到主题文件
if not theme_files:
    print("No theme files found in the directory.")
    exit(1)

# 按忽略大小写的字母顺序排序
theme_files.sort(key=str.casefold)

# 计算每列的宽度
max_width = max(len(theme) for theme in theme_files) + 2  # 加上一些填充

# 按四列打印主题文件的名称
print("\nAvailable Themes:")
for i in range(0, len(theme_files), 4):
    row = theme_files[i:i+4]
    print(''.join(f"{theme:<{max_width}}" for theme in row))

# 读取命令行参数
if len(sys.argv) > 1:
    new_theme = sys.argv[1]
else:
    sys.exit(0)

# 检查输入的主题是否存在
if new_theme not in theme_files:
    print(f"Theme '{new_theme}' not found.")
    sys.exit(1)

# 替换配置文件中的主题
for i, import_path in enumerate(imports):
    if 'themes' in import_path:
        imports[i] = f"~/.config/alacritty/themes/themes/{new_theme}.toml"
        break

# 将修改后的配置写回文件
config['import'] = imports
with open(config_file, 'w') as file:
    file.write(tomlkit.dumps(config))

# 打印修改后的主题
print()  # 换行
print(f"{GREEN}New Theme: {new_theme}{RESET}")
