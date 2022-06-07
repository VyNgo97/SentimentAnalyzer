from nltk.sentiment.util import *
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import utils.data_parser
import pprint as pp
from schemas.request_body import RequestBody


# nltk.download('vader_lexicon')

# words_list = [words for word in sentences for words in sentences if words.isalpha()]

# stopwords = nltk.corpus.stopwords.words('english')

# dir() prints out all attributes and methods of this object

# clean_words = [w for w in sentences for sentences in clean_sentences]

# another way would be [word for line in clean_sentences for word in line.split()]

# clean_words = nltk.word_tokenize(clean_sentences)

# clean_words = [word for word in clean_words if (word.isalpha() and set('aeiou').intersection(word.lower()))]

def analyze(subreddit: str, movie: str):
    df = utils.data_parser.parse_data_to_df(subreddit, movie)
    sentences = [sentence for sentence in df['data.selftext'] if sentence]
    clean_sentences = [re.sub('\W', ' ', sent) for sent in sentences]
    clean_sentences = ' '.join(clean_sentences)
    sid = SentimentIntensityAnalyzer()
    ss = sid.polarity_scores(clean_sentences)
    pp.pprint(ss)
    return ss

if __name__ == '__main__':
    analyze()