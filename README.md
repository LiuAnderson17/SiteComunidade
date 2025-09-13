```markdown
# 🌐 SiteComunidade

## 📋 Descrição

O **SiteComunidade** é uma aplicação web desenvolvida em **Flask** que simula uma rede social simples.  
Os usuários podem criar uma conta, fazer login e interagir com a comunidade por meio de postagens personalizadas.  
O projeto foi criado para praticar desenvolvimento back-end com Flask, autenticação de usuários, CRUD completo e upload de imagens.

---

## 🚀 Funcionalidades

- 👤 **Cadastro e Login de Usuários**.  
- 📝 **CRUD de Postagens**: criar, visualizar, editar e excluir posts.  
- 🎨 **Formatação de texto** nas postagens.  
- 🖼️ **Upload de imagens** junto às postagens.  
- 🌍 **Timeline comunitária**: visualizar posts de outros usuários.  
- 🔒 Controle de permissões (usuário só pode editar/excluir os próprios posts).  

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3  
- **Framework:** Flask  
- **Banco de Dados:** SQLite  
- **Frontend:** HTML, CSS, Jinja2 Templates  
- **IDE/Editor:** VSCode e PyCharm (configuração explicada abaixo)  
- **Controle de Versão:** Git & GitHub  

---

## 📂 Estrutura do Projeto


SiteComunidade/
│
├── static/                      # arquivos estáticos (CSS, imagens, JS)
├── templates/                   # templates HTML (Jinja2)
├── uploads/                     # uploads de imagens
├── main.py                      # ponto de entrada da aplicação Flask
├── requirements.txt             # dependências do projeto
└── README.md                    # documentação do projeto

````

---

## ▶️ Como executar o projeto localmente

### 1. Clonar o repositório

```bash
git clone https://github.com/LiuAnderson17/SiteComunidade.git
cd SiteComunidade
````

### 2. Criar ambiente virtual

```bash
python -m venv venv
```

* **Linux / macOS**

  ```bash
  source venv/bin/activate
  ```
* **Windows (PowerShell)**

  ```bash
  venv\Scripts\activate
  ```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

### 4. Executar o projeto

```bash
python main.py
```

Acesse no navegador:

```
http://127.0.0.1:5000
```

---

## ⚙️ Executando no VSCode

1. Abra a pasta do projeto no **VSCode**.
2. Certifique-se de selecionar o **interpretador Python** correto (Ctrl+Shift+P → “Python: Select Interpreter” → escolha o `venv`).
3. Abra o arquivo **`main.py`** e clique em **Run ▶** ou use `F5` para rodar com debug.

---

## ⚙️ Executando no PyCharm

1. Abra a pasta do projeto no **PyCharm**.
2. Vá em **File > Settings > Project: SiteComunidade > Python Interpreter** e selecione o `venv`.
3. Crie uma **Run Configuration**:

   * Em **Script path**, selecione `main.py`.
   * Salve a configuração.
4. Clique em **Run ▶** para executar o projeto.

---

## 📌 Melhorias Futuras

* 📱 Layout responsivo para mobile.
* 🔍 Busca e filtros de postagens.
* ❤️ Curtidas e comentários.
* 📤 Deploy online (Render, Railway, etc.).
* ✅ Testes automatizados.

---

## 📫 Contato

* GitHub: [LiuAnderson17](https://github.com/LiuAnderson17)
* Email: *[seuemail@dominio.com](mailto:liu.anderson17@gmail.com)*
