ip_version_priority = "ipv6"

source_urls = [
    "https://live.fanmingming.com/tv/m3u/ipv6.m3u",
   # "https://m3u.ibert.me/fmml_ipv6.m3u",
   # "https://ghp.ci/https://raw.githubusercontent.com/dengmeiqing/IPTV1/main/直播/央视频道.txt",
   # "https://live.zhoujie218.top/tv/iptv6.txt",
    #"https://live.zhoujie218.top/tv/iptv4.txt",
   # "https://www.mytvsuper.xyz/m3u/Yang.m3u",
   # "https://tv.youdu.fan:666/live/",
   # "http://ww.weidonglong.com/dsj.txt",
    #"http://xhztv.top/zbc.txt",
    "https://raw.githubusercontent.com/dengmeiqing/IPTV1/refs/heads/main/live.txt",
    #"https://ghp.ci/https://raw.githubusercontent.com/qingwen07/awesome-iptv/main/tvbox_live_all.txt",
    #"https://ghp.ci/https://raw.githubusercontent.com/Guovin/TV/gd/output/result.txt",
   # "http://home.jundie.top:81/Cat/tv/live.txt",
   # "https://ghp.ci/https://raw.githubusercontent.com/vbskycn/iptv/master/tv/hd.txt",
    #"https://cdn.jsdelivr.net/gh/YueChan/live@main/IPTV.m3u",
    #"https://fm1077.serv00.net/SmartTV.m3u",
    #"https://ghp.ci/https://raw.githubusercontent.com/kimwang1978/collect-tv-txt/main/merged_output.txt"
]

url_blacklist = [
     "http://[2409:8087:1a01:df::7005]:80/ottrrs.hl.chinamobile.com/TVOD/88888888/224/3221226559/index.m3u8",
     "http://[2409:8087:1a01:df::7005]:80/ottrrs.hl.chinamobile.com/PLTV/88888888/224/3221226540/index.m3u8",
     "http://[2409:8087:1a01:df::7005]/ottrrs.hl.chinamobile.com/PLTV/88888888/224/3221226540/index.m3u8",
     "http://ottrrs.hl.chinamobile.com/PLTV/88888888/224/3221226540/index.m3u8",
     "2409:8087:1a01:df::4077",
  
]
url_whitelist = [
    "ottrrs.hl.chinamobile.com",
   # "2409:8087:5e00:24::1e",
    "2409:8087:74d9:21::6",
    "2409:8087:5e08:24::11",
    "221.233.192.152:1111",
   # "218.89.240.144:59901",
]

announcements = [
    {
        "channel": "公告",
        "entries": [
            {"name": "请阅读", "url": "https://liuliuliu.tv/api/channels/1997/stream", "logo": "http://175.178.251.183:6689/LR.jpg"},
            {"name": "yuanzl77.github.io", "url": "https://liuliuliu.tv/api/channels/233/stream", "logo": "http://175.178.251.183:6689/LR.jpg"},
            {"name": "更新日期", "url": "https://gitlab.com/lr77/IPTV/-/raw/main/%E4%B8%BB%E8%A7%92.mp4", "logo": "http://175.178.251.183:6689/LR.jpg"},
            {"name": None, "url": "https://gitlab.com/lr77/IPTV/-/raw/main/%E8%B5%B7%E9%A3%8E%E4%BA%86.mp4", "logo": "http://175.178.251.183:6689/LR.jpg"}
        ]
    }
]

epg_urls = [
    "https://live.fanmingming.com/e.xml",
    "http://epg.51zmt.top:8000/e.xml",
    "http://epg.aptvapp.com/xml",
    "https://epg.pw/xmltv/epg_CN.xml",
    "https://epg.pw/xmltv/epg_HK.xml",
    "https://epg.pw/xmltv/epg_TW.xml"
]
