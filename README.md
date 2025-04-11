### 💡 **Projeto: Monitoramento de Pedidos de um E-commerce**

#### 📘 Contexto:
Você tem uma tabela no DynamoDB chamada `Pedidos`. Toda vez que um novo pedido é criado ou alterado (por exemplo, mudança de status), essa informação deve ser capturada via Stream. O Lambda consome essas mudanças e grava um histórico no banco Postgres, que pode ser usado depois para relatórios ou auditoria.

---

### 🔧 Componentes:

- **DynamoDB (Localstack):**
  - Tabela: `Pedidos`
  - Campos:
    - `pedido_id` (PK)
    - `cliente_id`
    - `valor_total`
    - `status` (ex: `pendente`, `processando`, `concluído`, `cancelado`)
    - `data_criacao`

- **Stream do DynamoDB:**
  - Habilitado para `NEW_AND_OLD_IMAGES`, para detectar atualizações.

- **Lambda (Localstack):**
  - Gatilho: mudanças no Stream da tabela `Pedidos`
  - Função:
    - Quando um novo pedido entra, ele insere uma entrada no Postgres na tabela `historico_pedidos`
    - Quando um pedido é atualizado, grava a alteração com o novo status e timestamp

- **Postgres (rodando local ou via Docker):**
  - Tabela: `historico_pedidos`
  - Campos:
    - `id`
    - `pedido_id`
    - `acao` (ex: "criação", "atualização", "cancelamento")
    - `status`
    - `data_evento`

---

### 🏃‍♂️ Como iniciar o projeto?

1. Execute o comando `docker compose up -d` para subir os servicos que a aplicação depende
2. Crie as tabelas no postgres com os SQSl localizados em [lambda-historico-pedidos/db-migrations](lambda-historico-pedidos/db-migrations)
3. Execute os scrips localizados em [lambda-historico-pedidos/scripts](lambda-historico-pedidos/scripts)
em ordem  
  3.1. É necessário executar apenas até o script 003. Os outros são opcionais.  
  3.2. É preciso estar no no diretorio do `lambda-historico-pedidos` para os scripts funcionarem
  corretamente devido a referecia  
  3.3. É preciso dar permissão de execução para os scripts com o comando `chmod`.  
  Ex: `chmod +x ./lambda-historico-pedidos/scripts/*`  
  3.4. Caso os scripts estejam com erro, a causa talvez seja o caracter de fim de linha (CRLF ou LF).
  Para corrigir execute o comando `sed -i 's/\r//' nome_do_script.sh`  

---

### 🧪 Fluxo de Teste:

1. Insere um pedido na tabela `Pedidos` via código/script.
2. DynamoDB aciona o Stream.
3. Lambda é invocado.
4. Lambda grava no Postgres a ação com os dados relevantes.

---

### 🚀 Extras para deixar mais legal:

- Crie um script que simula a criação/atualização de pedidos periodicamente.
- Adicione uma pequena API para listar o histórico de pedidos (usando Flask ou FastAPI).
- Gere um dashboard simples com os pedidos por status.