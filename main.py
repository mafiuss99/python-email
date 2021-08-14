from flask import Flask, render_template, request
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import sys

app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
    return render_template('sendEmail.html')

@app.route('/enviar', methods=['POST'])
def enviarEmail():
    email = request.form.get('email')
    senha = request.form.get('senha')
    dest = request.form.get('dest')
    assunto = request.form.get('assunto')
    mensagem = request.form.get('mensagem')

    msg = MIMEMultipart()
    texto = assunto
    senha = senha
    msg['From'] = email
    msg['To'] = dest
    msg['Subject'] = mensagem
    msg.attach(MIMEText(texto, 'plain'))

    try:
        # Criação do servidor"
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
    except:
        return "Tivemos um problema para iniciar o servidor"
        sys.exit()

    try:
        # Login na conta para envio
        server.login(msg['From'], senha)
    except:
        return "Usuário ou senha incorretos"
        sys.exit()

    try:
        # envio da Mensagem
        server.sendmail(msg['From'], msg['To'], msg.as_string())
        # encerramento do servidor
        server.quit()
    except:
        return "Tivemos um problema ao tentar eviar a mensagem"
        sys.exit()

    return 'Email Enviado com sucesso!!!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)