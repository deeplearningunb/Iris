# Iris

Iris é um software que faz uso de redes neurais para relizar a análise de sentimento de tweets em português para identificação de usuários que estão com algum tipo de problema de saúde mental.

## Problemática

Neste século um transtorno mental que está se tornando cada vez mais comum é a depressão, e segundo a Organização Mundial da Saúde (OMS), mais de 300 milhões de pessoas sofrem com esta doença em todo o mundo.
A depressão se manifesta de forma diferente em cada indivíduo e com diferentes níveis de intensidade. Nos quadros mais graves, a depressão pode fazer com que o indivíduo cometa suicídio.

## Solução

Geralmente, as pessoas com depressão, manifestam indícios de suicídio através de seus comportamentos, porém muitas vezes eles não são percebidos ou não são levados a sério. Qualquer pessoa que tenha um agravamento muito severo de um quadro depressivo, a ponto de não querer mais viver (mesmo que não mencione se matar), é um candidato em potencial ao suicídio.
Visto que o primeiro passo para se evitar um suicídio é identificar estes comportamentos, nós escolhemos realizar esta busca na rede social Twitter, que é um site onde há um maior número de pessoas que divulgam o que estão sentindo e o que estão fazendo. Para isso, nós utilizamos redes neurais que auxiliarão na identificação de perfis de usuários que com depressão.

## Construção do Projeto

Com base em varios artigos, escolhemos fizer a **Rede Neural Convolucional** (CNN). A fim de conseguir uma acurácia aceitável no projeto, fizemos um dicionario de palavras brasileiras com base em mais de 600 mil _tweets_. Para a análise de sentimento da Rede Neural, usamos 4 mil tweets classificados como depressivos e os 4 mil classificados como não depressivos, e separamos 80% deles para treinamento, e 20% para teste. Com isso, conseguimos a acurácia de 92,10%.

![acurácia](./assets/acuracia.png)

Além disso, é possivel escolher um perfil no twitter e fazer uma análise de sentimento do perfil com base nos seus tweets

## Público Alvo

Com este software, nós buscamos identificar as milhares de pessoas que utilizam a plataforma Twitter e que sofrem deste transtorno mental, e com isso gerar dados para que seja possível evitar possíveis suicídios.

## Equipe

### Requisitos necessários dos integrantes

Para a realização deste software é necessário que na equipe contenha:

- Desenvolvedores com conhecimento de python
- Desenvolvedores que saibam implementar uma rede neural

### Lider da Equipe

O integrante escolhido para liderar a equipe é o Andrew Lucas

### Regras de Conduta

É possível verificar as regras de conduta [aqui](https://github.com/deeplearningunb/Iris/blob/master/CODE_OF_CONDUCT.md)

### Quantidade de pessoas na equipe

Foram designadas 5 pessoas para realizar o desenvolvimento do software

## Planejamento

### Objetivo

O nosso objetivo é ajudar pessoas que têm depressão evitando que elas cometam suicídio.

### Metas

Construir um software que faça reconhecimento de tweets com tendências depressivas e identifique estes perfis de usuários.

### Tarefas

As atividade para a construção do software pode ser conferída na página de Issues, [aqui](https://github.com/deeplearningunb/Iris/issues)

### Membros

| Nome               | Matrícula  | GitHub                                                    | Email                       |
| ------------------ | ---------- | --------------------------------------------------------- | --------------------------- |
| Guilherme Deusdará | 16/0122996 | [gdeusdara](https://github.com/gdeusdara)                 | guibanci@gmail.com          |
| Andrew Lucas       | 16/0023921 | [andrewlucasgs](https://github.com/andrewlucasgs)         | andrewlucasgs@gmail.com     |
| Gabriel Filipe     | 16/0121019 | [gabrielfilipe7unb](https://github.com/gabrielfilipe7unb) | gabrielfilipe7unb@gmail.com |
| Lucas Penido       | 16/0013243 | [LucasPenido](https://github.com/LucasPenido)             | lpenidoa@me.com             |
| João Zarbielli     | 17/0146251 | [zarbielli](https://github.com/zarbielli)                 | jlfz06@gmail.com            |

### Stakeholders

Professor Diego Dorgam [@diegodorgam](https://github.com/diegodorgam)
