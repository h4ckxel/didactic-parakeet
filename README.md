# Proyecto de Comunicación con Personas Sordomudas

## Objetivo

Este proyecto tiene como finalidad facilitar la comunicación con personas sordomudas, permitiendo una conversación fluida y natural entre individuos con diferentes capacidades de comunicación.

## Descripción

La aplicación permitirá:
- **Reconocimiento de voz y texto:** Convertirá audios o palabras en lenguaje de señas.
- **Reconocimiento de señas:** Usará una cámara para interpretar el lenguaje de señas y convertirlo en texto o audio.

Este sistema será útil para interacciones cotidianas, como conversaciones informales, acceso a conferencias, clases y compras en establecimientos comerciales.

## Tecnología Utilizada

Para el procesamiento de imágenes y reconocimiento de señas se utilizará **YOLOv8**, una arquitectura avanzada de detección de objetos en tiempo real. Gracias a su precisión y rapidez, será posible interpretar el lenguaje de señas con alta eficiencia.

### Ejemplo de flujo de trabajo con YOLOv8

1. **Entrada:** Una cámara capta los gestos de la persona.
2. **Procesamiento:** YOLOv8 identifica la seña en tiempo real.
3. **Salida:** Se genera un texto o un audio con la interpretación de la seña.

<div align="center">
  
## Ejemplo de interfaz de usuario


<img src="https://miro.medium.com/v2/resize:fit:600/1*e_7bN4nfREd0KGai-eQzGQ.gif" width=40%>

##### La imagen muestra cómo el sistema puede detectar y reconocer diferentes señas en tiempo real.

</div>

## Aplicaciones y Beneficios

- Facilita la comunicación entre personas sordomudas y oyentes.
- Mejora la accesibilidad en distintos entornos como educación, comercio y salud.
- Permite una integración más inclusiva en la sociedad.

## Próximos Pasos

- Desarrollo del modelo de reconocimiento basado en YOLOv8.
- Entrenamiento del modelo con un dataset específico de lenguaje de señas.
- Implementación de una interfaz amigable para los usuarios.

📌 **Este proyecto busca eliminar barreras y acercar la tecnología a la accesibilidad para todos.**

