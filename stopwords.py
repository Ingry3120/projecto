#importar libreria nltk
import nltk

# DESDE NLTK DESCARGAR LOS STOPWORDS
from nltk.corpus import stopwords
nltk.download('stopwords')
lista_stopwords = stopwords.words('spanish')#lista de stopwords en español
# IMPRIMIR LOS STOPWORDS
print(stopwords.words('spanish'))





