[![Open in MATLAB Online](https://www.mathworks.com/images/responsive/global/open-in-matlab-online.svg)](https://matlab.mathworks.com/open/github/v1?repo=EmiCrack132/MSFP2)

# Práctica 5.4: Modelado y control del sistema cardiovascular mediante el modelo Windkessel

## Información de la estudiante
Emiliano Gómez Quiroa; 23212196 [l23212196@tijuana.tecnm.mx]

Modelado de Sistemas Fisiológicos

Ingeniería Biomédica

## Docente
Dr. Paul Antonio Valle Trujillo; paul.valle@tectijuana.edu.mx

Departamento de Ingeniería Eléctrica y Electrónica, Tecnológico Nacional de México/IT Tijuana, Blvd. Alberto Limón Padilla s/n, Tijuana, C.P. 22454, B.C., México.

## Descripción de la asignatura

El modelizado de sistemas fisiológicos es una herramienta importante en Ingeniería Biomédica, permite comprender el funcionamiento del cuerpo humano, así como diseñar y evaluar terapias y dispositivos médicos; se define como el proceso de formular modelos matemáticos o computacionales que representan el comportamiento y la interacción de los sistemas biológicos y fisiológicos. Esta asignatura pretende aportar al perfil del Ingeniero Biomédico la capacidad de realizar investigación científica en el área de Biología de Sistemas con la finalidad de dirigir y participar en equipos de trabajo interdisciplinarios en contextos nacionales e internacionales, así como de proporcionar soluciones informáticas para resolver problemas en el campo de la Ingeniería Biomédica con ética profesional; lo anterior al proporcionar al estudiante bases sólidas para modelizar sistemas y diseñar controladores para la solución de problemas en las áreas de atención médica y del sector industrial médico. La construcción de analogías entre circuitos eléctricos y sistemas fisiológicos para la formulación de modelos matemáticos y el diseño de controladores mediante la experimentación in silico brindan herramientas de gran aplicación en el quehacer profesional del Ingeniero Biomédico.

La asignatura de Modelado de Sistemas Fisiológicos forma parte del plan de estudios de la carrera en Ingeniería Biomédica con la siguiente competencia general del curso: Utiliza las propiedades de los circuitos RLC para describir la dinámica de sistemas fisiológicos, obtener modelos matemáticos y aplicar el control clásico, esto con el objetivo de integrar los principios de la Ingeniería de Control, la Electrónica Analógica y las Ciencias de la Computación con la Anatomía y Fisiología del cuerpo humano para proporcionar descripciones cuantitativas y cualitativas de sistemas fisiológicos complejos con el objetivo de modelizar, analizar, controlar, ilustrar y predecir su dinámica tanto en el corto como en el largo plazo.

## Objetivos

1. Formular el modelo matemático del sistema cardiovascular mediante el modelo Windkessel.
2. Determinar el modelo de ecuaciones diferenciales ordinarias de primer orden.
3. Calcular la función de transferencia del sistema cardiovascular.
4. Obtener las funciones de transferencia para los casos normotenso, hipotenso e hipertenso.
5. Determinar los polos de los modelos y analizar su estabilidad.
6. Analizar la respuesta de los modelos cardiovasculares en lazo abierto.
7. Comparar la respuesta de los modelos hipotenso e hipertenso con respecto al modelo normotenso.
8. Diseñar un sistema de control en lazo cerrado para reducir el error entre la respuesta normotensa y las respuestas hipotensa e hipertensa.
9. Sintonizar los parámetros del controlador para los casos hipotenso e hipertenso.
10. Obtener la respuesta en lazo abierto y en lazo cerrado mediante MATLAB/Simulink y Python.
11. Comparar los resultados obtenidos mediante las diferentes implementaciones computacionales.

## Descripción detallada del sistema

El modelo Windkessel representa de manera simplificada el comportamiento hemodinámico del sistema cardiovascular mediante una analogía con circuitos eléctricos. El modelo considera la impedancia característica Z, la inertancia L, la resistencia periférica R y la complianza arterial C para representar las propiedades dinámicas del sistema cardiovascular.

La presión arterial Pa(t) representa la entrada del modelo y el flujo sanguíneo FL(t) junto con la presión periférica Pp(t) representan las variables asociadas con el comportamiento dinámico del sistema. La salida del modelo corresponde a la presión periférica Pp(t).

Para el análisis se consideran tres condiciones fisiológicas: normotenso, hipotenso e hipertenso. Los parámetros utilizados son:

- Z = 0.010
- L = 0.001
- R = 1.000
- C_normo = 1.500
- C_hipo = 3.500
- C_hiper = 1.000

A partir de estos parámetros se obtienen las funciones de transferencia correspondientes a cada condición del sistema cardiovascular.

Para los casos hipotenso e hipertenso se implementa un sistema de control en lazo cerrado tomando como referencia la respuesta del modelo normotenso, con el objetivo de disminuir el error entre la respuesta deseada y la respuesta del sistema.

Palabras clave: Modelo Windkessel; Sistema cardiovascular; Controlador PID; Modelo matemático; Simulaciones numéricas.

## Lista de archivos incluidos en el repositorio
1. Análisis matemático.
2. Cuaderno computacional de MATLAB [.mlx y .pdf].
3. Modelo de Simulink [.slx].
4. Archivo de Python [.py].
5. Archivo con la señal de entrada utilizada en las simulaciones [.xlsx].
6. Imagen con los parámetros del controlador.
7. Figuras de las simulaciones en Python [.pdf].
8. Figuras de las simulaciones en MATLAB/Simulink [.pdf].
p. Diagrama fisiológico del sistema cardiovascular.
   

## Referencias

\[1] P. A. Valle, Syllabus para Modelado de Sistemas Fisiológicos, Tecnológico Nacional de México / Instituto Tecnológico de Tijuana, Tijuana, B.C., México, 2025. Permalink: https://biomath.xyz/course/

\[2] M. C. Khoo, Physiological Control Systems Analysis Simulation, and Estimation, 2nd ed. Piscataway, New Jersey, USA: IEEE Press, 2018.

\[3] N. S. Nise, Control Systems Engineering, 8th ed. Hoboken, New Jersey, USA: John Wiley & Sons, 2020.
