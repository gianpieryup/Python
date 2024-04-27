### Scripts Pyspark

https://spark.apache.org/docs/latest/sql-data-sources-json.html


Spark SQL puede inferir automáticamente el esquema de un conjunto de datos JSON y cargarlo como un DataFrame. Esta conversión se puede realizar utilizando `SparkSession.read.json()` para un archivo JSON.


Tenga en cuenta que el archivo que se ofrece como archivo json no es un archivo JSON típico. Cada línea debe contener un objeto JSON válido, independiente y autónomo.

Ejemplo de como deberia verse el archivo

```json
{"ca1":'1', name:"Jorde"}   // salto de linea
{"ca1":'2', name:"Pedor"}   // salto de linea
{"ca1":'3', name:"Esteban"}  // salto de linea
...
```