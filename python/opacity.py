import tomlkit
import os
import sys

# 读取 Alacritty 配置文件
config_file = os.path.expanduser("~/.config/alacritty/alacritty.toml")

# 解析 TOML 文件
with open(config_file, 'r') as file:
    config = tomlkit.parse(file.read())

# 获取当前的 opacity 值
current_opacity = config.get('window', {}).get('opacity')

# 打印当前的 opacity 值
if current_opacity is not None:
    print(f"Current Opacity: {current_opacity}")
else:
    print("Opacity not found in the configuration file.")

# 读取命令行参数
if len(sys.argv) > 1:
    new_opacity = float(sys.argv[1])
else:
    print("Usage: python opacity.py <new_opacity>")
    sys.exit(1)

# 检查参数是否在有效范围内
if not (0 <= new_opacity <= 1):
    print("Opacity must be between 0 and 1")
    sys.exit(1)

# 修改配置文件中的 opacity 值
if 'window' in config:
    config['window']['opacity'] = new_opacity
else:
    config['window'] = {'opacity': new_opacity}

# 将修改后的配置写回文件
with open(config_file, 'w') as file:
    file.write(tomlkit.dumps(config))

# 打印修改后的 opacity 值
print(f"New Opacity: {new_opacity}")
