# Pyspark

### Tips

Para mostrar el contenido completo de las columnas de un Dataframe
```python
# Por defecto solo muestra una cantidad fija de ancho por columna
df.show(truncate=False)

# Por defecto solo se pueden visualizar 20 filas. Si quieres mas aumenta el numero
df.show(20, False)
```


### Parsear

Un campo String con un Schema definido

```python
from pyspark.sql.types import *
schema = StructType([ 
    StructField("Zipcode",StringType(),True), 
    StructField("ZipCodeType",StringType(),True), 
    StructField("City",StringType(),True), 
    StructField("State", StringType(), True)
  ])

#Convert json column to multiple columns
from pyspark.sql.functions import col,from_json
dfJSON = dfFromTxt.withColumn("jsonData",from_json(col("value"),schema)) \
                   .select("jsonData.*")
dfJSON.printSchema()
dfJSON.show(truncate=False)

#==================================================
root
 |-- Zipcode: string (nullable = true)
 |-- ZipCodeType: string (nullable = true)
 |-- City: string (nullable = true)
 |-- State: string (nullable = true)

+-------+-----------+-------------------+-----+
|Zipcode|ZipCodeType|City               |State|
+-------+-----------+-------------------+-----+
|704    |STANDARD   |PARC PARQUE        |PR   |
|704    |STANDARD   |PASEO COSTA DEL SUR|PR   |
|709    |STANDARD   |BDA SAN LUIS       |PR   |
|76166  |UNIQUE     |CINGULAR WIRELESS  |TX   |
|76177  |STANDARD   |FORT WORTH         |TX   |
|76177  |STANDARD   |FT WORTH           |TX   |
|704    |STANDARD   |URB EUGENE RICE    |PR   |
|85209  |STANDARD   |MESA               |AZ   |
|85210  |STANDARD   |MESA               |AZ   |
|32046  |STANDARD   |HILLIARD           |FL   |
+-------+-----------+-------------------+-----+
```


### Archivos Json

Spark SQL puede inferir automáticamente el esquema de un conjunto de datos JSON y cargarlo como un DataFrame. 

Esta conversión se puede realizar utilizando `SparkSession.read.json()` para un archivo JSON. [[Docu]](https://spark.apache.org/docs/latest/sql-data-sources-json.html)  


Tenga en cuenta que el archivo que se ofrece como archivo json no es un archivo JSON típico. Cada línea debe contener un objeto JSON válido, independiente y autónomo.

Ejemplo de como deberia verse el archivo

```json
{"ca1":'1', name:"Jorde"}   // salto de linea
{"ca1":'2', name:"Pedor"}   // salto de linea
{"ca1":'3', name:"Esteban"}  // salto de linea
...
```