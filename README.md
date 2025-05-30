# 简单链接收集器

一个超简单的 Web 应用，允许用户通过网页提交和查看链接（例如书签或资源列表）。本项目使用 Python 和 Flask 构建，适合初学者学习 Web 开发。

## 功能
- 通过网页添加链接。
- 显示所有已保存的链接。
- 简单易用的代码库，欢迎开源贡献。

## 安装
1. 克隆仓库：
   ```bash
   git clone https://github.com/myvless/simple-link-collector.git
   cd simple-link-collector
   ```
2. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```
3. 运行应用：
   ```bash
   python app.py
   ```
4. 在浏览器打开：
   ```bash
   http://localhost:5000
   ```

## 贡献
欢迎贡献！请阅读 [CONTRIBUTING.md](CONTRIBUTING.md) 了解如何参与。

## 开发计划
- [ ] 添加链接删除功能。
- [ ] 支持链接分类。
- [ ] 添加 Docker 部署。
- [ ] 改进界面样式。
- [ ] 添加搜索链接功能。

## 许可证
本项目采用 MIT 许可证，详情见 [LICENSE](LICENSE) 文件。

## 致谢
- 基于 Flask 构建。
- 申请 VTEXS 开源计划 提供托管支持。

## 测试记录
- 2025-04-26：测试链接格式验证，`example.com` 未保存，`https://github.com` 保存成功（附截图：[static/flask_page_20250426.png]）。