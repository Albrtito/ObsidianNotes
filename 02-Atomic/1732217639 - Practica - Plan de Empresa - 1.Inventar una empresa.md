---
aliases:
  - Practica - Plan de Empresa - 1.Inventar una empresa
  - Inventar una empresa
tags:
  - Empresa
References: 
cssclasses:
---
#  Plan de Empresa - 1. Inventar una empresa

> [!NOTE] Requisito: 
> Describir el campo de actividad de la empresa (producto o servicio). 
> 

## 1. Inventar una empresa:

### 1.1 Descripción del servicio
El campo de actividad de la empresa propuesta se encuentra dentro del mercado de seguros. La empresa **ofrece un seguro de matrícula para estudiantes universitarios**[^4]

La empresa se creará en un único mercado y nación, convirtiéndola en una **empresa nacional de monomercado**
### 1.2 Qué es un seguro de matrícula?
Un seguro de matrícula es un servicio ofrecido por la empresa dirigido a estudiantes universitarios. 

 Al contratar este seguro el estudiante pagará un precio **variable** en función de **su nota de ebau, nota media universitaria y nº de matrícula**. A  cambio la empresa asegura que pagará el valor de la siguiente matrícula  **en caso de que el estudiente suspendiese la asignatura**

Algunas características a remarcar del seguro son: 
+ El estudiante contratará un seguro **para UNA única asignatura**, contratando otro seguro diferente en caso de que quiera asegurar otra asignatura.

#### Computo del seguro:
El cálculo realizado para calcular el seguro será: 

**En caso de que el estudiante sea de nuevo acceso a la universidad (primer año)**
+ Se utiliza **unicamente la nota de ebau**
+ Se descuenta un máximo del 50%

El precio se calcula resolviendo:
$$
\text{Precio} = \text{PM} * (1 - (\frac{\text{NB}}{14})*0.5)
$$
Donde: 
+ **PM**: (Precio Matrícula) Es el precio de la siguiente (segunda)matrícula de la asignatura. 
+ **NB**: (Nota Ebau) Nota de ebau sobre 14

**En caso de que el estudiante no sea de nuevo acceso a la universidad(cualquiera menos el primer año)**
+ Se utiliza **la nota de ebau,la nota media universitaria y el número de matrícula**
+ Se descontará un máximo del 80% subdividido de la siguiente forma: 
	+ 50% Dependiente de la nota media universitaria 
	+ 30% Dependiente de la nota de ebau
+ Se subirá el precio un 10% sobre el precio calculado por cada matrícula extra: 
  > Entonces para la segunda matrícula se sube un 10%, para la tercera un 20%…

El precio se calcula resolviendo:
$$
\text{Precio} = (\text{PM} * ( 1-\text{FE} + \text{FU})) +( PM * (0.1 * (NM - 1)))
$$
Donde:
+ **NB:** (Nota Ebau) Nota de ebau sobre 14
+ **NM:** (Número matrícula) Con rango empezando en 1
+ **NU:**( Nota Universidad) Nota media de la universidad sobre 10
+ **FE:** (Factor Ebau) Se calcula resolviendo:
$$
\text{FactorEbau} = (\frac{\text{NB}}{14}*0.3)
$$
+ **FU:** (Factor Uni) Se calcula resolviendo
$$
\text{FactorUni} = (\frac{\text{NU}}{10}*0.5)
$$

Se ha de tener en cuenta que: 
+ El cómputo se hace contra el precio de la siguiente matrícula. 
+ Para realizar los cálculos de este plan de empresa se asumirá que
	+ **El valor de PM para una primera matrícula es de 100$**
	+ **El valor de PM para otras matrículas será**
	$$
	 \text{PM}_i = \text{NM} * 100
	$$
		+ Cada año aumenta 100$

#### Estandarización de los ingresos: 
Si se realizase el cálculo de los ingresos con datos para cada asegurado podríamos obtener exactamente los ingresos generados.
Para el cómputo de indicadores como el punto muerto se complicaría inmensamente el cálculo, debido a esto se ha decidido estandarizar los ingresos generados para un número n de seguros. 

Para estandarizar los ingresos generados por un número n de seguros utilizamos los siguientes datos, tomando como referencia la escuela politécnica de la UC3M.

+ **Nota media de EBAU de los estudiantes**: *12.285* [^5]
+ **Nota media universitaria de los estudiantes (aprox):** [^6] *6.5*

Utilizando estos datos podemos calcular el **ingreso generado antes de pagos de matrícula** por los seguros. (Ingreso si ningún estudiante asegurado suspendieses su asignatura) 

Asumimos que se ofrecerán la mitad de los seguros para primeras 

En vez de dividir los n seguros generados entre aquellos que pertenecen a primera matricula de los que no (puesto a que conllevarían cálculos distintos) aproximamos un porcentaje del 50%, 50%.
De esta forma se asume que, la mitad de los seguros serán para asignaturas en primera matrícula mientras que el resto serán para matrículas superiores. 
No obstante, el cálculo del seguro para matrículas segundas/terceras/cuartas/… depende también del número de matrícula. Para real

  
$$

$$
***
[^4]: Aquí habría que añadir los gráficos creados. 
[^5]: https://www.uc3m.es/conocenos/nuestros-estudiantes
[^6]: Este dato no lo da la UC3M así que se obtiene un número aproximado, generado por los autores del plan de empresa. 