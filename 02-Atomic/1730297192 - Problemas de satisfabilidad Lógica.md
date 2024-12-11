# Problemas de satisfabilidad Lógica

> [!NOTE] Intro: 
> Existe una gran cantidad de problemas que podemos modelar directamente como problemas de [[20240523 - 122919 - Propositional logic|Propositional logic]], este tipo de problemas son aquellos con **condiciones lógicas** → “Si pasa x entonces y | Si pasa x también pasa y”
> En esta nota tocaremos formas de modelar y resovler este tipo de problemas. 

> [!example] Nomenglaturas: 
>  - **CNF** : Forma Normal Conjuntiva
>  - $\neg$ :  Negación lógica 
##  Modelo:
Un problema de satisfabilidad se define por una **fórmula lógica proposicional**: 
$$
F = p \lor q \land r \rightarrow w
$$
Como trabajar con fórmulas de cualquier tipo es dificil y requeriría diferentes approaches **siempre utilizaremos la FORMA NORMAL CONJUNTIVA (CNF)** de la fórmula. 

	$\hat{x}$
### Forma Normal Conjuntiva (CNF):
En la forma normal conjuntiva todas las cláusulas han de contener únicamente operadores de tipo OR y han de estar unidas por operadores de tipo AND:
$$F=\Lambda_{i=1}^n C_i=\Lambda_{i=1}^n\left(V_{j=1}^n l_j\right)$$
> por ejemplo: $(\neg x)$

> [!Attention] EXAM & PROBLEMS: 
> De cara al examen y problemas de examen siempre obtendremos **directamente esta forma**, no buscaremos obtener una fórmula de ningun otro tipo. 


Las *proposiciones* que usaban los antiguos filósofos griegos se llaman ahora *variables*, tal que $x_1 = \text{True} = 1$ es una variable. Las variables pueden ser de negación tal que $\overline{x_1} = \text{False} = 0$.

En lógica proposicional se tiende a usar $p \rightarrow q = p \lor q$, **disyunción de literales**.

Una fórmula normal está en **forma normal conjuntiva** si: $\land_{i=1}^N \lor_{j=1}^N l_{ij}$

Se denomina **modelo** $M$ a la definición de variables de una fórmula para que dicha fórmula se cumpla. Por ejemplo:
$$M = x_1 = \perp, x_2 = T, ..., x_n = \perp/T$$
$$donde \perp = False \space \text{y T = True}$$
>[!NOTE]
>Un literal es puro si su negación no pertenece a la fórmula (si tenemos $x_1$, no podemos tener $\overline{x_1} \space \text{en el resto de la fórmula}$)

**Tautología**: fórmula proposicional siempre cierta en cualquier asignación de sus expresiones atómicas tal que: $F = x_1 \lor \overline{x_1}$

**Contradicción**: algo que no puede ser cierto, que no tiene sentido tal que: $F = x_1 \land \overline{x_1}$. Entonces $Res(F, x_1) = \emptyset \lor \emptyset = \{\emptyset\}$    


$$Res(F, l) = \begin{cases}  F &  l \notin F \\ F \backslash l & l \in F \space \text{y l es puro} \\ (C_1 \lor C_2) & l \in F, \text{l no es puro}\end{cases}$$
$$\text{F = Formula y l = Literal}$$

Si $F = (x_1 \lor \overline{x_2} \land (\overline{x_1} \lor \overline{x_2} \lor x_3))$, entonces $Res(F, \overline{x_2}) = \emptyset$.     

**1-SAT**: problema que se resuelve en tiempo lineal $O(n)$. Este problema tiene la forma de:
$$x_1 \land \overline{x_2} \land \overline{x_1} \space ... \space \land x_n$$
**2-SAT**: problema que se resuelve en tiempo cuadrático $O(n²)$
$$(\overline{x_1} \lor x_2) \land (x_1 \lor \overline{x_3}) \space ...$$
Para resolver problemas del tipo *exponencialmente difíciles* usaremos el [[1730301854 - Algoritmo de Davis-Putnam|Algoritmo de Davis-Putnam]]

Una modificación de este algoritmo mucho más efectiva es la del [[1730301910 - Algoritmo de Davis-Putnam-Logemann-Loveland|Algoritmo de Davis-Putnam-Logemann-Loveland]].
Estos algoritmos tienen una complejidad $O(2^n)$, ya que la propia naturaleza de un problema booleano es de complejidad exponencial.

***