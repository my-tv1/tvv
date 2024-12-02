import requests

# 获取原始文件内容
url = "https://gitee.com/deng-meiqing/iptv1/raw/main/live.txt"
response = requests.get(url)

# 检查是否成功获取文件
if response.status_code == 200:
    content = response.text.splitlines()
    
    # 删除前5行
    content = content[5:]
    
    # 删除包含"CCTV5+"的行
    content = [line for line in content if "CCTV5+" not in line]
    
    # 保存修改过的文件为ipvt.txt，指定编码为utf-8
    with open("ipvt.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(content))
    print("文件已成功保存为ipvt.txt")
else:
    print("无法获取文件，HTTP状态码:", response.status_code)
