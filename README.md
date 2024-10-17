# dotfiles
使用zsh、alacritt等工具的配置文件。

使用修改文字大小等功能使用python脚本，所以要先安装python。
1. 安装python
```shell
brew install python
sudo ln -sf $(which python3) /usr/local/bin/python
sudo ln -sf $(which pip3) /usr/local/bin/pip
```

2. 因为 `toml` 库在写入配置文件时，默认不会保留原始文件中的注释和格式。为了保留注释和格式，你可以使用 `tomlkit` 库，它是一个兼容 `toml` 的库，可以保留注释和格式。
安装python tomlkit
```shell
python -m venv ~/venv
source ~/venv/bin/activate
pipx install tomlkit
deactivate
```

## Installation
```shell
git clone git@github.com:a77067530/dotfiles.git ~/.dotfiles
```

### 1. alacritty配置文件
```shell
ln -sf ~/.dotfiles/alacritty/alacritty.toml ~/.config/alacritty
ln -sf ~/.dotfiles/alacritty/themes ~/.config/alacritty/
```

### 2. zsh配置文件
```shell
ln -sf ~/.dotfiles/zsh/.zshrc ~/.zshrc
source ~/.zshrc
```


## Update Version
[2024.10.17]
- 新增修改文字大小
- 新增修改Alacritty主题等功能
- 增加zsh配置文件

[2024.10.17]
- Alacritty配置文件初始版本