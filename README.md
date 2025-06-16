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

O Parabank é uma aplicação web simuladora de um sistema bancário que oferece operações comuns como abertura de conta, transferências, depósitos e saques. Por ser uma aplicação completa, com interface e funcionalidades bem definidas, ela é ideal para testes de caixa preta, cujo objetivo é validar as funcionalidades do sistema sem conhecimento do código interno.
Nesse contexto, utilizamos o Parabank para realizar testes funcionais, focando no Login, para garantir que o sistema se comporte conforme esperado, aceitando credenciais válidas e rejeitando inválidas, além de verificar mensagens de erro apropriadas. Também aplicamos testes não funcionais para avaliar aspectos como desempenho, segurança, usabilidade e confiabilidade do sistema, garantindo que o Parabank não só funcione corretamente, mas também atenda a requisitos de qualidade além da funcionalidade.

- <strong>Teste de Login com credenciais corretas:</strong> Para verificar se o sistema verifica corretamente um usuário quando ele fornece um nome de usuário e senha válidos. Ou seja, o teste confirma que ao inserir os dados de acesso legítimos, o sistema permite o acesso á conta, garantindo que o proceso de autenticalção está funcionando como esperado. 
![image](https://github.com/user-attachments/assets/c0c9932c-70e3-45c9-81dd-2d9354430b44)

- <strong>Teste de Login com Senha Incorreta:</strong>Testar Login com senha incorreta propositalmente é útil para o teste de caixa preta porque permite validar se o sistema reage corretamente a entradas inválidas, sem precisar conhecer seu funcionamento interno. Esse tipo de teste verifica se o sistema bloqueia o acesso e exibe mensagens de erro apropriadas, garantindo que a funcionalidade de autenticação está protegendo o sistema contra acessos indevidos. No contexto do teste funcional, esse teste é importante para confirmar que o sistema cumpre os requisitos especificados, ou seja, que ele rejeita credenciais incorretas e impede o login, evitando falhas de segurança e melhorando a confiabilidade do sistema.
![image](https://github.com/user-attachments/assets/8dc69c3f-c557-40b1-bc4a-6bc2314b6c90)

- <strong>Teste de Login com Usuário Inexistente:</strong> Testar o login com um usuário inexistente significa verificar se o sistema responde corretamente quando alguém tenta acessar com um nome de usuário que não está cadastrado, segue a mesma lógica do teste de Login com Senha Incorreta.
![image](https://github.com/user-attachments/assets/3946e6b9-7d23-462b-99c7-3ecfe9e031c3)

- <strong> Teste de Login com Caraceters Especias:</strong> O Parabank recusa Login com caraceteres especiais, então foi feito uma automação com selenium e pytest para verificação dessa informação, tendo que retornar uma mensagem de erro a respeito disso.
 ![image](https://github.com/user-attachments/assets/1b642d1a-2647-49fb-b278-9aa17de05092)

- <strong> Teste de Login com Inserção de SQL Injection:</strong> O teste de inserção de SQL Injection consiste em tentar inserir comandos SQL maliciosos nos campos de entrada de uma aplicação (como o formulário de login) para verificar se o sistema é vulnerável a esse tipo de ataque. O objetivo é explorar falhas na validação e tratamento dos dados fornecidos pelo usuário, que, se concatenados diretamente em consultas SQL, podem permitir que um invasor modifique a consulta original e obtenha acesso não autorizado, extraia, modifique ou exclua dados do banco.

Era pra ter retornado uma mensagem de "Teste de login com SQL injection passou", porém não apareceu mensagem de erro no sistema, dando erro e não passasndo no teste. 
![image](https://github.com/user-attachments/assets/0aba9f8d-0aa5-4d39-9d39-dcc6fb32f739)

- <strong> Teste de Login com Limite de Caracteres nos Campos:</strong> O teste de login com limite de caracteres consiste em verificar se o sistema aceita apenas uma quantidade adequada de caracteres nos campos de usuário e senha, garantindo que entradas muito longas ou muito curtas sejam tratadas corretamente. Esse teste é importante para evitar problemas como estouro de buffer, falhas na validação e possíveis vulnerabilidades de segurança.
![image](https://github.com/user-attachments/assets/55ea8ff8-3fa0-4c1f-9e51-70edf0c148da)




