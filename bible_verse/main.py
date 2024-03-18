import random 

bible_verses = [
    "O Senhor é meu pastor; nada me faltará. - Salmo 23:1",
    "O amor é paciente, o amor é bondoso. Não inveja, não se vangloria, não se orgulha. - 1 Coríntios 13:4",
    "Porque Deus amou o mundo de tal maneira que deu o seu Filho unigênito, para que todo aquele que nele crê não pereça, mas tenha a vida eterna. - João 3:16",
    "Tudo posso naquele que me fortalece. - Filipenses 4:13",
    "O Senhor é a minha luz e a minha salvação; a quem temerei? O Senhor é a fortaleza da minha vida; a quem me recearei? - Salmo 27:1",
    "Confia no Senhor de todo o teu coração, e não te estribes no teu próprio entendimento. - Provérbios 3:5",
    "Pois onde estiver o teu tesouro, aí estará também o teu coração. - Mateus 6:21",
    "Vinde a mim, todos os que estais cansados e oprimidos, e eu vos aliviarei. - Mateus 11:28",
    "Não andem ansiosos por coisa alguma, mas em tudo, pela oração e súplicas, e com ação de graças, apresentem seus pedidos a Deus. - Filipenses 4:6",
    "Mas, a todos quantos o receberam, aos que crêem no seu nome, deu-lhes o poder de se tornarem filhos de Deus. - João 1:12",
    "Bem-aventurados os humildes de espírito, porque deles é o Reino dos céus. - Mateus 5:3",
    "E conhecereis a verdade, e a verdade vos libertará. - João 8:32",
    "Buscai primeiro o Reino de Deus, e a sua justiça, e todas essas coisas vos serão acrescentadas. - Mateus 6:33",
    "Porque onde estiverem dois ou três reunidos em meu nome, aí estou eu no meio deles. - Mateus 18:20",
    "Assim, eles já não são dois, mas sim uma só carne. Portanto, o que Deus uniu, ninguém separe. - Mateus 19:6",
    "Peça e lhe será dado; busque e encontrará; bata e a porta será aberta para você. - Mateus 7:7",
    "Nem só de pão viverá o homem, mas de toda palavra que procede da boca de Deus. - Mateus 4:4",
    "Então disse Jesus: Deixem vir a mim as crianças e não as impeçam; porque o Reino dos céus pertence aos que são semelhantes a elas. - Mateus 19:14",
    "Se Deus é por nós, quem será contra nós? - Romanos 8:31",
    "Este é o dia que o Senhor fez; regozijemo-nos e alegremo-nos nele. - Salmo 118:24",
    "No princípio, Deus criou os céus e a terra. - Gênesis 1:1"
]


def get_bible_verse():
    return random.choice(bible_verses)

def print_bible_verse():
    print(random.choice(bible_verses))