# Jupyter Switch

[![PyPI version](https://badge.fury.io/py/jupyter-switch.svg)](https://badge.fury.io/py/jupyter-switch)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

一个强大、轻量且直观的工具，可在 Markdown (.md) 和 Jupyter Notebook (.ipynb) 格式之间无缝转换。

## ✨ 功能特性

- 🚀 **自动检测**：自动检测输入文件是 `.md` 还是 `.ipynb` 并相应转换
- 🔄 **双向转换**：支持从 Markdown 转换为 Jupyter Notebook，反之亦然
- 🛡️ **备份保护**：当输出文件已存在时自动创建备份
- 📋 **保持结构**：保留代码块、markdown 内容和单元格结构
- 🔧 **MCP 集成**：可作为 MCP 服务器工具供 AI 助手使用

## 📦 CLI 使用

### 安装和执行（推荐的方法）⚡️

[`uvx`](https://docs.astral.sh/uv/concepts/tools/) 会自动安装包并运行命令。

```bash
# Convert example.md to example.ipynb
uvx jupyter-switch example.md

# Convert example.ipynb to example.md
uvx jupyter-switch example.ipynb
```

### 用 pip 安装和执行（不推荐）

使用 pip 安装：

```bash
pip install jupyter-switch
```

然后执行命令：

```bash
# Convert example.md to example.ipynb
jupyter-switch example.md

# Convert example.ipynb to example.md
jupyter-switch example.ipynb
```

注意：与 `uvx` 在一条命令中完成安装和执行不同，`pip` 需要先单独安装。

工具会自动：
- 检测输入文件格式
- 生成相应的输出文件名
- 如果输出文件已存在则创建备份
- 在保持结构的同时转换内容

### 帮助 🆘

```bash
jupyter-switch --help
jupyter-switch --version
```

## 🤖 MCP 工具使用（推荐用于 AI 助手）

本包提供了一个 MCP（Model Context Protocol）服务器，可与 Claude 等 AI 助手配合使用。

### 安装为 MCP 服务器

添加到您的 MCP 设置配置中：

```json
{
  "mcpServers": {
    "jupyter-switch": {
      "command": "uvx",
      "args": ["--from", "jupyter-switch", "jupyter-switch-mcp"]
    }
  }
}
```

### 可用工具

- **`switch_file`**：根据输入文件扩展名自动在 `.md` 和 `.ipynb` 格式之间转换

### 推荐的 .ipynb 编辑工作流

1. **转换为 Markdown**：使用 `switch_file` 工具将 `.ipynb` → `.md` 以便于编辑
2. **编辑**：使用您喜欢的编辑器修改 `.md` 文件
3. **转换回来**：完成后再次使用工具将 `.md` → `.ipynb`

### 示例

```
"使用 jupyter-switch 将此 notebook 翻译成法语"
```

## 转换详情 🔄

### Markdown 转 Jupyter Notebook
- Python 代码块（```python...```）变为代码单元格
- 所有其他内容变为 markdown 单元格
- 添加适当的 notebook 元数据和结构

### Jupyter Notebook 转 Markdown
- 代码单元格变为 Python 代码块
- Markdown 单元格保持不变
- 转换时忽略单元格输出

## 要求 🐍

- Python >= 3.10

## 许可证 📄

MIT License
