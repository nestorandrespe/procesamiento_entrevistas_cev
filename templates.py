departamentos = """
Amazonas
Antioquia
Arauca
Atlántico
Bolívar
Boyacá
Caldas
Caquetá
Casanare
Cauca
Cesar
Chocó
Córdoba
Cundinamarca
Guainía
Guaviare
Huila
La Guajira
Magdalena
Meta
Nariño
Norte de Santander
Putumayo
Quindío
Risaralda
San Andrés y Providencia
Santander
Sucre
Tolima
Valle del Cauca
Vaupés
Vichada
"""

instrucciones = """
Instruccion: Desanonimizar el texto. Los campos anonimizados que debes reemplazar estan marcados con "----". El resto del texto debe mantenerse intacto. Los campos anonimizados son o lugares que deben ser reemplazados por lugares de Colombia, o nombres de personas que deben ser reemplazados por nombres de personas colombianas. Intentar mantener coherencia en el texto y los nombres de los lugares. El texto desanonimizado no debe contener "----".

Ejemplo:
ENT: ¿Qué pasó con el novio de ------------- TEST: ¡Ay, mi novio! Me llamó ahora, porque yo lo había llamado [risas]. Mi novio vive en ----- Él es un fotógrafo en este momento. Es un fotógrafo que retrata mucho las, pues, el festival del Petronio. No, pues él se fue de --------- se fue a estudiar a, primero fue para ---------- después fue para -----y allá fue que estudió pero no acabó y se dedicó a la fotografía y le va muy bien. Está muy bien, es muy conocido. Tiene un ojo muy bueno para la fotografía. Y hablamos de vez en cuando. Hablamos y nos damos bien. Nosotros es como que hubiéramos quedado unidos por algo así como un hilo invisible. Es lo que le estaba diciendo a ENT.

ENT: ¿Qué pasó con el novio de Josefina? TEST: ¡Ay, mi novio! Me llamó ahora, porque yo lo había llamado [risas]. Mi novio vive en Meta Él es un fotógrafo en este momento. Es un fotógrafo que retrata mucho las, pues, el festival del Petronio. No, pues él se fue de Sucre se fue a estudiar a, primero fue para Antioquia después fue para Santander y allá fue que estudió pero no acabó y se dedicó a la fotografía y le va muy bien. Está muy bien, es muy conocido. Tiene un ojo muy bueno para la fotografía. Y hablamos de vez en cuando. Hablamos y nos damos bien. Nosotros es como que hubiéramos quedado unidos por algo así como un hilo invisible. Es lo que le estaba diciendo a ENT.

Texto a desanonimizar:
{}

Respuesta:
"""