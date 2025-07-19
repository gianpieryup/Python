# El bicho

Imaginate el Spyder del python, tenemos un cuadro con los valores de las variables solo que veremos como van cambiando

**El puntito rojo** :red_circle:  :  `breakpoint` ,podemos poner muchos, cada punto es individual. Son los puntos de corte de la ejecución. Ósea que por cada punto la ejecución se detiene y espera confirmación del usuario para poder seguir corriendo.

> TIP: Yo pensaba antes que necesitaba dos puntos mínimo y que el código encerrado... Nao /cada punto es único

### Acceder al bicho

Una ves puesto los :red_circle:, presionar al bicho. El IDE entrara en modo <span style="background:yellow;">debug</span> y podemos manejarlo con los siguientes botones

- **Continue** : Este ejecutara hasta el próximo `breakpoint` o hasta el fin del programa si no hay mas
- **Step over** : Ejecuta lineá por lineá
- **Stop into** : Si hay un llamado a la función entra a esa definición
- **Stop out** : Para salir de esta función

Para salir **Stop** el <span style="color:red;">cuadrito rojo</span> 

> TIP: Cuando entro al modo bicho no se ejecuta la lineá del breakpoint, si no todo lo anterior

<span style="background:yellow;">Sucede mucho que si no asignamos un valor a una variable al ser declara se llena de basura, por lo que esto me ayuda mucho</span>