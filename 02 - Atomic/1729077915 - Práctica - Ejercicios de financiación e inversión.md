---
aliases:
  - Práctica - Ejercicios de financiación e inversión
tags:
  - Empresa
References: 
cssclasses:
---
# Práctica - Ejercicios de financiación e inversión

## Ejercicio 6:

> [!NOTE] Enunciado: 
>  La apertura de un servicio de autobuses desde Lorca al aeropuerto de Madrid, requiere la adquisición de un mínimo de 2 autobuses que, totalmente equipados, suponen una inversión total de 1.000.000€, con una vida útil de 4 años. Cada autobús cuenta con 60 plazas de viajeros, con un precio por trayecto de 25€. El coste variable por trayecto es de 500€. Cada autobús realizará al día dos trayectos, uno de ida y uno de vuelta, todos los días del año.
>  
 La ocupación media esperada es del 50% el primer año, 60% el segundo, 70% el tercero y del 80% el cuarto año.
 
**Nota:** Considerar que un año tiene 360 días
+ Inversión inicial(A): 1.000.000u
+ 4 años para recuperar la inversión
+ 60 plazas
+ 25u/viajero
+ Coste variable x Trayecto: 500u
+ Trayectos de cada autobús x año: 2x360
	+ Gastos variables anuales x autobús: 360.000
+ Ocupación esperada por años para un autobus:
	+ 1º: 30 plazas por viaje: Ingresos: 30x2x360x25 = 540.000
	+ 2º: 36 plazas por viaje: Ingresos: 648.000
	+ 3º: 42 plazas por viaje: Ingresos: 756.000
	+ 3º: 48 plazas por viaje: Ingresos: 864.000

1. **¿Cuál es el Valor Actual Neto de la línea Lorca-Aeropuerto Madrid, para una previsión de coste del dinero del 10%?**
   $$
   \begin{gather}
   VAN = -1.000.000 + \frac{(+2(-360.000 + 540.000))}{(1+.1)^1} \\+ \frac{(2(-360.000 + 648.000))}{(1+.1)^2}+  \frac{(2(-360.000 + 756.000))}{(1+.1)^3} \\+ \frac{(2(-360.000 + 864.000))}{(1+.1)^4} = 1.086.824,67
   \end{gather}
   $$
   
2. **Espera recuperar el dinero invertido en un plazo máximo de 3 años; de acuerdo a las previsiones. ¿Lo conseguirá? (cuantifique la respuesta).**
   Podemos utilizar el análisis del VAN anterior pero solo con tres años:
   $$
   \begin{gather}
VAN_3 = -1.000.000 + \frac{(+2(-360.000 + 540.000))}{(1+.1)^1} + \\\frac{(2(-360.000 + 648.000))}{(1+.1)^2}+  \frac{(2(-360.000 + 756.000))}{(1+.1)^3} = 398.347,1074
\end{gather}
   
   $$
   Vemos que el valor del VAN es mayor que cero, o que significa que la inversión no solo se recupera sino que hay ganancias. 

## Ejercicio 7:

> [!NOTE] Enunciado
> [Contents](<En un proyecto de inversión que se pretende realizar en cuatro años para la compra
de maquinaria, se dispone de la siguiente información:
>- Inversión inicial de 125.000€. → **A**
>- Los ingresos netos generados por la producción de la maquinaria durante esoscuatro años, son respectivamente 45.000 €, 55.000 €, 40.000 € y 35.000 €. → **$C_i$**
>- Se establece un Contrato para el mantenimiento de la maquinaria, por importe de
>3.000 € /año. Adicionalmente, en el segundo año, la maquinaria sufre una avería
>que no está contemplada en el contrato de mantenimiento y la reparación tiene un
>coste adicional de 2.000 €. → **Costes fijos y variables** → $P_i$
>- La maquinaria al final de los 4 años de su vida útil se vende para desguace por
>10.000 €.
>- La tasa descuento anual es del 10%.>)


1. **Calcular el VAN del proyecto:**
   $$
   \begin{gather}
VAN = -125000 + \frac{(+45000-3000)}{(1+.1)^1} + \\\frac{(+55000-3000-2000)}{(1+.1)^2}+  \frac{(+40000 -3000)}{(1+.1)^3} + \frac{(+35000-3000+10000)}{(1+.1)^4} = 10989.34
\end{gather}
$$
2. **Razonar como afectarían los siguientes hechos:**
	1. El TIR sería mayor al 10% debido a que el valor del VAN para un 10% es mayor que 0. Si queremos que sea 0 debemos de tener un ratio de más alto para que al dividir el VAN sea menor. 
	2. –
	3. $Payback_3. = -125000 + 45000 + 55000 + 40000 - 3000\cdot 3 - 2000 = 4000$ => El payback en 3 años se cumpliría
	4. –

## Ejercicio 8:

> [!NOTE]  Enunciado:
> ¿Cuál es la máxima cantidad que deberíamos invertir en un proyecto en el momento 0 si los flujos de entrada de tesorería estimados son de 30.000 euros al año durante 4 años a partir del año 1? Se ha estimado que la tasa de rentabilidad interna es del 8%. 

Calculamos usando el VAN del proyecto e igualándolo a 0: 
$$\begin{gather}
0 = -I + \frac{30000}{(1+0.8)}+\frac{30000}{(1+0.8)^2}+\frac{30000}{(1+0.8)^3} \Rightarrow I =  + \frac{30000}{(1+0.8)}+\frac{30000}{(1+0.8)^2}+\frac{30000}{(1+0.8)^3} = 31069.96
\end{gather}
$$
+ Se podrán invertir un máximo de 31069.96
**NOTA:** Hay que tener en cuenta que es la inversión máxima pero para obtener beneficios se ha de invertir menos.

## Ejercicio 9:

> [!NOTE] Enunciado:
>  Dados los siguientes flujos de caja con k = 13%:
>  **A:** 
>  + 0 → -1000 
>  + 1 → 1000
>  + 2 → 1000
>  
>  **B:**
>  + 0 → -100000 
>  + 1 → 65000
>  + 2 → 65000

1. **Cálculo y comentario del cálculo de VAN y TIR**
   $$
   \begin{gather}
VAN_A = -1000 + \frac{1000}{(1+r)} +\frac{1000}{(1+r)^2}\\\\
VAN_B = -100000 + \frac{65000}{(1+r)}+\frac{65000}{(1+r)^2}
\end{gather}
$$
Obtenemos valores para el TIR:
$$
\begin{gather}
-1000 + \frac{1000}{(1+r_A)} +\frac{1000}{(1+r_A)^2} = 0\\\\
-100000 + \frac{65000}{(1+r_B)}+\frac{65000}{(1+r_B)^2} = 0\\\\
r_A = 
\end{gather}

***
 