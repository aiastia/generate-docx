from flask import Flask, request, send_file
from docxtpl import DocxTemplate
from io import BytesIO

app = Flask(__name__)

@app.route('/generate-docx', methods=['POST'])
def generate_docx():
    try:
        # 获取上传的模板文件
        template_file = request.files.get('template')
        if not template_file:
            return {"error": "未上传模板文件"}, 400

        # 获取数据（假设前端用 form-data 传递 json 字符串）
        data = request.form.get('data')
        if not data:
            return {"error": "未提供数据"}, 400

        import json
        data = json.loads(data)

        # 用上传的模板生成文档
        doc = DocxTemplate(template_file)
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