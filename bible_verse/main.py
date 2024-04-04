import random 

bible_verses_pt = [
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

bible_verses_en = [
    "The Lord is my shepherd, I lack nothing. - Psalm 23:1",
    "Love is patient, love is kind. It does not envy, it does not boast, it is not proud. - 1 Corinthians 13:4",
    "For God so loved the world that he gave his one and only Son, that whoever believes in him shall not perish but have eternal life. - John 3:16",
    "I can do all this through him who gives me strength. - Philippians 4:13",
    "The Lord is my light and my salvation - whom shall I fear? The Lord is the stronghold of my life — of whom shall I be afraid? - Psalm 27:1",
    "Trust in the Lord with all your heart and lean not on your own understanding. - Proverbs 3:5",
    "For where your treasure is, there your heart will be also. - Matthew 6:21",
    "Come to me, all you who are weary and burdened, and I will give you rest. - Matthew 11:28",
    "Do not be anxious about anything, but in every situation, by prayer and petition, with thanksgiving, present your requests to God. - Philippians 4:6",
    "Yet to all who did receive him, to those who believed in his name, he gave the right to become children of God. - John 1:12",
    "Blessed are the poor in spirit, for theirs is the kingdom of heaven. - Matthew 5:3",
    "Then you will know the truth, and the truth will set you free. - John 8:32",
    "But seek first his kingdom and his righteousness, and all these things will be given to you as well. - Matthew 6:33",
    "For where two or three gather in my name, there am I with them. - Matthew 18:20",
    "So they are no longer two, but one flesh. Therefore what God has joined together, let no one separate. - Matthew 19:6",
    "Ask and it will be given to you; seek and you will find; knock and the door will be opened to you. - Matthew 7:7",
    "Man shall not live on bread alone, but on every word that comes from the mouth of God. - Matthew 4:4",
    "Jesus said, 'Let the little children come to me, and do not hinder them, for the kingdom of heaven belongs to such as these.' - Matthew 19:14",
    "If God is for us, who can be against us? - Romans 8:31",
    "This is the day the Lord has made; let us rejoice and be glad in it. - Psalm 118:24",
    "In the beginning God created the heavens and the earth. - Genesis 1:1"
]




def get_bible_verse_pt():
    return random.choice(bible_verses_pt)

def print_bible_verse_pt():
    print(random.choice(bible_verses_pt))

def get_bible_verse_en():
    return random.choice(bible_verses_en)

def print_bible_verse_en():
    print(random.choice(bible_verses_en))