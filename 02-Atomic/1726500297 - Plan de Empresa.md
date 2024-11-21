---
aliases:
  - Plan de Empresa
  - Practica - Plan de Empresa
tags:
  - Empresa
References: 
cssclasses:
---
# Plan de Empresa


> [!NOTE] Intro: 
> Esta nota recoge toda la información, análisis y decisiones tomadas para realizar el plan de empresa, trabajo final de la asignatura de Empresa de la UC3M 
+ Se pueden revisar los consejos y directrices dadas en clase en la sección de apuntes[^1]
+ Se pueden encontrar dudas en el pie de página, cada duda numerada. 

Se presenta a continuación un MOC con cada una de las partes realizadas. 

**Notas sobre la escritura:**
+ Se escribé en futuro, presentando la empresa como una posibilidad futura: 
  > La empresa se **creará**, se **financiará**, etc. 
  
+ Tipo de explicación[^2]
## 1. Inventar una empresa:

> [!NOTE] Requisito: 
> Describir el campo de actividad de la empresa (producto o servicio). 
> 

### 1.1 Descripción del servicio
El campo de actividad de la empresa propuesta se encuentra dentro del mercado de seguros. La empresa **ofrece un seguro de matrícula para estudiantes universitarios**[^4]
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


## 3. Definición de la empresa
### 3.1 Forma jurídica y económica 
La empresa propuesta es **Try Again Seguros**. Una aseguradora para matrículas universitarias. 
> “Paga una vez, inténtalo dos veces”

La empresa se posiciona dentro del sector terciario de servicios como una microempresa que actua en un ámbito de monomercado nacional. 
Esto se debe a que: 
+ La cantidad de trabajadores de la empresa será menor que 10 y facturará una cantidad menor que 2M anualmente. 
+ La empresa actua únicamente en el mercado de seguros español. 

Por último, la empresa se creará como  sociedad de capitales, una **sociedad de responsabilidad limitada** que se creará con dos socios. 
Se elegirá esta forma debido a que:
+ ==El capital desembolsado incialmente será de X==  → @Tomas
+ Al elegir esta forma jurídica la empresa se beneficia de que los socios puedan realizar prestaciones accesorias como trabajo [^3]
### 3.2 Objetivos de la empresa: 
Los objetivos de la empresa serán:
1. **Maximizar el valor de la empresa**
2. **Proporcionar seguridad económica a los estudiantes universitarios**


***
[^1]: **Apuntes:**
+ Poner como objetivo de empresa: **Maximizar el valor de la empresa**
+ Se aconseja (aunq no se requiere) que se utilice el [[1727105227 - Modelos de negocio de la empresa#Modelo canvas:|Modelo canvas]]]
[^2]: #Duda: Se busca que redactemos las características y teoría de cada parte realizada o que directamente argumentemos las decisiones asuminedo que la teoría ya es conocida? 
[^3]: #Duda: En una SA los socios no podrían realizar trabajo? Los socios no son los que tienen las acciones? Serían entonces los socios los organizativos y los accionistas otros diferentes?
[^4]: Aquí habría que añadir los gráficos creados. 