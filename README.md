# ge-elenco-brasileirao2018-crawler
Crawler ["simples"] para obtenção de dados da "Avaliação dos elencos do Brasileirão 2018" feita pelo GloboEsporte.com

Por volta do início de abril de 2018 o GloboEsporte.com publicou um conteúdo especial contendo uma avaliação dos principais jogadores dos 20 times da elite do futebol brasileiro no endereço http://app.globoesporte.globo.com/futebol/brasileirao-serie-a/guia/avaliacao-dos-elencos-brasileirao-2018.

Segundo descrição da própria publicação:

> O Brasileirão está começando, e o GloboEsporte.com volta a avaliar os principais jogadores dos 20 clubes da elite. Vale lembrar que o momento vivido pelo atleta conta na hora de escolher seu status.

Este trabalho resultou em uma avaliação (pontuação) de 23 jogadores de cada um dos times conforme as categorias (critérios):

* `1`: É craque (6 pontos)
* `2`: Joga muito (4 pontos)
* `3`: Agrega valor (3 pontos)
* `4`: Compõe elenco (2 pontos)
* `5`: Sujeito a vaias (1 ponto)
* `6`: Irrita a torcida (não pontua)

A partir disso foi criado um ranking dos times. Neste momento (13/04/2018) o Palmeiras é o time com maior pontuação (79) e o Paraná, com a menor (40).

A publicação não informa mais detalhes do processo de avaliação (quem foram os avaliadores, qual o período de avaliação etc.), mas informa que foi considerada a situação atual de cada jogador.

Este repositório é um crawler para os dados desta publicação e foi criado, inicialmente, como um exercício de desenvolvimento de crawler em Python. Para isso utiliza [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) e [Requests](http://docs.python-requests.org/en/master/).

Ao ser executado o programa `main.py` gera quatro arquivos na pasta local:

* `evaluation_criterion.csv`: armazena os critérios de avaliação; colunas: `id`, `label`
* `players_positions.csv`: armazena as posições dos jogadores; colunas: `id`, `label`
* `teams.csv`: armazena dados dos times; colunas: `id`, `name`, `shield_image_url`, `description`, `stats_1`, `stats_2`, `stats_3`, `stats_4`, `stats_5`, `stats_6` (cada coluna `stats_n` representa a quantidade de jogadores do critério `n`)
* `players_evaluations.csv`: armazena dados de avaliações dos jogadores; colunas: `team`, `id`, `name`, `photo_url`, `position`, `evaluation`

Este repositório já inclui estes arquivos (gerados em 13/04/2018 por volta de 01:00:00, horário de Brasília).

Quem sabe o pessoal do GloboEsporte.com continua avaliando esses jogadores a cada rodada do Brasileirão 2018 e poderemos ver esses dados gerarem um *lindo* conjunto de dados para análises mais elaboradas =)

> **Aviso**: o código não está comentado, nem modularizado e nem faz tratamentos, por isso use por sua conta e risco :p

