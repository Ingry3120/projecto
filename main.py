# importar la libreria nltk
import nltk
nltk.download('punkt_tab')
# desde nltk descargar el paquete stopwords
from nltk.corpus import stopwords
nltk.download('stopwords')
#definir la ruta de los archivos de nltk
nltk.data.path.append(r'C:/Users/igonzsu/AppData/Roaming/nltk_data')
# Vamos a importar NLTK (Natural Language Toolkit) que nos va a ayudar a trabajar con lenguaje natural
import nltk

# Definir la ruta donde se almacenarán los datos descargados de NLTK
nltk.data.path.append('C:\\Users\\yeiso\\AppData\\Local\\nltk_data')

# Descargamos la lista de palabras vacías stopwords que son palabras comunes como el, la, los, etc.
nltk.download('stopwords')

# Importar la función que divide un texto en palabras
from nltk.tokenize import word_tokenize

# Importar la lista de palabras vacías stopwords en español
from nltk.corpus import stopwords

# Imporar la herramienta para calcular la frecuencia de palabras en un texto
from nltk.probability import FreqDist

# Definimos un texto en español que queramos analizar

texto = """
Mi nombre es Juan Manuel González Suárez, mi edad es 36 años, mi ciudad es Bogotá, mi país es Colombia, mi email es juanmanuelgonzalezsuarez@gmail.com, mi teléfono es 3178456923, mi género es masculino
Mi nmbre es Ingry Tatana González Suárez, mi edad es 20 años, mi ciudad es Bogotá, mi país es Colombia, mi email es ingrytatana@gmail.com, mi teléfono es 3178456923, mi género es femenino
"""

# Tokenización: Convertimos el texto en una lista de palabras individuales
palabras = word_tokenize(texto, language= 'spanish')

# Mostramos la lista de palabras obtenidas
print(palabras)

# Obtenemos la lista de palabras vacías en español, es decir, cargamos las stopwords en español. Aquí obtenemos una lista de palabras comunes en español que normalmente no necesistamos para el análisis. 
stop_words = set(stopwords.words('spanish'))

# Filtramos las palabras: eliminamos las stopwords y los signos de puntuación
# Recorremos cada palabra en una lista llamada palabras. Si la palabra no está en las stopwords y es una palabra real (sin números ni símbolos), la guardamos.

palabras_filtradas = [palabras for palabras in palabras if palabras.lower() not in stop_words and palabras.isalpha()]

# Mostramos la lista de palabras después del filtrado.
# Resultado: Nos quedamos solo con las palabras importantes.
print(palabras_filtradas)

# Calculamos la frecuencia de cada palabra en la lista filtrada
frecuencia_de_las_palabras = FreqDist(palabras_filtradas)

# Mostramos las 10 palabras más comunes y la cantidad de veces que aparecen
print(frecuencia_de_las_palabras.most_common(10))