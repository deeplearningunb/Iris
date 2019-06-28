import pandas as pd
import twint
import nest_asyncio


def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i : i + n]


def get_user_tweets(user, keywords):
    c = twint.Config()
    c.Username = user
    c.Search = keywords
    c.Custom["tweet"] = ["id", "tweet", "link", "date", "time"]
    #     c.Since = datetime.strftime(datetime.now() - timedelta(1), '%Y-%m-%d')
    #     c.Until = datetime.strftime(datetime.now(), '%Y-%m-%d')
    c.Store_csv = True
    c.Store_object = True
    c.Format = ""
    c.Output = "users/" + user + ".csv"
    twint.run.Search(c)


def get_users_tweets():
    for user in TWEETS["username"]:
        for keyword in KEYWORDS:
            print("fetching " + user)
            get_user_tweets(user, keyword)


KEYWORDS = """amigos pessoas cair companheiro quarto faculdade agradável diversão organizar desfrutar caber conversa tempo chupar estúpido odeio inferno bebida merda foda lixo fumo ruim garoto droga louco cachorra pessoa futuro vida possibilidade crescer controle sonho mente mudança momento sentir experiência acontecimento aprenda sono noite manhã cama dia hora tarde amanhã mate estudo sonolento acordado amor vida feliz coração chorar triste mundo duro cicatriz cicatrizes perfeito sentimento sorriso sorrir cuidado forte maravilhoso verdade estranho falar cachorro tempo louco triste coisas engraçado paraíso acontecer ruim lembrar dia ódio adivinhar louco noite machucado tipo cabeça parada olho mão começar sentir tempo dedo braço pescoço mover cadeira estômago incomodar executar ombro dor sensação preocupação estresse estudo tempo difícil relaxar nervoso teste foco escola ansioso concentrado pressão difícil extremamente constantemente oprimir sentir tempo razão deprimir momento ruim mudança confortável erro sozinho sentimento perder culpado emoção confundir realizar conforto superior aconteça odeio doe doente sinto mal magoa cuidado errado acontecer bagunça horrível estúpido louco deixar pior difícil lidar chorar"""

KEYWORDS = KEYWORDS.split(" ")
KEYWORDS = list(dict.fromkeys(KEYWORDS))

KEYWORDS = list(chunks(KEYWORDS, 46))
for i, l in enumerate(KEYWORDS):
    KEYWORDS[i] = " OR ".join(l)

nest_asyncio.apply()

for tweets in range(1, 46):

    file = "data/tweets{}.csv".format(tweets)

    TWEETS = pd.read_csv(file)

    get_users_tweets()
