from bs4 import BeautifulSoup
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import re
import os


def text_cleaning(text):
	text = re.sub(r'<[^>]+>', '', text)
	text = re.sub(r'[^a-zA-ZÀ-ÿ0-9\s]', '', text) 
	text = text.lower()

	return(text)


def trash_content(soup):
    for tag in soup.find_all('header'):
        tag.decompose()

    for tag in soup.find_all('aside', class_='scaffold-layout__aside'):
        tag.decompose()

    for tag in soup.find_all('section', class_='artdeco-card pv-profile-card break-words'):
        tag.decompose()

    for tag in soup.find_all('footer'):
        tag.decompose()


def get_word(path_root):

	text_final = []
	for file in sorted(os.listdir(path_root)):
		with open(os.path.join(path_root,file), 'r', encoding='utf-8') as f: conteudo = f.read()
		soup = BeautifulSoup(conteudo, 'html.parser')
		trash_content(soup)

		text_complete = ' '.join(tag.get_text(separator=' ', strip=True) for tag in soup.find_all(['h1', 'h2', 'h3', 'p', 'span', 'li', 'section', 'div']))
		txt_cleaning = text_cleaning(text_complete)
		text_final.append(txt_cleaning)

	result_string = ", ".join(text_final)
	return(result_string)


def word_cloud(stop_word, final_text):
	wordcloud = WordCloud(
		width=1000,
		height=600,
		background_color='white',
		stopwords=stop_word,
		collocations=True
	).generate(final_text)

	plt.figure(figsize=(12, 6))
	plt.imshow(wordcloud, interpolation='bilinear')
	plt.axis('off')
	plt.title('Word Cloud - LinkedIn Profiles')
	plt.show()


if __name__ == '__main__':
	path_root =  os.path.join(os.getcwd(),"_profile")
	#caminho_html = os.path.join(path_root,"11_gf.html")
	final_text = get_word(path_root)

	stop_word = set(STOPWORDS)
	stop_word.update([
        'linkedin', 'profile', 'experience', 'company', 'present', 'month', 'year',
        'gabriela', 'ferraz'
    ])

	if 1 == 0:
		stop_word = set([
			'de', 'da', 'do', 'em', 'para', 'com', 'o', 'a', 'e', 'é', 'na', 'no', 'os', 'as',
			'por', 'uma', 'um', 'ao', 'como', 'que', 'se', 'não', 'mais', 'também', 'entre',
			'sobre', 'minha', 'meu', 'sou', 'tenho', 'anos', 'linkedin', 'perfil'
		])

	word_cloud(stop_word, final_text)