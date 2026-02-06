### **1. Visão Geral da Arquitetura**

O projeto implementa uma variante da **Clean Architecture** (Arquitetura Limpa), com forte influência de **Domain-Driven Design (DDD)**. A estrutura busca o desacoplamento total entre o core business e as ferramentas externas (frameworks, drivers de banco de dados e bibliotecas de segurança).

**Fluxo de Dados:**

1. **Request:** A requisição atinge a camada de **HTTP Controllers**.  
2. **Orquestração:** O Controller utiliza **Dependency Injection** para instanciar a camada de **Services**.  
3. **Domínio:** O Service recupera ou manipula **Entities** de domínio, utilizando **Value Objects** para validação estrutural.  
4. **Persistência:** A comunicação com o banco de dados é feita através de **Interfaces de Repositório**, cujas implementações concretas residem na camada de **Infrastructure** (SQLAlchemy).  
5. **Response:** O dado é mapeado para um **Schema (DTO)** e retornado ao cliente.

*     Client --> Controllers[HTTP Controllers / Gateways]
*     Controllers --> Services[Application Services / Use Cases]
*     Services --> Domain[Domain Entities / Value Objects]  
*     Services --> Repositories[Repository Interfaces]  
*     Repositories --> SQLAlchemy[Infrastructure / SQLAlchemy Implementation]  
*     SQLAlchemy --> DB[(PostgreSQL)]

---

### **2\. Tecnologias Fundamentais**

* **Python 3.11+**: Escolhido pela maturidade do ecossistema e suporte nativo a tipos assíncronos.  
* **FastAPI**: Framework moderno que utiliza Pydantic para validação de dados e gera documentação automática (OpenAPI/Swagger), garantindo alta performance via ASGI.  
* **SQLAlchemy 2.0**: Utilizado como ORM para abstração da camada de dados, permitindo a troca de dialetos de banco de dados com impacto mínimo no domínio.  
* **Alembic**: Ferramenta de migração de banco de dados, permitindo versionamento controlado do schema.  
* **Docker & Docker Compose**: Garante a paridade entre ambientes de desenvolvimento e produção, encapsulando dependências como o banco de dados PostgreSQL.

---

### **3\. Estrutura de Diretórios**

A organização segue um padrão modular que isola preocupações técnicas de conceitos de negócio:

**src/**  
**├── main.py # Ponto de entrada da aplicação**  
**└── app/**  
- **├── core/ # Configurações globais, segurança e DB**  
-  **├── domain/ # Entidades puras e objetos de valor**  
-   **├── http/ # Camada de entrega (Controllers, Routers, Deps)**  
-   **├── repositories/ # Interfaces e implementações de persistência**  
-   **├── schemas/ # Data Transfer Objects (Pydantic models)**  
-   **└── services/ # Lógica de aplicação (Casos de uso)**

**Justificativa:** Esta árvore permite que a infraestrutura (como o repositório SQLAlchemy) seja alterada ou testada em memória sem tocar na lógica de negócio presente em `domain/` ou `services/`.

---

### **4\. Separação de Responsabilidades**

* **Domain (Entities/Value Objects):** Contém a lógica de negócio "pura". As entidades como `User` utilizam `Value Objects` (`Email`, `Username`) para garantir integridade desde a criação.  
* **Services (Use Cases):** Atuam como orquestradores. Eles não sabem "como" um usuário é salvo, apenas que existe um contrato (`UserRepository`) que faz isso.  
* **HTTP (Controllers):** Responsáveis apenas pelo protocolo de entrada. Eles validam o payload via `Schemas` e convertem exceções de negócio em códigos de status HTTP.  
* **Infrastructure (Repositories):** Implementações técnicas. Aqui reside o código específico do SQLAlchemy ou de repositórios em memória para testes unitários.

---

### **5\. Padrões de Design e Princípios**

* **Dependency Injection (DI):** O projeto utiliza extensivamente o sistema de injeção de dependências do FastAPI para injetar repositórios e serviços, facilitando o desacoplamento e a testabilidade.  
* **Dependency Inversion (D do SOLID):** Os serviços dependem de abstrações (Interfaces ABC) e não de implementações concretas de banco de dados.  
* **Single Responsibility Principle (S do SOLID):** Cada controller e service é responsável por um único fluxo ou recurso (Ex: `RegisterUserService`, `DeleteUserService`).  
* **Repository Pattern:** Centraliza a lógica de acesso a dados, ocultando a complexidade das consultas SQL do restante da aplicação.

---

### **6\. Gestão de Erros e Segurança**

A infraestrutura de segurança é centralizada no diretório `core/` e distribuída via dependências HTTP:

* **Segurança:** Implementação de JWT (JSON Web Tokens) com suporte a *Access Tokens* e *Refresh Tokens* persistidos.  
* **Exceções:** O sistema utiliza `ValueError` e exceções personalizadas na camada de serviço, que são capturadas pelos Controllers e transformadas em `HTTPException` com o status code adequado.  
* **Hashing:** Utilização do `passlib` com algoritmos modernos (`bcrypt`) para proteção de credenciais antes da persistência.

