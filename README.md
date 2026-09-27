# Linfeng Homepage Site

这个文件夹已经整理成可直接部署的独立静态网站项目。

包含内容：

- `index.html`
- `publications.html`
- `news.html`
- `honors.html`
- `services.html`
- `contact.html`
- `styles.css`
- `.github/workflows/deploy-pages.yml`
- `.nojekyll`
- `assets/icons/`
- `assets/img/`

推荐发布方式：

1. 新建一个独立仓库，例如 `linfeng-homepage-site`
2. 把这个文件夹里的全部内容上传到仓库根目录
3. 在 GitHub 仓库 `Settings > Pages` 中把 `Source` 设为 `GitHub Actions`
4. 推送到 `main` 后，站点会通过工作流自动部署

当前目录中的素材路径都已经改成站内相对路径，不再依赖旧项目或外部本地文件夹。

## 每日 Google Scholar 引用记录

现有的 `.github/workflows/update-scholar-stats.yml` 每天北京时间约 10:00 运行一次，读取[公开 Google Scholar 作者主页](https://scholar.google.com/citations?user=PyRqpAsAAAAJ)的一页数据。GitHub Actions 可能延迟，实际执行时间以运行记录为准。无需另外搭建网站或服务器。

- `assets/data/scholar.json`：主页目前使用的总引用、H 指数和 i10 指数。
- `assets/data/scholar-latest.md`：最新一次成功读取的中文日报，含逐篇引用变化。
- `assets/data/scholar-daily.csv`：每天的总引用变化，可用 Excel 打开。
- `assets/data/scholar-history.json`：完整每日快照和逐篇数据。

首次运行建立基线，从第二次成功读取开始计算变化。变化是相对上一次成功记录的差值；若某天未能获取主页数据，下一次变化可能跨越多天。Google Scholar 数据可能修订，因此差值也可能为负。若页面要求人机验证或结构不完整，程序保留已有记录，不进行高频重试。

本地手动运行：`python tools/update_scholar_stats.py`。GitHub 仓库的 Actions 页面也可以手动运行同名工作流。每天更新需要将本目录作为 GitHub 仓库发布，并启用 Actions；本地文件本身不会自动定时运行。

详细步骤见 [DEPLOY_TO_GITHUB_PAGES.md](./DEPLOY_TO_GITHUB_PAGES.md)。
