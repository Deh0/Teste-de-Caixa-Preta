# Teste de Caixa Preta

Nome dos participantes: Débora 2320516, Gabriel Sela 2320449, e Ruhan Faria 2222062 

O teste de caixa preta é uma metodologia de testes de software em que o testador avalia as funcionalidades do sistema sem ter acesso ao código-fonte ou ao conhecimento da estrutura interna do software. O foco está nas entradas e saídas: o testador fornece dados de entrada e observa as respostas do sistema, validando se o comportamento está de acordo com os requisitos especificados. Esse tipo de teste pode ser utilizado tanto para validar funcionalidade quanto para avaliar aspectos como desempenho, segurança, e usabilidade. 

O objetivo seria realizar testes de forma automatizada para verificar se o software faz o que deveria fazer, para verificar isso existem dois tipos de testes, o teste funcional e o teste não funcional

- **Teste Funcional:** O teste funcional é focado na autenticação do sistema e entrada de dados, que verifica se o sistema autentica corretamente usuários válidos e rejeita tentativas inválidas, alguns exemplos seriam: “Login com credenciais corretas”, onde o sistema deve permitir acesso. “Login com senha errada”, onde o sistema deve rejeitar o acesso. “Login com usuário inexistente”, onde o sistema também deve rejeitar. Outro ponto importante para o teste funcional seria a verificação de entrada de dados, que valida o comportamento do sistema ao receber diferentes tipos de entrada nos campos login, alguns exemplos seriam: “Inserção de caracteres especiais”, “Inserção de SQL Injection” para verificar tratamento de segurança, “Limite de caracteres nos campos”.

- **Teste Não Funcional:** O teste não funcional é focado na segurança e na usabilidade, com o objetivo avaliar se o sistema é resistente a ataques comuns, exemplo de casos de teste: “Tentativas de brute force”, que seriam múltiplos logins seguidos. “Teste de SQL Injection no campo senha”. “Verificação de mensagens de erro”, não devem revelar informações sensíveis. O teste não funcional na parte de usabilidade tem como objetivo avaliar a experiência do usuário ao interagir com o sistema de autenticação, exemplos de critérios: “Mensagens de erros claras e objetivas”. “Facilidade de navegação”. “Feedback visual adequado após ações do usuário”. 

# Ferramentas que foram utilizadas para testes: 

- **Selenium:** O selenium serve para automação de testes funcionais em aplicações web. Permite simular ações do usuário no navegador, como clicar, preencher formulários e navegar entre páginas. Será utilizado principalmente em testes funcionais, como autenticação, navegação, validação de formulários e testes de sistemas. O selenium suporta múltiplos navegadores e linguagens de programação, e permite integração com frameworks de testes como o Pytes, isso facilita a automação de testes repetitivos e aumenta a cobertura dos testes funcionais. 

- **Pytest:** O pytest é um framework para organizar, executar e estruturar testes automatizados em Python. Será utilizados para testes funcionais quanto para alguns testes não funcionais (como testes de desempenho simples). O pytest facilita a criação de testes legíveis e manuenção dos scripts, pode ser integrado ao Selenium para criar testes web automatizados com relátorios detalhados. 

# Sistema que foi realizado os testes: 

O Parabank é uma aplicação web simuladora de um sistema bancário que oferece operações comuns como abertura de conta, transferências, depósitos e saques. Por ser uma aplicação completa, com interface e funcionalidades bem definidas, ela é ideal para testes de caixa preta, cujo objetivo é validar as funcionalidades do sistema sem conhecimento do código interno.
Nesse contexto, utilizamos o Parabank para realizar testes funcionais, focando no Login, para garantir que o sistema se comporte conforme esperado, aceitando credenciais válidas e rejeitando inválidas, além de verificar mensagens de erro apropriadas. Também aplicamos testes não funcionais para avaliar aspectos como desempenho, segurança, usabilidade e confiabilidade do sistema, garantindo que o Parabank não só funcione corretamente, mas também atenda a requisitos de qualidade além da funcionalidade.

# Teste Funcional:
✅ **Teste de Login com credenciais corretas:** Para verificar se o sistema verifica corretamente um usuário quando ele fornece um nome de usuário e senha válidos. Ou seja, o teste confirma que ao inserir os dados de acesso legítimos, o sistema permite o acesso á conta, garantindo que o proceso de autenticalção está funcionando como esperado. 

Retornou o resultado esperado, conseguiu entrar no site e realizar o login corretamente.


✅ **Teste de Login com Senha Incorreta:** Testar Login com senha incorreta propositalmente é útil para o teste de caixa preta porque permite validar se o sistema reage corretamente a entradas inválidas, sem precisar conhecer seu funcionamento interno. Esse tipo de teste verifica se o sistema bloqueia o acesso e exibe mensagens de erro apropriadas, garantindo que a funcionalidade de autenticação está protegendo o sistema contra acessos indevidos. No contexto do teste funcional, esse teste é importante para confirmar que o sistema cumpre os requisitos especificados, ou seja, que ele rejeita credenciais incorretas e impede o login, evitando falhas de segurança e melhorando a confiabilidade do sistema.

Retonou o resultado esperado, erro por ter colocado uma senha inválida.

✅ **Teste de Login com Usuário Inexistente:** Testar o login com um usuário inexistente significa verificar se o sistema responde corretamente quando alguém tenta acessar com um nome de usuário que não está cadastrado, segue a mesma lógica do teste de Login com Senha Incorreta.

Retornou o resultado esperado, erro por ter colocado um usuário inexistente.

✅ **Teste de Login com Caraceters Especias:** O Parabank recusa Login com caraceteres especiais, então foi feito uma automação com selenium e pytest para verificação dessa informação, tendo que retornar uma mensagem de erro a respeito disso.

Retornou o resultado esperado, o sistema não permitiu caracteres especiais e informou um erro. 

❌ **Teste de Login com Inserção de SQL Injection:** O teste de inserção de SQL Injection consiste em tentar inserir comandos SQL maliciosos nos campos de entrada de uma aplicação (como o formulário de login) para verificar se o sistema é vulnerável a esse tipo de ataque. O objetivo é explorar falhas na validação e tratamento dos dados fornecidos pelo usuário, que, se concatenados diretamente em consultas SQL, podem permitir que um invasor modifique a consulta original e obtenha acesso não autorizado, extraia, modifique ou exclua dados do banco.

Esperava-se uma mensagem confirmando que o teste de SQL Injection foi bloqueado ('Teste de login com SQL injection está agindo de acordo com o esperado'), porém nenhuma mensagem de erro foi exibida, indicando possível falha na validação dos inputs. O que pode informar que o sistema pode estar vulnerável ou não retornou feedback visível.

✅ **Teste de Login com Limite de Caracteres nos Campos:** O teste de login com limite de caracteres consiste em verificar se o sistema aceita apenas uma quantidade adequada de caracteres nos campos de usuário e senha, garantindo que entradas muito longas ou muito curtas sejam tratadas corretamente. Esse teste é importante para evitar problemas como estouro de buffer, falhas na validação e possíveis vulnerabilidades de segurança.

Retornou o resultado esperado, erro por que o sistema não permitiu e constou.

# Teste Não Funcional:

✅ **Brute Force:** O teste não funcional de brute force consiste em avaliar a capacidade do sistema de resistir a ataques de força bruta, que são tentativas automatizadas de adivinhar senhas ou credenciais por meio de múltiplas tentativas sequenciais, geralmente usando softwares que testam diversas combinações até encontrar a correta.

Retornou o resultado esperado, sistema não permitiu brute force. 

❌ **Teste de SQL Injection no campo senha:** O teste de SQL Injection no campo senha, no contexto de teste não funcional, tem como objetivo verificar se a aplicação é vulnerável a ataques que exploram falhas no tratamento das entradas do usuário para manipular comandos SQL. Ao inserir códigos maliciosos no campo senha, como ' OR '1'='1, o teste busca identificar se a aplicação executa a consulta SQL de forma insegura, permitindo que um invasor contorne a autenticação e acesse o sistema sem credenciais válidas.
  
Como não retornou o erro esperado, provavelmente a SQL Injection funcionou, isso significa que a aplicação não está segura.

✅ **Teste de Verificação de mensagens de erro:** O teste de verificação de mensagens de erro no contexto de teste não funcional consiste em avaliar se o sistema apresenta mensagens claras, informativas e adequadas quando ocorrem erros ou falhas, como em tentativas de login com dados incorretos. Esse teste vai além de simplesmente verificar se a funcionalidade está correta; ele analisa a usabilidade e a experiência do usuário, garantindo que as mensagens ajudem o usuário a entender o problema e saibam como proceder.

Retornou no resultado esperado, não obteve nenhuma informação sensível durante o teste. 

✅ **Teste de Feedback Visual:** O teste de feedback visual, no contexto de teste não funcional, avalia como o sistema comunica visualmente ao usuário o resultado de suas ações, como confirmações, erros ou carregamentos. Esse tipo de teste verifica se o sistema apresenta indicadores claros e imediatos. Esse feedback visual é fundamental para a usabilidade, um aspecto não funcional, pois melhora a experiência do usuário, reduz dúvidas e evita frustrações. Além disso, garante que o sistema seja acessível e responsivo a diferentes interações, contribuindo para a confiabilidade e eficiência do software.

Retornou o resultado esperado.

✅ **Teste de Tempo de Resosta:** O tempo de resposta, no contexto de teste não funcional, refere-se ao tempo que o sistema leva para responder a uma solicitação do usuário, como o carregamento de uma página ou a autenticação em um login. Esse parâmetro é fundamental para avaliar o desempenho do software, garantindo que ele seja rápido e eficiente sob condições normais de uso.

Retornou o resultado esperado.

# Conclusão dos Testes

Tanto no teste funcional quanto no teste não funcional, houve falha no teste de SQL Injection, isso é extremamente perigoso porque essa vulnerabilidade permite que invasores insiram comandos SQL maliciosos em campos de entrada, como o Login ou Senha, explorando falhas no tratamento dos dados pelo sistema. No teste funcional, a falha indica que o sistema não está validando ou filtrando corretamente as entradas, permitindo que comandos maliciosos sejam executados, o que compromete a funcionalidade esperada da aplicação, como autenticação segura e integridade dos dados.
Já no teste não funcional, a falha revela uma grave vulnerabilidade de segurança que pode levar a consequências severas, como exposição de dados confidenciais, alteração ou exclusão de informações, acesso não autorizado a contas e até controle total do sistema pelo invasor. Além disso, essa falha pode comprometer a confiabilidade, a privacidade dos usuários e causar danos financeiros e à reputação da empresa.


# Sistema começou a dar erro

O Parabank começou a permitir o acesso de contas não cadastradas, não autorizadas, exemplo: se fosse fazer um teste de colocar caracteres no usuário ou na senha não seria informado nenhuma mensagem de erro, e conseguiria acessar a conta, mesmo a conta não existindo. 



# Teste de Integração: 
class TesteIntegracaoAPIAvaliacoes(APITestCase):
    """
    Teste de Integração para API de Avaliações
    Verifica integração entre:
    - API Views + Serializers
    - Models + Database
    - Request/Response handling
    - Validação de dados
    """
    
    def setUp(self):
        self.client = APIClient()
        
        # Cria dados de teste
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        
        self.hotel = Hotel.objects.create(
            nome='SupenCaro',
            endereco='Rua só isso mesmo',
            cidade='Curitiba'
        )
        
        self.hospede = Hospede.objects.create(
            nome='Vinicius',
            email='vinicius@gmail.com',
            telefone='419975622585'
        )
        
        self.list_url = '/api/avaliacoes/'  
        self.create_url = '/api/avaliacoes/create/'  
        
    def test_integracao_api_listar_avaliacoes_sem_filtro(self):
        """
        Teste de integração: API + Database + Serializer
        Verifica listagem sem filtros
        """
        print("\n=== TESTE: Listar Avaliações sem Filtro ===")
        
        avaliacao1 = Avaliacoes.objects.create(
            hotel=self.hotel,
            hospede=self.hospede,
            comentario='Excelente hotel!',
            nota=5,
        )
        
        avaliacao2 = Avaliacoes.objects.create(
            hotel=self.hotel,
            hospede=self.hospede,
            comentario='Muito bom!',
            nota=4,
        )
        
        # Testa integração API + Database
        response = self.client.get(self.list_url)
        
        print(f"Status da resposta: {response.status_code}")
        print(f"Quantidade de avaliações retornadas: {len(response.data)}")
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)  
        
        print("✓ Integração API + Database funcionando corretamente")
    
    def test_integracao_api_listar_avaliacoes_com_filtro(self):
        """
        Teste de integração: API + Query Parameters + Database
        Verifica filtro por hotel_id
        """
        print("\n=== TESTE: Listar Avaliações com Filtro por Hotel ===")
        
        # Cria avaliação no banco
        avaliacao = Avaliacoes.objects.create(
            hotel=self.hotel,
            hospede=self.hospede,
            comentario='Hotel maravilhoso!',
            nota=5,
        )
        
        # Testa integração com query parameters
        response = self.client.get(f"{self.list_url}?hotel_id={self.hotel.id}")
        
        print(f"Status da resposta: {response.status_code}")
        print(f"Hotel ID usado no filtro: {self.hotel.id}")
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        
        # Verifica se o serializer está funcionando corretamente
        avaliacao_data = response.data[0]
        self.assertEqual(avaliacao_data['comentario'], 'Hotel maravilhoso!')
        self.assertEqual(avaliacao_data['nota'], 5)
        self.assertEqual(avaliacao_data['nome_hospede'], 'Vinicius')
        
        print("✓ Integração API + Filtros + Serializer funcionando")
    
    def test_integracao_api_criar_avaliacao_dados_validos(self):
        """
        Teste de integração: API POST + Serializer + Database
        Verifica criação de avaliação com dados válidos
        """
        print("\n=== TESTE: Criar Avaliação - Dados Válidos ===")
        
        dados_avaliacao = {
            'hotel': self.hotel.id,
            'hospede': self.hospede.id,
            'comentario': 'Experiência incrível!',
            'nota': 5
        }
        
        # Conta avaliações antes da criação
        count_antes = Avaliacoes.objects.count()
        print(f"Avaliações antes: {count_antes}")
        
        # Testa integração API POST + Database
        response = self.client.post(
            self.create_url, 
            dados_avaliacao, 
            format='json'
        )
        
        print(f"Status da resposta: {response.status_code}")
        
        # Verifica se foi salvo no banco
        count_depois = Avaliacoes.objects.count()
        print(f"Avaliações depois: {count_depois}")
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(count_depois, count_antes + 1)
        
        # Verifica se os dados foram salvos corretamente
        nova_avaliacao = Avaliacoes.objects.latest('id')
        self.assertEqual(nova_avaliacao.comentario, 'Experiência incrível!')
        self.assertEqual(nova_avaliacao.nota, 5)
        self.assertEqual(nova_avaliacao.hotel, self.hotel)
        
        print("✓ Integração API POST + Database funcionando")
    
    def test_integracao_api_criar_avaliacao_dados_invalidos(self):
        """
        Teste de integração: API + Validação + Error Handling
        Verifica tratamento de dados inválidos
        """
        print("\n=== TESTE: Criar Avaliação - Dados Inválidos ===")
        
        # Dados inválidos (
        dados_invalidos = {
            'hotel': self.hotel.id,
            'hospede': self.hospede.id,
            'comentario': '',  
            'nota': 10  
        }
        
        count_antes = Avaliacoes.objects.count()
        
        response = self.client.post(
            self.create_url, 
            dados_invalidos, 
            format='json'
        )
        
        print(f"Status da resposta: {response.status_code}")
        print(f"Erros retornados: {response.data}")
        
        # Verifica que não foi salvo no banco
        count_depois = Avaliacoes.objects.count()
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(count_depois, count_antes)  
        
        print("✓ Integração API + Validação funcionando")
    
    def test_integracao_completa_ciclo_crud_api(self):
        """
        Teste de integração completo: Ciclo CRUD via API
        """
        print("\n=== TESTE: Ciclo Completo CRUD via API ===")
        
        # 1. CREATE - Cria via API
        dados_create = {
            'hotel': self.hotel.id,
            'hospede': self.hospede.id,
            'comentario': 'Teste CRUD',
            'nota': 4
        }
        
        response_create = self.client.post(
            self.create_url, 
            dados_create, 
            format='json'
        )
        
        self.assertEqual(response_create.status_code, status.HTTP_201_CREATED)
        avaliacao_id = response_create.data['id']
        print(f"✓ CREATE: Avaliação criada com ID {avaliacao_id}")
        
        # 2. READ - Lista via API
        response_list = self.client.get(f"{self.list_url}?hotel_id={self.hotel.id}")
        self.assertEqual(response_list.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response_list.data) > 0)
        print("✓ READ: Avaliação listada com sucesso")
        
        # 3. Verifica integração Database + Serializer
        avaliacao_db = Avaliacoes.objects.get(id=avaliacao_id)
        self.assertEqual(avaliacao_db.comentario, 'Teste CRUD')
        print("✓ Integração Database + API confirmada")
        
        print("✓ Ciclo CRUD completo via API funcionando")
    
    def test_integracao_api_performance_multiplas_avaliacoes(self):
        """
        Teste de integração: Performance com múltiplas avaliações
        """
        print("\n=== TESTE: Performance com Múltiplas Avaliações ===")
        
        # Cria múltiplas avaliações
        avaliacoes_criadas = []
        for i in range(10):
            avaliacao = Avaliacoes.objects.create(
                hotel=self.hotel,
                hospede=self.hospede,
                comentario=f'Comentário {i+1}',
                nota=(i % 5) + 1,  
            )
            avaliacoes_criadas.append(avaliacao)
        
        print(f"Criadas {len(avaliacoes_criadas)} avaliações")
        
        # Testa performance da listagem
        response = self.client.get(f"{self.list_url}?hotel_id={self.hotel.id}")
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 10)
        
        for avaliacao_data in response.data:
            self.assertIn('id', avaliacao_data)
            self.assertIn('comentario', avaliacao_data)
            self.assertIn('nota', avaliacao_data)
            self.assertIn('nome_hospede', avaliacao_data)
        
        print("✓ Performance com múltiplas avaliações OK")
    
    def test_integracao_api_relacoes_foreign_key(self):
        """
        Teste de integração: Relacionamentos Foreign Key via API
        """
        print("\n=== TESTE: Relacionamentos Foreign Key ===")
        
        avaliacao = Avaliacoes.objects.create(
            hotel=self.hotel,
            hospede=self.hospede,
            comentario='Teste relacionamentos',
            nota=5,
        )
        
        response = self.client.get(f"{self.list_url}?hotel_id={self.hotel.id}")
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        avaliacao_data = response.data[0]
        
        # Verifica se o relacionamento está sendo serializado corretamente
        self.assertEqual(avaliacao_data['nome_hospede'], 'João Silva')
        self.assertEqual(avaliacao_data['hotel'], self.hotel.id)
        
        print("✓ Relacionamentos Foreign Key funcionando via API")

class TesteIntegracaoAPICompleto(TestCase):
    """
    Teste de integração adicional para cenários complexos
    """
    
    def setUp(self):
        self.client = APIClient()
        
    def test_integracao_api_sem_dados(self):
        """
        Teste de integração: API com banco vazio
        """
        print("\n=== TESTE: API com Banco Vazio ===")
        
        response = self.client.get('/api/avaliacoes/')
        
        # Deve retornar lista vazia, mas status 200
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)
        
        print("✓ API funciona corretamente mesmo sem dados")
    
    def test_integracao_api_headers_content_type(self):
        """
        Teste de integração: Headers e Content-Type
        """
        print("\n=== TESTE: Headers e Content-Type ===")
        
        response = self.client.get('/api/avaliacoes/')
        
        # Verifica headers da resposta
        self.assertEqual(response['Content-Type'], 'application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        print("✓ Headers e Content-Type corretos")
