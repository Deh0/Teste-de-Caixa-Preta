# Teste de Caixa Preta

O teste de caixa preta é uma metodologia de testes de software em que o testador avalia as funcionalidades do sistema sem ter acesso ao código-fonte ou ao conhecimento da estrutura interna do software. O foco está nas entradas e saídas: o testador fornece dados de entrada e observa as respostas do sistema, validando se o comportamento está de acordo com os requisitos especificados. Esse tipo de teste pode ser utilizado tanto para validar funcionalidade quanto para avaliar aspectos como desempenho, segurança, e usabilidade. 

O objetivo seria realizar testes de forma automatizada para verificar se o software faz o que deveria fazer, para verificar isso existem dois tipos de testes, o teste funcional e o teste não funcional

- <strong>Teste Funcional:</strong> O teste funcional é focado na autenticação do sistema e entrada de dados, que verifica se o sistema autentica corretamente usuários válidos e rejeita tentativas inválidas, alguns exemplos seriam: “Login com credenciais corretas”, onde o sistema deve permitir acesso. “Login com senha errada”, onde o sistema deve rejeitar o acesso. “Login com usuário inexistente”, onde o sistema também deve rejeitar. Outro ponto importante para o teste funcional seria a verificação de entrada de dados, que valida o comportamento do sistema ao receber diferentes tipos de entrada nos campos login, alguns exemplos seriam: “Inserção de caracteres especiais”, “Inserção de SQL Injection” para verificar tratamento de segurança, “Limite de caracteres nos campos”.

- <strong>Teste Não Funcional:</strong> O teste não funcional é focado na segurança e na usabilidade, com o objetivo avaliar se o sistema é resistente a ataques comuns, exemplo de casos de teste: “Tentativas de brute force”, que seriam múltiplos logins seguidos. “Teste de SQL Injection no campo senha”. “Verificação de mensagens de erro”, não devem revelar informações sensíveis. O teste não funcional na parte de usabilidade tem como objetivo avaliar a experiência do usuário ao interagir com o sistema de autenticação, exemplos de critérios: “Mensagens de erros claras e objetivas”. “Facilidade de navegação”. “Feedback visual adequado após ações do usuário”. 

# Ferramentas que foram utilizadas para testes: 

- <strong>Selenium:</strong> O selenium serve para automação de testes funcionais em aplicações web. Permite simular ações do usuário no navegador, como clicar, preencher formulários e navegar entre páginas. Será utilizado principalmente em testes funcionais, como autenticação, navegação, validação de formulários e testes de sistemas. O selenium suporta múltiplos navegadores e linguagens de programação, e permite integração com frameworks de testes como o Pytes, isso facilita a automação de testes repetitivos e aumenta a cobertura dos testes funcionais. 

- <strong>Pytest:</strong> O pytest é um framework para organizar, executar e estruturar testes automatizados em Python. Será utilizados para testes funcionais quanto para alguns testes não funcionais (como testes de desempenho simples). O pytest facilita a criação de testes legíveis e manuenção dos scripts, pode ser integrado ao Selenium para criar testes web automatizados com relátorios detalhados. 

- <strong>PyAutoGUI:</strong> O PyAutiGUI serve para automação de interações com a interface gráfica do usuário, contolando mouse e teclado para automatizar tarefas em qualquer aplicativo, incluindo desktop. Será utilizado para testes funcionais em aplicações desktop, testes de interface, e também pode ajudar em testes não funcionais que envolvem interação com o sistema operacional.

# Sistema que foi realizado os testes funcionais: 
