import requests
import json

url = "http://localhost:5000/generate-docx"

# 要发送的数据
data = {
    "company": "未来科技有限公司",
    "employees": [
        { "name": "张三", "role": "工程师", "age": 28 },
        { "name": "李四", "role": "设计师", "age": 31 },
        { "name": "王五", "role": "产品经理", "age": 30 }
    ]
}

# 打开模板文件
with open("final_template.docx", "rb") as template_file:
    files = {
        "template": template_file
    }
    form_data = {
        "data": json.dumps(data, ensure_ascii=False)
    }
    response = requests.post(url, files=files, data=form_data)

# 检查响应状态并保存文件
if response.status_code == 200:
    with open("employee_report1.docx", "wb") as f:  # 修改保存的文件名
        f.write(response.content)
    print("Word 文档已保存为 employee_report1.docx")  # 同步修改提示信息
else:
    print("请求失败：", response.status_code, response.text)
