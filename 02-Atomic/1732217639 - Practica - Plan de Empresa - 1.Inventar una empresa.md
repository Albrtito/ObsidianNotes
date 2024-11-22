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
\text{Precio} = \text{PM} - DE
$$
Donde: 

+ **PM**: (Precio Matrícula) Es el precio de la siguiente (segunda)matrícula de la asignatura. 
+ **DE:** (Descuento Ebau) Es el precio que se descuenta debido a la nota de ebau
$$
DE =  (\frac{\text{NB}}{14})*0.5*PM
$$
+ **NB**: (Nota Ebau) Nota de ebau sobre 14

**En caso de que el estudiante no sea de nuevo acceso a la universidad(cualquiera menos el primer año)**
+ Se utiliza **la nota de ebau,la nota media universitaria y el número de matrícula**
+ Se descontará un máximo del 80% subdividido de la siguiente forma: 
	+ 50% Dependiente de la nota media universitaria 
	+ 30% Dependiente de la nota de ebau
+ Se subirá el precio un 10% sobre el precio de la matrícula por cada matrícula extra: 
  > Entonces para la segunda matrícula se sube un 10%, para la tercera un 20%…

El precio se calcula resolviendo:
$$
\text{Precio} = PM - DT + PE 
$$
Donde:
+ **PM:** (Precio matrícula)
+ **NB:** (Nota Ebau) Nota de ebau sobre 14
+ **NU:**( Nota Universidad) Nota media de la universidad sobre 10
+ **NM:** (Número matrícula) Con rango empezando en 1
+ **DT:** Descuento total, calculado como: 
		$$
		DT = \text{DE} + \text{DN}
		$$
	Donde: 
	+ **DE:** (Descuento Ebau) Se calcula igual que en el primer caso solo que con un porcentaje del 30%
		
$$
DE =  (\frac{\text{NB}}{14})*0.3*PM
$$
	+ **DN:** (Descuento Nota) Calculado como
	  $$
	  DN = \frac{NU}{10} * 0.5 * PM
	  $$
+ **PE:** (Precio Extra) Se calcula el porcentaje extra por matrícula: 
$$
PE = PM *0.1 * (NM-1)
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

Realizaremos la estandarización en dos pasos.
1. Primero se obtendrán los beneficios calculados antes del pago de matrículas aseguradas 
2. A continuación se analizará el porcentaje de matrículas que el seguro deberá de pagar (en caso de que el estudiante asegurado suspendiese la asignatura) y el coste que ello supodría. 

**NOTA:** 
+ Para estos cálculos asumimos que el precio de la primera matrícula es de 100 y se duplica posteriormente por matrícula
##### Ingresoss generados antes del pago de matrículas:
Para estandarizar los ingresos generados por un número n de seguros antes del pago de matrículas utilizamos los siguientes datos, tomando como referencia la escuela politécnica de la UC3M.

+ **Nota media de EBAU de los estudiantes**: *12.285* [^5]
+ **Nota media universitaria de los estudiantes (aprox):** [^6] *6.5*

Utilizando estos datos podemos calcular el **ingreso generado antes de pagos de matrícula** por los seguros. (Ingreso si ningún estudiante asegurado suspendieses su asignatura) 

Asumimos que se ofrecerán la mitad de los seguros para primeras matrículas y la otra mitad para matrículas posteriores. 

No obstante, el cálculo del seguro para matrículas segundas/terceras/cuartas/… depende también del número de matrícula. Para estandarizarlo dividimos el 50% de la siguiente forma: 
+ 25% : Segundas matrículas 
+ 20% : Terceras matrículas 
+ 5% : Cuartas matrículas

Finalmente podemos obtener los ingresos generados antes del pago de matrículas por un número n de seguros : 
$$
\text{Ingresos} = (0.5n*\text{IP}) + (0.25n * \text{IS}) + (0.2*\text{IT})+ (0.2*\text{IC})
$$
**Donde**: 
Tenemos en cuenta los descuentos de la siguiente forma:
+ **DE:** El descuento ebau, utilizando la nota media(12.285) de EBAU toma un valor de 
  → $DE = (0.13*200) = 26$ : En caso de ser una primera matrícula
  →  $DE= (0.0.78*PM)$ : En caso de ser una matrícula posterior a la primera
+ **DU:** El descuento uni, utilizando la nota media (6.5) toma un valor de →  $DU = (0.325*PM)$
  
Calculamos los ingresos para cada tipo de matrícula:
+ **IP:** Ingreso por **un seguro de Primera matrícula** donde: 
	+ $DE = 26$
	
$$
IP  = 200 - 26 = 174
$$
+ **IS:** Ingreso por **un seguro de Segunda Matrícula** donde:
	+ $DE = 0.078 * 300 = 23.4$
	+ $DU =0.325*300 =  97.5$
	+ $PE = 300 * 0.1 = 30$
$$
IS = 300 - 23.4 - 97.5 + 30 = 209.1
$$
+ **IT:** Ingreso por **un seguro de tercera matrícula** donde:
	+ $DE = 0.078 * 400 = 31.2$
	+ $DU =0.325*400= 130$
	+ $PE = 400 * 0.1 = 40$
$$
IS = 400 - 31.2 - 130 + 40 =  278.8
$$
  
+ **IC:** Ingreso por **un seguro de cuarta matrícula** donde:
	+ $DE = 0.078 * 500 = 39$
	+ $DU =0.325*500= 162,5$
	+ $PE = 500 * 0.1 = 50$
$$
IS = 500-39-162,5+50 = 348,5
$$

Obtenemos entonces el **cálculo final de los ingresos como:** 
$$
\text{Ingresos} = (0.5n*174) + (0.25n * 209.1) + (0.2n*278.8)+ (0.05n*348.5)
$$
Que se puede simplificar a: 
$$
Ingresos = 212,46 \cdot n
$$
+ Esto quiere decir que **generalizando, la empresa ganaría 212,46$ por cada seguro vendido**

+ Observamos que,por ejemplo, por un número de seguros igual a 100 se obtendrá un beneficio de: [^7]
$$
Ingresos_{100} = 21 246
$$

##### Perdidas estimadas: 
+ Esto para mañana 

***
[^4]: Aquí habría que añadir los gráficos creados. 
[^5]: https://www.uc3m.es/conocenos/nuestros-estudiantes
[^6]: Este dato no lo da la UC3M así que se obtiene un número aproximado, generado por los autores del plan de empresa. 
[^7]: #Duda Todas las funciones y programas utilizados merece la pena añadirlos al plan de emrpesa de alguna forma? Se calificarían?