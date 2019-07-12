# visualizing-real-world-data-project

https://github.com/emachadoc/visualizing-real-world-data-project

El objetivo de mi empresa es abrir una sucursal en Alemania, por lo que en 'Clean_companies.ipynb' filtro la base de datos para quedarme exclusivamente con los registros con oficinas en ese país.

Creo un DataFrame seleccionando las columnas que me interesan y descartando las demás y extraigo los datos de ciudad, latitud, longitud y geo para cada oficina de las ubicadas en Alemania y que tengan latitud y longitud. Creo un nuevo DataFrame agregando los datos extraídos y filtro para eliminar los registros nulos de latitud y longitud, ordeno por año de fundación y exporto a .json.

Importo ese archivo en Compass para indexar la geolocalización y me lo llevo a 'Geoindex_queries.ipynb' para realizar las geoqueries. Creo una clase 'Finder' en la que incluyo todas las funciones para localizar las oficinas de otras empresas en distintos radios y aplicarles puntuaciones en función de distintos criterios: distancia, antigüedad, fondos, número de empleados y categoría, para luego sumarlos y asignar una puntuación total a cada ubicación.

La idea es crear un nuevo DataFrame 'points' agregando la columna 'score', que debería devolverme 'Finder' tras el apply, al DataFrame previo 'germany_offices' y generar los gráficos en Tableau desde ese archivo, pero no consigo que me funcionen las geoqueries, que es en lo que estoy trabajando.