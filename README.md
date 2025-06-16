# Envio de E-mail

Biblioteca simples para envio de e-mails utilizando Python e o servidor SMTP do Gmail.

## Estrutura do projeto
- `biblioteca/bib.py` – Implementa a função `enviar_email`, que cria a mensagem, adiciona anexos (caso existam) e realiza o envio usando o Gmail.
- `exemplo.py` – Exemplo de uso da biblioteca: gera dados fictícios com `pandas` e `numpy`, converte o resultado para HTML e envia o relatório por e-mail.

Trecho da função principal (`enviar_email`):

```python
def enviar_email(destinatarios, assunto, texto_html, copia=[], caminhos_anexo=[]):
    remetente = 'seu_email@gmail.com'  # Edite com seu e-mail
    senha = 'senha'                    # Edite com sua senha de app
    ...

enviar_email(
    destinatarios=['seu_email@gmail.com'],
    assunto='Relatório Mensal',
    texto_html=html
)
