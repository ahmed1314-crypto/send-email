
from flask import Flask, request, jsonify
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'chatyahmed8@gmail.com'
app.config['MAIL_PASSWORD'] = '0051720187zeko'
app.config['MAIL_DEFAULT_SENDER'] = 'chatyahmed8@gmail.com'

mail = Mail(app)

@app.route('/send-report', methods=['POST'])
def send_report():
    data = request.form
    location = data.get('location')
    file = request.files.get('image')

    if not file or not location:
        return jsonify({'status': 'error', 'message': 'بيانات ناقصة'}), 400

    msg = Message("تقرير جديد من الجهاز", recipients=["Zakaria.m.krayem@gmail.com"])
    msg.body = f"الموقع:\n{location}"
    msg.attach(filename="captured.jpg", content_type=file.content_type, data=file.read())

    try:
        mail.send(msg)
        return jsonify({'status': 'success', 'message': 'تم الإرسال بنجاح'}), 200
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
