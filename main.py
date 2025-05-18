from flask import Flask, request, send_file
from docxtpl import DocxTemplate
from io import BytesIO

app = Flask(__name__)

@app.route('/generate-docx', methods=['POST'])
def generate_docx():
    try:
        # 获取上传的模板文件（如果有）
        template_file = request.files.get('template')
        if template_file:
            doc = DocxTemplate(template_file)
        else:
            # 没有上传模板时，使用默认模板
            doc = DocxTemplate('final_template.docx')

        # 获取数据（假设前端用 form-data 传递 json 字符串）
        data = request.form.get('data')
        if not data:
            return {"error": "未提供数据"}, 400

        import json
        data = json.loads(data)

        # 用模板生成文档
        doc.render(data)

        output_stream = BytesIO()
        doc.save(output_stream)
        output_stream.seek(0)

        return send_file(
            output_stream,
            as_attachment=True,
            download_name='final_template1.docx',
            mimetype='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
        )
    except Exception as e:
        return {"error": str(e)}, 500

if __name__ == '__main__':
    app.run(debug=True)
