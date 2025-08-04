# importar la libreria nltk
import nltk
# desde nltk descargar el paquete stopwords
from nltk.corpus import stopwords
nltk.download('stopwords')
#listar las stopwords en ingles
lista_stopwords = stopwords.words('english')
#imprimir las stopwords
print(lista_stopwords)
