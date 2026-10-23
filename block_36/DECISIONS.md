# Decisión: `staticmethod` o función de módulo

Para la conversión de kilómetros a millas implementé dos alternativas: un `@staticmethod` dentro de la clase `Kilometers` y una función normal definida directamente en el módulo.

Después de comparar ambas opciones, dejaría finalmente la **función de módulo**.

## Responsabilidad

La conversión de kilómetros a millas solamente necesita recibir una cantidad y devolver el resultado convertido.

No necesita acceder al estado de un objeto `Kilometers`.

Por ejemplo, para realizar la conversión no es necesario conocer:

```python
self.kilometers
```

La operación puede realizarse únicamente con el valor recibido como argumento.

## Cohesión

La conversión está relacionada con distancias, por lo que colocarla como `staticmethod` dentro de `Kilometers` no sería incorrecto.

Sin embargo, la función sigue siendo independiente del estado y comportamiento de una instancia concreta. Por eso considero que puede mantenerse como una utilidad del módulo sin necesidad de pertenecer a la clase.

## Dependencia de instancia

La conversión no depende de `self`.

No es necesario crear:

```python
kilometers = Kilometers(25)
```

para poder convertir otro valor diferente.

Una función de módulo puede recibir directamente el número que se quiere convertir.

## Dependencia de clase

La operación tampoco necesita `cls`.

No crea nuevas instancias de `Kilometers`, no modifica atributos de clase y no necesita conocer ninguna configuración de la clase.

Por ese motivo tampoco sería necesario utilizar `@classmethod`.

## Claridad de la API

Con una función de módulo, queda claro que la conversión es una operación independiente:

```python
kilometers_to_miles(10)
```

En cambio, utilizar:

```python
Kilometers.kilometers_to_miles(10)
```

puede dar la impresión de que la conversión depende de alguna característica de la clase, aunque realmente solo utiliza el argumento recibido.

## Decisión final

Mantendría la conversión como **función normal del módulo**.

`@staticmethod` funciona y permite agrupar la operación dentro de `Kilometers`, pero en este caso no aprovecha ninguna característica de la clase.

La función de módulo representa mejor que la conversión:

- no depende de una instancia;
- no depende de la clase;
- únicamente transforma un valor recibido;
- puede utilizarse de manera independiente.

Por estas razones considero que la función de módulo produce una API más simple y expresa mejor la responsabilidad real de la operación.