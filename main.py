import nltk
import pymorphy2
from nltk import sent_tokenize
from nltk.tokenize import word_tokenize

nltk.download('punkt_tab')

text = open('src.txt', 'r', encoding='utf-8')
text = text.read()
print(text)

sentences = sent_tokenize(text)
print(len(sentences))

words = word_tokenize(text)
print(len(words))


def c1(w1, w2):
    if (w1.tag.POS == 'NOUN' or w1.tag.POS == 'ADJF') and (w2.tag.POS == 'NOUN' or w2.tag.POS == 'ADJF'):
        return True
    else:
        return False


def c2(w1, w2):
    if (w1.tag.case == w2.tag.case) and (w1.tag.number == w2.tag.number) and (w1.tag.gender == w2.tag.gender):
        return True
    else:
        return False


morph_analyzer = pymorphy2.MorphAnalyzer()

cleared_words = []

for w in words:
    if w.isalpha():
        cleared_words.append(w)

words = cleared_words

for j in range(len(words) - 1):
    w1 = morph_analyzer.parse(words[j])[0]
    w2 = morph_analyzer.parse(words[j + 1])[0]
    if c1(w1, w2) and c2(w1, w2):
        print(w1.normal_form, w2.normal_form)
