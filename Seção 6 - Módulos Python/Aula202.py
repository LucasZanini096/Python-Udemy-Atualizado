# O módulo requests para requisisções HTTP no Python 
# HTTP (HyperText Transfer Protocol) é um protocolo usado para enviar e 
# receber dados na Internet. Ele funciona no modo cliente/servidor, onde o cliente 
# (seu navegador, por exemplo) faz uma requisição ao servidor
# (site, por exemplo), que responde com os dados adequados.
#
# A mesnagem de requisição do cleinte deve incluir dados como:
# O método HTTP
#       -leitura (safe) - Get(Ler), Head (cabeçalhos), Options (métodos suportados)
#       -escrita - Post, Put (substitui), Patch (atualiza), Delete
# Quando digito uma url em que no final aparece barra, estou tentando acessar a página de um Site.
# - O endereço do recurso a ser acessado (/users/) -> tentando aessar um dado específico
# Os cabeçahos HTTP (Content-Type, Authorization)
# O Corpo da mensagem (caso necessário, de acordo com o método HTTTP)
#
# A mensagem de resposta do servidor deve incluir dados como:
# -código de status HTTP (200 success, 404 Not found, 301 Moved Permanently)
# - Os cabeçahos HTTP (Content-Type, Accept) 
# - O corpo da mensagem (Pode estar vazio em alguns casos)

#Restante das aulas no ambiente virtual 