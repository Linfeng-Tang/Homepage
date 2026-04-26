from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parents[1]

PAGES = [
    ("index.html", "about"),
    ("publications.html", "publications"),
    ("news.html", "news"),
    ("honors.html", "honors"),
    ("services.html", "services"),
    ("contact.html", "contact"),
]

NAV = {
    "zh": {
        "about": "关于",
        "publications": "论文",
        "news": "动态",
        "honors": "荣誉",
        "services": "服务",
        "contact": "联系",
    },
    "en": {
        "about": "About",
        "publications": "Publications",
        "news": "News",
        "honors": "Honors",
        "services": "Services",
        "contact": "Contact",
    },
}

PUBS = [
    {
        "id": "videofusion",
        "groups": "selected all",
        "venue": "CVPR",
        "image": "VideoFusion.jpg",
        "title": "VideoFusion: A Spatio-Temporal Collaborative Network for Multi-modal Video Fusion and Restoration",
        "authors": ["Linfeng Tang", "Yeda Wang", "Meiqi Gong", "Zizhuo Li", "Yuxin Deng", "Xunpeng Yi", "Chunyu Li", "Han Xu", "Hao Zhang", "Jiayi Ma"],
        "venue_text": "In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 2026",
        "citations": "10",
        "links": [("PDF", "https://arxiv.org/abs/2503.23359"), ("CODE", "https://github.com/Linfeng-Tang/VideoFusion")],
    },
    {
        "id": "dspfusion",
        "groups": "all",
        "venue": "ArXiv",
        "image": "DSPFusion.jpg",
        "title": "DSPFusion: Image Fusion via Degradation and Semantic Dual-Prior Guidance",
        "authors": ["Linfeng Tang", "Chunyu Li", "Guoqing Wang", "Yixuan Yuan", "Jiayi Ma"],
        "venue_text": "arXiv preprint arXiv:2503.23355, 2025",
        "citations": "2",
        "links": [("PDF", "https://arxiv.org/abs/2503.23355")],
    },
    {
        "id": "mask-difuser",
        "groups": "selected all",
        "venue": "IEEE TPAMI",
        "image": "Mask-DiFuser.jpg",
        "title": "Mask-DiFuser: A Masked Diffusion Model for Unified Unsupervised Image Fusion",
        "authors": ["Linfeng Tang", "Chunyu Li", "Jiayi Ma"],
        "venue_text": "IEEE Transactions on Pattern Analysis and Machine Intelligence (TPAMI), 2026",
        "citations": "24",
        "links": [("PDF", "https://ieeexplore.ieee.org/document/11162636"), ("CODE", "https://github.com/Linfeng-Tang/Mask-DiFuser")],
    },
    {
        "id": "controlfusion",
        "groups": "selected all",
        "venue": "NeurIPS",
        "image": "ControlFusion.jpg",
        "title": "ControlFusion: A Controllable Image Fusion Framework with Language-Vision Degradation Prompts",
        "authors": ["Linfeng Tang", "Yeda Wang", "Zhanchuan Cai", "Junjun Jiang", "Jiayi Ma"],
        "venue_text": "In Advances in Neural Information Processing Systems (NeurIPS), 2025",
        "note": {"zh": "口头报告", "en": "Oral Presentation"},
        "citations": "16",
        "links": [("PDF", "https://arxiv.org/pdf/2503.23356"), ("CODE", "https://github.com/Linfeng-Tang/ControlFusion")],
    },
    {
        "id": "c2rf",
        "groups": "selected all",
        "venue": "IJCV",
        "image": "C2RF.jpg",
        "title": "C2RF: Bridging Multi-modal Image Registration and Fusion via Commonality Mining and Contrastive Learning",
        "authors": ["Linfeng Tang", "Qinglong Yan", "Xinyu Xiang", "Leyuan Fang", "Jiayi Ma"],
        "venue_text": "International Journal of Computer Vision (IJCV), 2025",
        "citations": "37",
        "home_citations": "39",
        "links": [("PDF", "https://link.springer.com/article/10.1007/s11263-025-02427-1"), ("CODE", "https://github.com/Linfeng-Tang/C2RF")],
    },
    {
        "id": "drmf",
        "groups": "all",
        "venue": "ACM MM",
        "image": "DRMF.jpg",
        "title": "DRMF: Degradation-Robust Multi-Modal Image Fusion via Composable Diffusion Prior",
        "authors": ["Linfeng Tang", "Yuxin Deng", "Xunpeng Yi", "Qinglong Yan", "Yixuan Yuan", "Jiayi Ma"],
        "venue_text": "Proceedings of the ACM International Conference on Multimedia (ACM MM), 2024",
        "citations": "65",
        "links": [("PDF", "https://dl.acm.org/doi/10.1145/3664647.3681064"), ("CODE", "https://github.com/Linfeng-Tang/DRMF")],
    },
    {
        "id": "seafusion",
        "groups": "selected highly-cited all",
        "venue": "Inf. Fusion",
        "image": "SeAFusion.jpg",
        "title": "Image Fusion in the Loop of High-level Vision Tasks: A Semantic-aware Real-time Infrared and Visible Image Fusion Network",
        "authors": ["Linfeng Tang", "Jiteng Yuan", "Jiayi Ma"],
        "venue_text": "Information Fusion, 2022",
        "citations": "1,064",
        "home_citations": "1,071",
        "tags": ["hot", "cited", "award"],
        "links": [("PDF", "https://www.sciencedirect.com/science/article/pii/S1566253521002542"), ("CODE", "https://github.com/Linfeng-Tang/SeAFusion")],
    },
    {
        "id": "swinfusion",
        "groups": "selected highly-cited all",
        "venue": "IEEE/CAA JAS",
        "image": "SwinFusion.jpg",
        "title": "SwinFusion: Cross-domain Long-range Learning for General Image Fusion via Swin Transformer",
        "authors": ["Jiayi Ma", "Linfeng Tang", "Fan Fan", "Jun Huang", "Xiaoguang Mei", "Yong Ma"],
        "venue_text": "IEEE/CAA Journal of Automatica Sinica, 2022",
        "citations": "1,404",
        "home_citations": "1,421",
        "tags": ["hot", "cited", "award"],
        "links": [("PDF", "https://ieeexplore.ieee.org/document/9812535"), ("CODE", "https://github.com/Linfeng-Tang/SwinFusion")],
    },
    {
        "id": "piafusion",
        "groups": "selected highly-cited all",
        "venue": "Inf. Fusion",
        "image": "PIAFusion.jpg",
        "title": "PIAFusion: A Progressive Infrared and Visible Image Fusion Network Based on Illumination Aware",
        "authors": ["Linfeng Tang", "Jiteng Yuan", "Hao Zhang", "Xingyu Jiang", "Jiayi Ma"],
        "venue_text": "Information Fusion, 2022",
        "citations": "1,100",
        "home_citations": "1,113",
        "tags": ["hot", "cited"],
        "links": [("PDF", "https://www.sciencedirect.com/science/article/pii/S156625352200032X"), ("CODE", "https://github.com/Linfeng-Tang/PIAFusion")],
    },
    {
        "id": "superfusion",
        "groups": "highly-cited all",
        "venue": "IEEE/CAA JAS",
        "image": "SuperFusion.jpg",
        "title": "SuperFusion: A Versatile Image Registration and Fusion Network with Semantic Awareness",
        "authors": ["Linfeng Tang", "Yuxin Deng", "Yong Ma", "Jun Huang", "Jiayi Ma"],
        "venue_text": "IEEE/CAA Journal of Automatica Sinica, 2022",
        "citations": "451",
        "tags": ["hot", "cited"],
        "links": [("PDF", "https://ieeexplore.ieee.org/document/9970457"), ("CODE", "https://github.com/Linfeng-Tang/SuperFusion")],
    },
    {
        "id": "divfusion",
        "groups": "highly-cited all",
        "venue": "Inf. Fusion",
        "image": "DIVFusion.jpg",
        "title": "DIVFusion: Darkness-free Infrared and Visible Image Fusion",
        "authors": ["Linfeng Tang", "Xinyu Xiang", "Hao Zhang", "Meiqi Gong", "Jiayi Ma"],
        "venue_text": "Information Fusion, 2023",
        "citations": "485",
        "tags": ["hot", "cited"],
        "links": [("PDF", "https://www.sciencedirect.com/science/article/pii/S156625352200210X"), ("CODE", "https://github.com/Linfeng-Tang/DIVFusion")],
    },
    {
        "id": "psfusion",
        "groups": "highly-cited all",
        "venue": "Inf. Fusion",
        "image": "PSFusion.jpg",
        "title": "Rethinking the Necessity of Image Fusion in High-level Vision Tasks: A Practical Infrared and Visible Image Fusion Network Based on Progressive Semantic Injection and Scene Fidelity",
        "authors": ["Linfeng Tang", "Hao Zhang", "Han Xu", "Jiayi Ma"],
        "venue_text": "Information Fusion, 2023",
        "citations": "351",
        "tags": ["hot", "cited"],
        "links": [("PDF", "https://www.sciencedirect.com/science/article/pii/S1566253523001860"), ("CODE", "https://github.com/Linfeng-Tang/PSFusion")],
    },
    {
        "id": "stdfusionnet",
        "groups": "highly-cited all",
        "venue": "IEEE TIM",
        "image": "STDFusionNet.jpg",
        "title": "STDFusionNet: An Infrared and Visible Image Fusion Network Based on Salient Target Detection",
        "authors": ["Jiayi Ma", "Linfeng Tang", "Meilong Xu", "Hao Zhang", "Guobao Xiao"],
        "venue_text": "IEEE Transactions on Instrumentation and Measurement, 2021",
        "citations": "633",
        "tags": ["cited"],
        "links": [("PDF", "https://ieeexplore.ieee.org/document/9416507"), ("CODE", "https://github.com/Linfeng-Tang/STDFusionNet")],
    },
    {
        "id": "survey",
        "groups": "selected all",
        "venue": "JIG",
        "image": "Survey.jpg",
        "title": "Deep Learning-based Image Fusion: A Survey",
        "authors": ["Linfeng Tang", "Hao Zhang", "Han Xu", "Jiayi Ma"],
        "venue_text": "Journal of Image and Graphics, 2024",
        "citations": "98",
        "home_citations": "97",
        "tags": ["note", "award2", "award"],
        "links": [("PDF", "https://txtx.publish.founderss.cn/zh/article/doi/10.11834/jig.220422"), ("CODE", "https://github.com/Linfeng-Tang/Image-Fusion")],
    },
    {
        "id": "drlie",
        "groups": "all",
        "venue": "IEEE TNNLS",
        "image": "DRLIE.jpg",
        "title": "DRLIE: Flexible Low-light Image Enhancement via Disentangled Representations",
        "authors": ["Linfeng Tang", "Jiayi Ma", "Hao Zhang", "Xiaojie Guo"],
        "venue_text": "IEEE Transactions on Neural Networks and Learning Systems, 2024",
        "citations": "33",
        "links": [("PDF", "https://ieeexplore.ieee.org/document/9833451"), ("CODE", "https://github.com/Linfeng-Tang/DRLIE")],
    },
    {
        "id": "camf",
        "groups": "all",
        "venue": "IEEE TMM",
        "image": "CAMF.jpg",
        "title": "CAMF: An Interpretable Infrared and Visible Image Fusion Network Based on Class Activation Mapping",
        "authors": ["Linfeng Tang", "Ziang Chen", "Jun Huang", "Jiayi Ma"],
        "venue_text": "IEEE Transactions on Multimedia, 2024",
        "citations": "69",
        "links": [("PDF", "https://ieeexplore.ieee.org/document/10288391"), ("CODE", "https://github.com/Linfeng-Tang/CAMF")],
    },
    {
        "id": "pstlfusion",
        "groups": "all",
        "venue": "PR",
        "image": "PSTLFusion.jpg",
        "title": "Infrared and Visible Image Fusion via Parallel Scene and Texture Learning",
        "authors": ["Meilong Xu", "Linfeng Tang", "Hao Zhang", "Jiayi Ma"],
        "venue_text": "Pattern Recognition, 2022",
        "citations": "67",
        "links": [("PDF", "https://www.sciencedirect.com/science/article/pii/S0031320322004101"), ("CODE", "https://github.com/Melon-Xu/PSTLFusion")],
    },
]

NEWS = [
    ("2026-02-20", "VideoFusion 被 CVPR 2026 接收", "VideoFusion accepted by CVPR 2026", [("paper", "论文", "Paper", "https://arxiv.org/abs/2503.23359"), ("code", "代码", "Code", "https://github.com/Linfeng-Tang/VideoFusion")]),
    ("2025-12-26", "图像融合综述获《中国图象图形学报》2020-2024 优秀论文", "The image fusion survey received the Journal of Image and Graphics 2020-2024 Excellent Paper Award", [("paper", "论文", "Paper", "https://www.cjig.cn/thesisDetails#10.11834/jig.220422&lang=zh")]),
    ("2025-09-18", "ControlFusion 被 NeurIPS 2025 接收为口头报告", "ControlFusion accepted by NeurIPS 2025 as an Oral presentation", [("paper", "论文", "Paper", "https://arxiv.org/pdf/2503.23356"), ("code", "代码", "Code", "https://github.com/Linfeng-Tang/ControlFusion")]),
    ("2025-09-10", "Mask-DiFuser 被 IEEE TPAMI 接收", "Mask-DiFuser accepted by IEEE TPAMI", [("paper", "论文", "Paper", "https://ieeexplore.ieee.org/document/11162636"), ("code", "代码", "Code", "https://github.com/Linfeng-Tang/Mask-DiFuser")]),
    ("2025-03-15", "C2RF 被 IJCV 接收", "C2RF accepted by IJCV", [("paper", "论文", "Paper", "https://link.springer.com/article/10.1007/s11263-025-02427-1"), ("code", "代码", "Code", "https://github.com/Linfeng-Tang/C2RF")]),
    ("2025-02-11", "发布红外-可见光视频融合数据集 M3SVD", "Released the M3SVD dataset for infrared-visible video fusion", [("data", "数据集", "Dataset", "https://github.com/Linfeng-Tang/M3SVD")]),
    ("2024-12-26", "图像融合综述获《中国图象图形学报》2024 年度优秀论文", "The image fusion survey received the Journal of Image and Graphics 2024 Excellent Paper Award", [("note", "报道", "News", "https://mp.weixin.qq.com/s?__biz=MzU1NzM4MjgzOA==&mid=2247536019&idx=1&sn=086193c8064ae58bc1f05de26faaee61")]),
    ("2024-11-28", "SeAFusion 获 Information Fusion 2024 最佳论文奖", "SeAFusion won the Information Fusion Best Paper Award 2024", [("paper", "论文", "Paper", "https://www.sciencedirect.com/science/article/pii/S1566253521002542"), ("code", "代码", "Code", "https://github.com/Linfeng-Tang/SeAFusion")]),
    ("2024-09-01", "图像融合综述入选空天信息科技期刊高影响力论文", "The image fusion survey was selected as a high-impact paper in aerospace information technology journals", [("paper", "论文", "Paper", "https://txtx.publish.founderss.cn/zh/article/doi/10.11834/jig.220422/")]),
    ("2024-07-16", "DRMF 被 ACM MM 2024 接收", "DRMF accepted by ACM MM 2024", [("paper", "论文", "Paper", "https://dl.acm.org/doi/10.1145/3664647.3681064"), ("code", "代码", "Code", "https://github.com/Linfeng-Tang/DRMF")]),
    ("2023-11-01", "SwinFusion 获 IEEE/CAA JAS 2023 钱学森论文奖", "SwinFusion won the Hsue-shen Tsien Paper Award 2023", [("paper", "论文", "Paper", "https://ieeexplore.ieee.org/document/9812535"), ("code", "代码", "Code", "https://github.com/Linfeng-Tang/SwinFusion")]),
]

HONORS = {
    "zh": [
        ("国际与国家级奖励", [
            "World's Top 2% Scientists, Stanford University/Elsevier, 2025",
            "中国图象图形学报 2020-2024 优秀论文，2025",
            "Information Fusion Best Paper Award, 2024",
            "IEEE/CAA JAS 钱学森论文奖，2023",
            "中国图象图形学报 2024 年度优秀论文",
            "空天信息科技期刊高影响力论文，2024",
            "博士研究生国家奖学金，2024",
            "本科生国家奖学金，2018",
            "Meritorious Winner, MCM/ICM, 2019",
        ]),
        ("学术认可", [
            "Outstanding Reviewer, Image and Vision Computing, 2025",
            "Outstanding Reviewer, Information Fusion, 2024",
            "优秀报告成果，中国图象图形学报学术论坛，2023",
        ]),
        ("校级荣誉与奖学金", [
            "武汉大学优秀毕业生，2025",
            "武汉大学“电子信息精英榜”之学术创新榜样，2025",
            "武汉大学知行学术论坛一等奖，2024",
            "武汉大学优秀研究生，2021 / 2023 / 2024",
            "优秀共产党员，2022 / 2023",
            "湖南省优秀毕业生，2020",
            "中南大学优秀毕业生，2020",
            "武汉大学甲等奖学金，2024",
            "雷军奖学金，2022",
            "华为奖学金，2021",
            "新生一等奖学金，2020",
        ]),
    ],
    "en": [
        ("International and National Awards", [
            "World's Top 2% Scientists, Stanford University/Elsevier, 2025",
            "Journal of Image and Graphics 2020-2024 Excellent Paper Award, 2025",
            "Best Paper Award, Information Fusion, 2024",
            "Hsue-shen Tsien Paper Award, IEEE/CAA JAS, 2023",
            "Journal of Image and Graphics 2024 Excellent Paper Award",
            "High-Impact Paper in Aerospace Information Technology Journals, 2024",
            "National Scholarship for Doctoral Students, 2024",
            "National Scholarship for Undergraduates, 2018",
            "Meritorious Winner, MCM/ICM, 2019",
        ]),
        ("Academic Recognition", [
            "Outstanding Reviewer, Image and Vision Computing, 2025",
            "Outstanding Reviewer, Information Fusion, 2024",
            "Excellent Presentation, Journal of Image and Graphics Academic Forum, 2023",
        ]),
        ("University Honors and Scholarships", [
            "Outstanding Graduate, Wuhan University, 2025",
            "Academic Innovation Role Model, Electronic Information Elite List, Wuhan University, 2025",
            "First Prize, Zhixing Academic Forum, Wuhan University, 2024",
            "Outstanding Graduate Student, Wuhan University, 2021 / 2023 / 2024",
            "Outstanding Communist Party Member, 2022 / 2023",
            "Outstanding Graduate, Hunan Province, 2020",
            "Outstanding Graduate, Central South University, 2020",
            "First-Class Scholarship, Wuhan University, 2024",
            "Lei Jun Scholarship, 2022",
            "Huawei Scholarship, 2021",
            "First-Class Freshman Scholarship, 2020",
        ]),
    ],
}


def page_path(filename, lang):
    return f"./{filename}" if lang == "zh" else f"./{filename}"


def asset(path, lang):
    return f"./{path}" if lang == "zh" else f"../{path}"


def other_lang_href(filename, lang):
    return f"./en/{filename}" if lang == "zh" else f"../{filename}"


def same_lang_href(filename, lang):
    return f"./{filename}"


def head(title, description, filename, lang):
    css = asset("styles.css", lang)
    en_href = f"./en/{filename}" if lang == "zh" else f"./{filename}"
    zh_href = f"./{filename}" if lang == "zh" else f"../{filename}"
    html_lang = "zh-CN" if lang == "zh" else "en"
    return f"""<!doctype html>
<html lang="{html_lang}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{escape(title)}</title>
  <meta name="description" content="{escape(description)}">
  <link rel="alternate" hreflang="zh-CN" href="{zh_href}">
  <link rel="alternate" hreflang="en" href="{en_href}">
  <link rel="stylesheet" href="{css}">
</head>"""


def header(active, filename, lang):
    brand = "唐霖峰 · Linfeng Tang" if lang == "zh" else "Linfeng Tang"
    mark = "唐" if lang == "zh" else "LT"
    items = []
    for nav_file, key in PAGES:
        cls = ' class="current"' if key == active else ""
        items.append(f'        <a{cls} href="{same_lang_href(nav_file, lang)}">{NAV[lang][key]}</a>')
    if lang == "zh":
        lang_switch = f'<a class="lang-link" href="{other_lang_href(filename, lang)}">EN</a>'
    else:
        lang_switch = f'<a class="lang-link" href="{other_lang_href(filename, lang)}">Chinese</a>'
    return f"""<body>
  <header class="topbar">
    <div class="wrap topbar-inner">
      <a class="brand" href="{same_lang_href('index.html', lang)}">
        <span class="brand-mark">{mark}</span>
        <span>{brand}</span>
      </a>
      <nav class="nav">
{chr(10).join(items)}
        {lang_switch}
      </nav>
    </div>
  </header>"""


def footer(text):
    return f"""    <div class="footer">{escape(text)}</div>
  </main>
</body>
</html>
"""


def authors_html(authors):
    parts = []
    for name in authors:
        if name == "Linfeng Tang":
            parts.append('<span class="me">Linfeng Tang</span>')
        else:
            parts.append(escape(name))
    if len(parts) == 1:
        return parts[0]
    if len(parts) == 2:
        return f"{parts[0]} and {parts[1]}"
    return ", ".join(parts[:-1]) + f", and {parts[-1]}"


CUSTOM_TAG_LABELS = {
    "seafusion": {
        "award": {
            "zh": "Information Fusion 2024 年度唯一最佳论文奖",
            "en": "Information Fusion 2024 Sole Best Paper Award",
        },
    },
    "swinfusion": {
        "award": {
            "zh": "IEEE/CAA JAS 2023 钱学森论文奖",
            "en": "IEEE/CAA JAS 2023 Hsue-shen Tsien Paper Award",
        },
    },
    "survey": {
        "note": {
            "zh": "空天信息科技期刊高影响力论文",
            "en": "High-Impact Paper in Aerospace Information Technology Journals",
        },
        "award2": {
            "zh": "中国图象图形学报 2020-2024 优秀论文",
            "en": "Journal of Image and Graphics 2020-2024 Excellent Paper",
        },
        "award": {
            "zh": "中国图象图形学报 2024 年度优秀论文",
            "en": "Journal of Image and Graphics 2024 Excellent Paper",
        },
    },
}


def tag_label(tag, lang, pub=None):
    if pub and pub["id"] in CUSTOM_TAG_LABELS and tag in CUSTOM_TAG_LABELS[pub["id"]]:
        return CUSTOM_TAG_LABELS[pub["id"]][tag][lang]
    labels = {
        "hot": {"zh": "ESI 热点论文", "en": "ESI Hot Paper"},
        "cited": {"zh": "ESI 高被引论文", "en": "ESI Highly Cited"},
        "award": {"zh": "最佳论文奖", "en": "Best Paper Award"},
        "award2": {"zh": "2020-2024 优秀论文", "en": "2020-2024 Excellent Paper"},
        "note": {"zh": "高影响力论文", "en": "High-Impact Paper"},
    }
    return labels[tag][lang]


def pub_item(pub, lang, compact=False):
    title = escape(pub["title"])
    href = f"{same_lang_href('publications.html', lang)}#{pub['id']}" if compact else pub["links"][0][1]
    thumb = f'<a class="pub-thumb" href="{href}"><img src="{asset("assets/img/publication_preview/" + pub["image"], lang)}" alt="{escape(pub["id"])}"></a>' if compact else f'<div class="pub-thumb"><img src="{asset("assets/img/publication_preview/" + pub["image"], lang)}" alt="{escape(pub["id"])}"></div>'
    note = ""
    if "note" in pub:
        note = f'            <div class="pub-note">{escape(pub["note"][lang])}</div>\n'
    citation_count = pub.get("home_citations", pub["citations"]) if compact else pub["citations"]
    citation_label = f"引用 {citation_count}" if lang == "zh" else f"Citations {citation_count}"
    tag_html = [f'<span class="badge-citation">{escape(citation_label)}</span>']
    for tag in pub.get("tags", []):
        tag_html.append(f'<span class="badge-{tag if tag != "award2" else "award"}">{escape(tag_label(tag, lang, pub))}</span>')
    links = []
    for label, url in pub["links"]:
        text = {"PDF": "论文", "CODE": "代码"}.get(label, label) if lang == "zh" else {"CODE": "Code"}.get(label, label)
        links.append(f'<a class="paper-btn" href="{url}" target="_blank" rel="noreferrer">{escape(text)}</a>')
    link = href if compact else pub["links"][0][1]
    id_attr = "" if compact else f' id="{pub["id"]}" data-groups="{pub["groups"]}"'
    return f"""        <article class="pub-item"{id_attr}>
          <div class="pub-media">
            <div class="venue-badge">{escape(pub["venue"])}</div>
            {thumb}
          </div>
          <div>
            <h3><a href="{link}"{' target="_blank" rel="noreferrer"' if not compact else ''}>{title}</a></h3>
            <div class="pub-authors">{authors_html(pub["authors"])}</div>
            <div class="pub-venue">{escape(pub["venue_text"])}</div>
{note}            <div class="pub-highlights">{"".join(tag_html)}</div>
            <div class="pub-actions">{"".join(links)}</div>
          </div>
        </article>"""


def news_item(item, lang):
    date, zh_text, en_text, links = item
    title = zh_text if lang == "zh" else en_text
    actions = []
    for kind, zh_label, en_label, url in links:
        label = zh_label if lang == "zh" else en_label
        actions.append(f'<a class="mini-btn {kind}" href="{url}" target="_blank" rel="noreferrer">{escape(label)}</a>')
    return f"""          <div class="timeline-item">
            <span>{date}</span>
            <strong>{escape(title)}</strong>
            <div class="mini-actions">{"".join(actions)}</div>
          </div>"""


def page_home(lang):
    if lang == "zh":
        title = "唐霖峰 | 个人学术主页"
        desc = "唐霖峰个人学术主页。"
        eyebrow = "个人学术主页"
        h1 = "唐霖峰"
        en_name = '<div class="en-name">Linfeng Tang</div>'
        subtitle = "武汉大学弘毅博士后 · 合作导师：马佳义教授"
        summary = "于 2025 年 12 月在武汉大学·电子信息学院获得博士学位，于 2020 年 6 月在中南大学·计算机学院获得学士学位。研究方向为多源图像融合感知，主要包括多模图像融合、视频融合、图像复原、图像匹配，以及语义感知驱动的图像融合。近五年以第一作者（导师第一或共同第一）发表学术论文 16 篇，包含中科院一区、IEEE Trans、CCF A 等高水平论文 15 篇，其中 ESI 热点论文（前 0.1%）6 篇，ESI 高被引论文（前 1%）7 篇；谷歌学术引用 6900 余次，H 指数 21，3 篇引用超过 1000 次，单篇引用最高 1416 次。"
        aff = ["机器人学院", "武汉大学", "弘毅博士后", "合作导师：马佳义教授", "武汉，中国 430072"]
        chips = ["多源融合感知", "图像融合", "图像复原", "语义感知"]
        actions = [("谷歌学术", "https://scholar.google.com/citations?user=PyRqpAsAAAAJ&hl=zh-CN", "btn"), ("GitHub", "https://github.com/Linfeng-Tang", "btn-blue"), ("论文列表", "./publications.html", "btn-gold")]
        highlights_title = "亮点"
        highlights = ["World's Top 2% Scientists, 2025", "NeurIPS 2025 口头报告", "Information Fusion 2024 年度唯一最佳论文奖", "中国图象图形学报 2024 年度优秀论文，2024", "中国图象图形学报 2020-2024 优秀论文，2025", "IEEE/CAA JAS 钱学森论文奖，2023", "6 篇 ESI 热点论文", "7 篇 ESI 高被引论文"]
        research_title = "研究方向"
        focus = [
            ("多模图像融合", "面向红外-可见光图像融合、视频融合、可控融合、配准-融合联合建模，以及通用图像融合。"),
            ("多模图像复原", "利用多模图像互补信息，研究退化感知复原，以及统一融合-复原框架。"),
            ("高低层视觉协同优化", "探索视觉-语义协同优化策略，以及服务于高层视觉任务的语义感知图像融合模型。"),
        ]
        rep_title = "代表性论文"
        view_all = "查看全部"
        latest = "最新动态"
        footer_text = "中文个人学术主页。"
    else:
        title = "Linfeng Tang | Academic Homepage"
        desc = "Academic homepage of Linfeng Tang."
        eyebrow = "Academic Homepage"
        h1 = "Linfeng Tang"
        en_name = ""
        subtitle = "Hongyi Postdoc at Wuhan University - Advisor: Prof. Jiayi Ma"
        summary = "I received my Ph.D. degree from the School of Electronic Information, Wuhan University in December 2025 and my B.S. degree from the School of Computer Science and Engineering, Central South University in June 2020. My research focuses on multi-source image fusion perception, including multi-modal image fusion, video fusion, image restoration, image matching, and semantics-aware image fusion. In the past five years, I have published 16 papers as first author, advisor-first-author, or co-first author, including 15 high-level papers in CAS Q1 journals, IEEE Transactions, and CCF-A venues. These papers include 6 ESI Hot Papers (top 0.1%) and 7 ESI Highly Cited Papers (top 1%). My Google Scholar citations exceed 6,900, with an h-index of 21; 3 papers have over 1,000 citations, and the highest-cited paper has 1,416 citations."
        aff = ["School of Robotics", "Wuhan University", "Hongyi Postdoc", "Advisor: Prof. Jiayi Ma", "Wuhan, 430072, China"]
        chips = ["Multi-source Fusion Perception", "Image Fusion", "Image Restoration", "Semantic Perception"]
        actions = [("Google Scholar", "https://scholar.google.com/citations?user=PyRqpAsAAAAJ&hl=zh-CN", "btn"), ("GitHub", "https://github.com/Linfeng-Tang", "btn-blue"), ("Publications", "./publications.html", "btn-gold")]
        highlights_title = "Highlights"
        highlights = ["World's Top 2% Scientists, 2025", "NeurIPS 2025 Oral", "Information Fusion 2024 Sole Best Paper Award", "Journal of Image and Graphics 2024 Excellent Paper, 2024", "Journal of Image and Graphics 2020-2024 Excellent Paper, 2025", "Hsue-shen Tsien Paper Award, 2023", "6 ESI Hot Papers", "7 ESI Highly Cited Papers"]
        research_title = "Research Focus"
        focus = [
            ("Multi-modal Image Fusion", "Infrared-visible image fusion, video fusion, controllable fusion, registration-fusion joint modeling, and general image fusion."),
            ("Multi-modal Image Restoration", "Image restoration with complementary multi-modal information, focusing on degradation-aware restoration and unified fusion-restoration frameworks."),
            ("High-Low Level Vision Co-optimization", "Visual-semantic co-optimization strategies and semantics-aware image fusion models designed for high-level vision tasks."),
        ]
        rep_title = "Representative Publications"
        view_all = "View All"
        latest = "Latest News"
        footer_text = "English academic homepage."
    aff_html = f'<a href="https://robotics.whu.edu.cn/" target="_blank" rel="noreferrer">{escape(aff[0])}</a><a href="https://www.whu.edu.cn/" target="_blank" rel="noreferrer">{escape(aff[1])}</a>' + "".join(f"<span>{escape(x)}</span>" for x in aff[2:])
    chip_html = "".join(f'<span class="chip">{escape(x)}</span>' for x in chips)
    action_parts = []
    for label, url, cls in actions:
        target = ' target="_blank" rel="noreferrer"' if url.startswith("http") else ""
        action_parts.append(f'<a class="{cls}" href="{url}"{target}>{escape(label)}</a>')
    action_html = "".join(action_parts)
    highlight_html = "".join(f"<span>{escape(x)}</span>" for x in highlights)
    focus_html = "\n".join(f'        <article class="card">\n          <h3>{escape(name)}</h3>\n          <p>{escape(text)}</p>\n        </article>' for name, text in focus)
    selected = [PUBS[i] for i in [0, 2, 3, 4, 7, 6, 8, 13]]
    pubs_html = "\n\n".join(pub_item(pub, lang, compact=True) for pub in selected)
    news_html = "\n".join(news_item(item, lang).replace('<div class="mini-actions">', '<p>').replace('</div>', '</p>', 1) for item in NEWS[:3])
    return f"""{head(title, desc, 'index.html', lang)}
{header('about', 'index.html', lang)}

  <main class="wrap">
    <section class="page-hero hero-home">
      <article class="hero-main hero-card">
        <div class="portrait-column">
          <img class="portrait" src="{asset('assets/img/prof_pic_color.png', lang)}" alt="{escape('唐霖峰照片' if lang == 'zh' else 'Portrait of Linfeng Tang')}">
          <div class="portrait-affiliation">{aff_html}</div>
        </div>
        <div>
          <h1>{escape(h1)}</h1>
          {en_name}
          <div class="subtitle">{escape(subtitle)}</div>
          <p class="summary">{escape(summary)}</p>
          <div class="actions">{action_html}</div>
        </div>
      </article>

      <div class="side-stack">
        <aside class="info-card keyword-card">
          <span class="eyebrow">{escape(research_title)}</span>
          <div class="chips">{chip_html}</div>
        </aside>
        <aside class="info-card">
          <span class="eyebrow">{escape(highlights_title)}</span>
          <div class="compact-badges">{highlight_html}</div>
        </aside>
      </div>
    </section>

    <section class="section">
      <div class="section-head"><h2>{escape(research_title)}</h2></div>
      <div class="focus-grid">
{focus_html}
      </div>
    </section>

    <section class="section">
      <div class="section-head">
        <h2>{escape(rep_title)}</h2>
        <a class="section-link" href="./publications.html">{escape(view_all)}</a>
      </div>
      <div class="publication-list">
{pubs_html}
      </div>
    </section>

    <section class="section">
      <div class="section-head">
        <h2>{escape(latest)}</h2>
        <a class="section-link" href="./news.html">{escape(view_all)}</a>
      </div>
      <div class="timeline-card">
        <div class="timeline-list">
{news_html}
        </div>
      </div>
    </section>

{footer(footer_text)}"""


def page_publications(lang):
    title = "唐霖峰 | 论文" if lang == "zh" else "Linfeng Tang | Publications"
    desc = "唐霖峰完整论文列表。" if lang == "zh" else "Complete publication list of Linfeng Tang."
    h1 = "论文" if lang == "zh" else "Publications"
    p = "按时间倒序整理的论文列表。" if lang == "zh" else "Publications in reverse chronological order."
    labels = {"selected": "精选" if lang == "zh" else "Selected", "highly": "高被引" if lang == "zh" else "Highly Cited", "all": "全部" if lang == "zh" else "All"}
    pubs_html = "\n\n".join(pub_item(pub, lang) for pub in PUBS)
    footer_text = "完整论文列表。" if lang == "zh" else "Independent publications page."
    return f"""{head(title, desc, 'publications.html', lang)}
{header('publications', 'publications.html', lang)}

  <main class="wrap">
    <section class="page-hero">
      <div class="hero-card">
        <h1>{h1}</h1>
        <p>{p}</p>
      </div>
    </section>

    <section class="section">
      <div class="filter-bar" aria-label="Publication filters">
        <button class="filter-btn active" type="button" data-filter="selected">{labels['selected']}</button>
        <button class="filter-btn" type="button" data-filter="highly-cited">{labels['highly']}</button>
        <button class="filter-btn" type="button" data-filter="all">{labels['all']}</button>
      </div>
      <div class="publication-list">
{pubs_html}
      </div>
    </section>

    <div class="footer">{escape(footer_text)}</div>
  </main>
  <script>
    const filterButtons = document.querySelectorAll(".filter-btn");
    const publicationItems = document.querySelectorAll(".pub-item");

    filterButtons.forEach((button) => {{
      button.addEventListener("click", () => {{
        const filter = button.dataset.filter;
        filterButtons.forEach((item) => item.classList.remove("active"));
        button.classList.add("active");
        publicationItems.forEach((item) => {{
          const groups = (item.dataset.groups || "").split(" ");
          item.classList.toggle("hidden", !groups.includes(filter));
        }});
      }});
    }});
  </script>
</body>
</html>
"""


def page_news(lang):
    title = "唐霖峰 | 动态" if lang == "zh" else "Linfeng Tang | News"
    desc = "唐霖峰近期动态。" if lang == "zh" else "Recent news of Linfeng Tang."
    h1 = "动态" if lang == "zh" else "News"
    p = "根据当前主页记录整理的近期动态。" if lang == "zh" else "Selected updates based on the current homepage records."
    items = "\n".join(news_item(item, lang) for item in NEWS)
    footer_text = "近期动态。" if lang == "zh" else "News page."
    return f"""{head(title, desc, 'news.html', lang)}
{header('news', 'news.html', lang)}

  <main class="wrap">
    <section class="page-hero">
      <div class="hero-card">
        <h1>{h1}</h1>
        <p>{p}</p>
      </div>
    </section>

    <section class="section">
      <div class="timeline-card">
        <div class="timeline-list">
{items}
        </div>
      </div>
    </section>

{footer(footer_text)}"""


def page_honors(lang):
    title = "唐霖峰 | 荣誉" if lang == "zh" else "Linfeng Tang | Honors"
    desc = "唐霖峰的荣誉、奖励与奖学金。" if lang == "zh" else "Honors, awards, and scholarships of Linfeng Tang."
    h1 = "荣誉" if lang == "zh" else "Honors"
    p = "荣誉、奖励与奖学金列表。" if lang == "zh" else "A list of honors, awards, and scholarships."
    cards = []
    for heading, items in HONORS[lang]:
        lis = "\n".join(f"            <li>{escape(item)}</li>" for item in items)
        cards.append(f"""        <article class="list-card">
          <h3>{escape(heading)}</h3>
          <ul class="plain-list">
{lis}
          </ul>
        </article>""")
    footer_text = "荣誉与奖励。" if lang == "zh" else "Honors page."
    return f"""{head(title, desc, 'honors.html', lang)}
{header('honors', 'honors.html', lang)}

  <main class="wrap">
    <section class="page-hero">
      <div class="hero-card">
        <h1>{h1}</h1>
        <p>{p}</p>
      </div>
    </section>

    <section class="section">
      <div class="honor-grid">
{chr(10).join(cards)}
      </div>
    </section>

{footer(footer_text)}"""


def page_services(lang):
    if lang == "zh":
        title = "唐霖峰 | 学术服务"
        desc = "唐霖峰的学术服务与审稿工作。"
        eyebrow = "学术服务"
        h1 = "学术服务"
        p = "审稿服务与学术共同体贡献。"
        badges = ["期刊审稿", "会议审稿", "计算机视觉", "图像融合"]
        overview = "概览"
        h2 = "审稿活动"
        j_mark = "期刊"
        j_title = "期刊审稿人"
        j_note = "服务于计算机视觉、多媒体、机器人、遥感、智能交通和交叉人工智能系统等方向的期刊。"
        c_mark = "会议"
        c_title = "会议审稿人"
        c_note = "服务于计算机视觉、机器学习、多媒体与人工智能相关顶级会议。"
        footer_text = "学术服务页面。"
    else:
        title = "Linfeng Tang | Services"
        desc = "Academic services and reviewing activities of Linfeng Tang."
        eyebrow = "Academic Services"
        h1 = "Academic Services"
        p = "Reviewer services and academic community contributions."
        badges = ["Journal Reviewing", "Conference Reviewing", "Computer Vision", "Image Fusion"]
        overview = "Overview"
        h2 = "Review Activities"
        j_mark = "Journals"
        j_title = "Journal Reviewer"
        j_note = "Selected journals in computer vision, multimedia, robotics, remote sensing, intelligent transportation, and interdisciplinary AI systems."
        c_mark = "Conferences"
        c_title = "Conference Reviewer"
        c_note = "Top-tier conferences related to computer vision, machine learning, multimedia, and AI."
        footer_text = "Services page."
    journals = [["IEEE TPAMI", "IJCV", "IEEE TIP", "IEEE TNNLS", "IEEE TMM", "IEEE TCSVT", "IEEE TII"], ["IEEE TGRS", "IEEE TITS", "IEEE TSMC", "IEEE TASE", "IEEE IoTJ", "IEEE JSAC", "IEEE/CAA JAS"], ["Information Fusion", "Pattern Recognition", "Neural Networks", "Energy", "Image and Vision Computing"]]
    journal_cols = "\n".join('<ul class="plain-list service-list">\n' + "\n".join(f"              <li>{j}</li>" for j in col) + "\n            </ul>" for col in journals)
    confs = "".join(f"<span>{c}</span>" for c in ["CVPR", "NeurIPS", "ECCV", "AAAI", "IJCAI", "ACM MM"])
    badge_html = "".join(f"<span>{escape(b)}</span>" for b in badges)
    return f"""{head(title, desc, 'services.html', lang)}
{header('services', 'services.html', lang)}

  <main class="wrap">
    <section class="page-hero">
      <div class="hero-card services-hero">
        <span class="eyebrow">{escape(eyebrow)}</span>
        <h1>{escape(h1)}</h1>
        <p>{escape(p)}</p>
        <div class="compact-badges services-badges">{badge_html}</div>
      </div>
    </section>

    <section class="section">
      <div class="section-head">
        <div>
          <span class="eyebrow">{escape(overview)}</span>
          <h2>{escape(h2)}</h2>
        </div>
      </div>

      <div class="services-grid refined-services-grid">
        <article class="list-card service-card service-card-wide">
          <div class="service-head">
            <span class="service-mark">{escape(j_mark)}</span>
            <h3>{escape(j_title)}</h3>
          </div>
          <p class="service-note">{escape(j_note)}</p>
          <div class="service-columns">
            {journal_cols}
          </div>
        </article>

        <article class="list-card service-card">
          <div class="service-head">
            <span class="service-mark">{escape(c_mark)}</span>
            <h3>{escape(c_title)}</h3>
          </div>
          <p class="service-note">{escape(c_note)}</p>
          <div class="compact-badges service-chip-list">{confs}</div>
        </article>
      </div>
    </section>

{footer(footer_text)}"""


def page_contact(lang):
    if lang == "zh":
        title = "唐霖峰 | 联系"
        desc = "唐霖峰的联系方式与学术合作信息。"
        eyebrow = "联系"
        h1 = "联系"
        p = "欢迎围绕图像融合、视频融合、图像增强和视觉-语义感知等方向开展学术合作与研究交流。"
        badges = ["学术合作", "项目交流", "学生交流"]
        contact_labels = {
            "Email": ("邮箱", "linfeng0419@gmail.com"),
            "Google Scholar": ("Google Scholar", "学术主页"),
            "GitHub": ("GitHub", "Linfeng-Tang"),
            "ResearchGate": ("ResearchGate", "学术网络"),
            "Zhihu": ("知乎", "timer-69"),
            "ORCID": ("ORCID", "0000-0002-8566-5743"),
            "Wuhan University": ("武汉大学", "武汉，中国 430072"),
        }
        qr_note = "欢迎通过邮箱或微信联系我，学术合作与交流都很欢迎。"
        footer_text = "联系方式。"
    else:
        title = "Linfeng Tang | Contact"
        desc = "Contact information and academic collaboration channels of Linfeng Tang."
        eyebrow = "Contact"
        h1 = "Contact"
        p = "Open to academic collaborations and research discussions on image fusion, video fusion, image enhancement, and visual-semantic perception."
        badges = ["Academic Collaboration", "Project Discussion", "Student Communication"]
        contact_labels = {
            "Email": ("Email", "linfeng0419@gmail.com"),
            "Google Scholar": ("Google Scholar", "Scholar Profile"),
            "GitHub": ("GitHub", "Linfeng-Tang"),
            "ResearchGate": ("ResearchGate", "Academic Network"),
            "Zhihu": ("Zhihu", "timer-69"),
            "ORCID": ("ORCID", "0000-0002-8566-5743"),
            "Wuhan University": ("Wuhan University", "Wuhan, 430072, China"),
        }
        qr_note = "Please feel free to contact me by email or WeChat for academic collaboration and discussion."
        footer_text = "Contact page."
    links = [
        ("accent-red", "gmail.svg", "Email", "mailto:linfeng0419@gmail.com"),
        ("accent-blue", "googlescholar.svg", "Google Scholar", "https://scholar.google.com/citations?user=PyRqpAsAAAAJ&hl=zh-CN"),
        ("accent-dark", "github.svg", "GitHub", "https://github.com/Linfeng-Tang"),
        ("accent-pink", "researchgate.svg", "ResearchGate", "https://www.researchgate.net/profile/Tang-Linfeng-2"),
        ("accent-gold", "zhihu.svg", "Zhihu", "https://www.zhihu.com/people/timer-69"),
        ("accent-blue", "orcid.svg", "ORCID", "https://orcid.org/0000-0002-8566-5743"),
        ("accent-neutral", "whu.ico", "Wuhan University", "https://www.whu.edu.cn/"),
    ]
    cards = []
    for accent, icon, key, url in links:
        strong, em = contact_labels[key]
        target = '' if url.startswith("mailto:") else ' target="_blank" rel="noreferrer"'
        cards.append(f"""            <a class="contact-link-card {accent}" href="{url}"{target}>
              <span class="contact-icon" aria-hidden="true"><img src="{asset('assets/icons/' + icon, lang)}" alt=""></span>
              <span class="contact-copy"><strong>{escape(strong)}</strong><em>{escape(em)}</em></span>
              <span class="contact-arrow">↗</span>
            </a>""")
    badge_html = "".join(f"<span>{escape(b)}</span>" for b in badges)
    return f"""{head(title, desc, 'contact.html', lang)}
{header('contact', 'contact.html', lang)}

  <main class="wrap">
    <section class="page-hero">
      <div class="hero-card contact-hero">
        <span class="eyebrow">{escape(eyebrow)}</span>
        <h1>{escape(h1)}</h1>
        <p>{escape(p)}</p>
        <div class="compact-badges contact-badges">{badge_html}</div>
      </div>
    </section>

    <section class="section">
      <div class="contact-card contact-card-refined">
        <div class="contact-grid">
          <div class="contact-links contact-links-refined">
{chr(10).join(cards)}
          </div>

          <aside class="qr-panel">
            <span class="eyebrow">WeChat</span>
            <img class="qr" src="{asset('assets/img/wechat_qr.png', lang)}" alt="{escape('微信二维码' if lang == 'zh' else 'WeChat QR code')}">
            <p class="qr-note">{escape(qr_note)}</p>
          </aside>
        </div>
      </div>
    </section>

{footer(footer_text)}"""


GENERATORS = {
    "index.html": page_home,
    "publications.html": page_publications,
    "news.html": page_news,
    "honors.html": page_honors,
    "services.html": page_services,
    "contact.html": page_contact,
}


def main():
    (ROOT / "en").mkdir(exist_ok=True)
    for filename, _ in PAGES:
        (ROOT / filename).write_text(GENERATORS[filename]("zh"), encoding="utf-8", newline="\n")
        (ROOT / "en" / filename).write_text(GENERATORS[filename]("en"), encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
