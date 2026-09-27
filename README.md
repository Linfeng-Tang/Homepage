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

每日历史只保存在 `assets/data/scholar-citations.xlsx`。`每日引用` 工作表每个日期一行，记录总引用、相较上次记录的变化、H 指数、i10 指数和实际获取时间；已从主页仓库恢复 2026-08-10 至 2026-09-26 的 9 条真实记录。`逐篇论文` 工作表每个日期、每篇论文一行，以稳定的 Scholar 论文 ID 区分，记录标题、引用数和相较该论文上次记录的变化；已从另一份现有快照恢复 2026-09-19 的 37 篇论文基线。同一天重复运行会更新当日记录。没有快照的日期保持空缺。

`assets/data/scholar.json` 是原有主页展示指标所需的小型缓存，由同一次请求顺带更新，不保存历史。

变化是相对上一次成功记录的差值；若某天未能获取主页数据，下一次变化可能跨越多天。Google Scholar 数据可能修订，因此差值也可能为负。若页面要求人机验证或结构不完整，程序保留已有记录，不进行高频重试。

本地手动运行：先安装 `openpyxl`，再运行 `python tools/update_scholar_stats.py`。GitHub 仓库的 Actions 页面也可以手动运行同名工作流。每天更新需要将本目录作为 GitHub 仓库发布，并启用 Actions；本地文件本身不会自动定时运行。

详细步骤见 [DEPLOY_TO_GITHUB_PAGES.md](./DEPLOY_TO_GITHUB_PAGES.md)。
