# Frontend — Clientes & Pedidos (Vue 3 + Vite)
Interface para o desafio técnico (CRUD de Clientes e Pedidos).

## Requisitos
- Node.js 18+ e npm
- Backend exposto em `http://localhost:5000/api` (ajuste via `.env`)

## Configuração
```bash
cp .env.example .env
# edite VITE_API_BASE_URL se necessário
npm install
npm run dev
```

## Rotas esperadas no Backend
- **Clientes**
  - `GET /api/clientes` — suporta filtros `id`, `nome`, `email`, `page`, `per_page`. Retorna `{ items, total }` ou lista simples.
  - `GET /api/clientes/:id`
  - `POST /api/clientes` — body `{ nome, email }`
  - `PUT /api/clientes/:id` — body `{ nome, email }`
  - `DELETE /api/clientes/:id` — deve retornar erro (p.ex. 409) se houver pedidos vinculados.
- **Pedidos**
  - `GET /api/pedidos` — filtros `id`, `descricao`, `valor`, `id_cliente`, `page`, `per_page`.
  - `GET /api/pedidos/:id`
  - `POST /api/pedidos` — body `{ descricao, valor, id_cliente }`
  - `PUT /api/pedidos/:id`
  - `DELETE /api/pedidos/:id`

## Notas de UX
- Listas carregam automaticamente ao abrir as páginas.
- Filtros reagem conforme digitação (com debounce onde faz sentido).
- Paginação simples (10/20/50 por página).
- Mensagens de erro do backend são exibidas quando disponíveis.
- Ao excluir, há confirmação de clique.

## Estrutura
```
src/
  components/
    ActionBar.vue
    ConfirmDelete.vue
  services/
    api.js
  views/
    ClientsList.vue
    ClientForm.vue
    OrdersList.vue
    OrderForm.vue
  router/
    index.js
  App.vue
  main.js
  styles.css
```
