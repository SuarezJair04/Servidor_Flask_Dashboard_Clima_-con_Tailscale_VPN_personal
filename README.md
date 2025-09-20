# Servidor_Flask_Dashboard_Clima_con_Tailscale_VPN_personal
Actividad Sistemas Programables, creación de una interfaz de clima mediante un servidor Flask

**Autor**: Suárez Castro Jair Alberto - 22211663  
**Institución**: Instituto Tecnológico de Tijuana  
**Materia**: Sistemas Programables  
**Fecha**: 19/sep/2025  

---

# Dashboard del Clima con Flask y Tailscale

Consiste en un servidor web sencillo implementado con **Flask** en Python que consulta datos de la API de **OpenWeatherMap** y los muestra en una interfaz web estilo dashboard.  
La aplicación está diseñada para ejecutarse en un teléfono móvil a través de **Termux** y ser accesible de manera segura mediante la red privada virtual **Tailscale**.

---

## Objetivo del proyecto

El objetivo principal es crear un sistema en el que un dispositivo móvil pueda actuar como servidor de aplicaciones.  
Este servidor obtiene información climática en tiempo real y la presenta de manera visual. El acceso al dashboard se realiza a través de Tailscale, lo cual garantiza seguridad sin necesidad de abrir puertos ni depender de direcciones IP públicas.

---

## Contenido

- **Servidor web**: Construido con Flask.  
- **Interfaz visual**: Presentación de temperatura, condiciones y ciudad en una tarjeta con diseño estilizado.
- **Datos actualizados**: Conexión directa a la API de OpenWeatherMap para obtener la información más reciente.
- **Seguridad**: Integración con Tailscale para conectarse desde otros dispositivos sin complicaciones de red.  
- **Portabilidad**: Preparado para ejecutarse en Termux sobre Android o iOS.  
 
---

## Herramientas que se utilizaron

| Componente       | Software/herramientas                |
|------------------|---------------------------|
| Backend          | Python 3, Flask           |
| Frontend         | HTML y CSS                |
| Datos            | API de OpenWeatherMap     |
| Dispositivo host | Termux (Android/iOS)      |
| Red privada      | Tailscale VPN             |

---

## Pasos de configuración

### 1. Clave de acceso a la API
Registrar una cuenta en [OpenWeatherMap](https://openweathermap.org/api) para obtener una clave gratuita.  
Colocar dicha clave en el archivo `app.py` dentro de la variable definida para el API Key.

### 2. Preparación de la red privada
Instalar y configurar **Tailscale** en el dispositivo servidor (el teléfono con Termux) y en los equipos clientes que accederán al dashboard.

### 3. Ejecución del servidor
Desde Termux, iniciar el proyecto ejecutando:

```bash
python app.py
```


Esto pondrá en marcha el servidor de Flask en el puerto definido.

### 4. Conexión al dashboard

Abrir un navegador en otro dispositivo conectado a **Tailscale** e ingresar la dirección IP asignada al teléfono, seguida del puerto `5000`.

---
## Evidencia
[Video comandos y creación del archivo .py en Termiux](https://asciinema.org/a/nXMYW4K2N4u3iT1L3CNsLCmKa)

![Video utilizando tailscale](https://github.com/user-attachments/assets/ba8d7056-8974-48a4-ac8f-2f705150fab5)


### Clima Tijuana
![Image](https://github.com/user-attachments/assets/1cc60d98-db24-42ef-9014-ca334631bee7)

### Climas de distintas ciudades del mundo
![Image](https://github.com/user-attachments/assets/26cc68b8-be48-4191-a0f5-613e9b1e7a35)

![Image](https://github.com/user-attachments/assets/78256d3c-2759-434d-8fb6-2857e5821046)

![Image](https://github.com/user-attachments/assets/5b2b40a6-9e3f-4ccb-931a-3f3933045e1e)


