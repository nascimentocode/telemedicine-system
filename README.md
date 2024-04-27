# Sistema de Telemedicina em Python com Django

Este é um projeto de sistema de telemedicina desenvolvido em Python usando o framework web Django. O projeto está dividido em três apps Django: `usuario`, `medico` e `paciente`.

## O que é Telemedicina?

A telemedicina é um campo da medicina que utiliza tecnologias de comunicação, como a internet e a telefonia, para fornecer assistência médica à distância. Ela permite que médicos e pacientes realizem consultas, diagnósticos e tratamentos sem a necessidade de estarem fisicamente no mesmo local.

## Funcionalidades

### Aplicativo `usuario`

Este aplicativo lida com o gerenciamento de usuários do sistema.

- Registro de novos usuários.
- Login e autenticação de usuários.
  
### Aplicativo `medico`

Este aplicativo gerencia as funcionalidades relacionadas aos médicos.

- Registro e gerenciamento de médicos.
- Agendamento de consultas por parte dos médicos.
- Visualização das consultas.

### Aplicativo `paciente`

Este aplicativo trata das funcionalidades relacionadas aos pacientes.

- Agendamento de consultas por parte dos pacientes.
- Acesso as consultas e resultados de exames.

## Instalação

Certifique-se de ter o Python e o Django instalados em sua máquina antes de prosseguir.

1. Clone este repositório:

    Utilizando HTTPS:
    ```bash
    git clone https://github.com/nascimentocode/telemedicine-system.git
    ```
      
    ou utilizando o SSH:
      
    ```bash
    git clone git@github.com:nascimentocode/telemedicine-system.git
    ```
    
2. Navegue até o diretório do projeto:
    ```bash
    cd nome-do-repositorio
    ```
    
3. Instale as Dependências:

      ```bash
      pip install -r requirements.txt
      ```

## Configuração

1. Crie e aplique as migrações do banco de dados:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```
    
2. Crie um superusuário para acessar a área de administração:
    ```bash
    python manage.py createsuperuser
    ```
    
3. Inicie o servidor de desenvolvimento:
    ```bash
    python manage.py runserver
    ```
    
4. Acesse o sistema em `http://localhost:8000`.
