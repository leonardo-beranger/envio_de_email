from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import os

def enviar_email(destinatarios, assunto, texto_html, copia=[], caminhos_anexo=[]):
    # Configurações do e-mail e do servidor SMTP
    remetente = 'seu_email@gmail.com' # <- coloque seu e-mail
    senha = 'senha' # <- coloque sua senha de app, crie uma com essa dica: https://www.youtube.com/watch?v=4Qgz2c7yR7s
     
    try:
        # Criando a mensagem
        msg = MIMEMultipart()
        msg['From'] = remetente
        msg['To'] = ', '.join(destinatarios)
        msg['Cc'] = ', '.join(copia)
        msg['Subject'] = assunto

        # Corpo do e-mail em formato HTML
        msg.attach(MIMEText(texto_html, 'html'))

        # Anexando os arquivos, se fornecidos
        for caminho_anexo in caminhos_anexo:
            anexo = MIMEBase('application', 'octet-stream')
            with open(caminho_anexo, 'rb') as file:
                anexo.set_payload(file.read())
            encoders.encode_base64(anexo)
            anexo.add_header('Content-Disposition', f'attachment; filename={os.path.basename(caminho_anexo)}')
            msg.attach(anexo)

        # Configurando o servidor SMTP do Gmail
        servidor = smtplib.SMTP('smtp.gmail.com', 587)
        servidor.starttls()
        servidor.login(remetente, senha)
        servidor.sendmail(remetente, destinatarios + copia, msg.as_string())
        servidor.quit()

        print("E-mail enviado com sucesso!")
    except Exception as e:
        print(f"Falha ao enviar o e-mail: {e}")
