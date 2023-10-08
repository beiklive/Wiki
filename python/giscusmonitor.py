import requests
from bs4 import BeautifulSoup
import subprocess
import time
import os

current_directory = os.getcwd()
print("当前工作目录的路径是:", current_directory)

MarkDownText = '''
---
comments: true
---

| 项目名 | 项目地址 | 简介 |
| :--- | :--- | :--- |
'''




def parse_github_project_info(text):
    project_info = "| "
    # 判断字符串是否以指定标志开始和结束
    if "-- Add Github Project --" in text and "-- Add End --"  in text:
        # 按行拆分文本
        lines = text.split('\n')
        for line in lines:
            if ' : ' in line:
                # 按冒号拆分每行，获取键值对
                parts = line.split(' : ')
                if len(parts) == 2:
                    key = parts[0].strip()
                    value = parts[1].strip()
                    project_info += value + " | "
    else:
        return None
    return project_info

def GetFormatComment():
    resultstr = ""
    url = 'https://github.com/beiklive/Gtalk_store/discussions/17'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',  # 请替换为合适的 User-Agent
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
    }
    i = 1
    for i in range(1, 10):
        try:
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')

                comments_elements = soup.find_all('td', class_='d-block color-fg-default comment-body markdown-body js-comment-body')
                comments = [comment.text.strip() for comment in comments_elements]
                print(f"评论:")
                for comment in comments:
                    result = parse_github_project_info(comment)
                    if None != result:
                        # print(comment)
                        # print(result)
                        resultstr += result+"\n"
                return resultstr
            else:
                print(f"无法获取页面。状态码: {response.status_code}")
        except:
            i += 1
            print(f"无法获取页面。开始第{i}次尝试")
    if i == 10:
        print("尝试多次失败,下次再试吧")
    return None

def append_text_to_file(file_path, text_to_append):
    try:
        # 打开文件以读取内容，删除尾部的换行符
        with open(file_path, 'r') as file:
            existing_content = file.read().rstrip('\n')
        
        # 追加新文本并写回文件
        with open(file_path, 'w') as file:
            file.write(existing_content + '\n' + text_to_append)
        
        print("文本已成功追加到文件末尾。")
    except Exception as e:
        print(f"发生错误：{str(e)}")


if __name__ == "__main__":
    res = GetFormatComment()
    if None != res:
        append_text_to_file("/home/runner/work/Wiki/Wiki/docs/docs/other/gayhub.md", res)
        MarkDownText += "\n" + res
        print(MarkDownText)