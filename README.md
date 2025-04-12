# Bring-U Project README

## Introduction

This README provides an overview of the Bring-U project, including installation instructions and a project description.

### Installed Apps

Before starting,  make sure you have installed `python`, `pip`, `django`and `git`:

In linux follow this steps:
1. `sudo apt install -y git`
2. `sudo apt install -y python3-pip`
3. `sudo su pip3 install django`
4. `python3 -m pip install --upgrade pip`
5. `sudo apt-get install libgl1-mesa-glx`
6. `sudo apt-get install tesseract-ocr`
6. Install requirements: `pip install -r requirements.txt`

For other OS look for custom tutorials

### Set project

1. Make sure to clone the repository using: `git clone https://github.com/KatherinAllin28/taller1-soft`
2. Move to root folder: `cd BRING_U_PROJECT`
3. Run migrations: `python3 manage.py makemigrations`
4. `python3 manage.py migrate`

### Deployment

To deploy the project, follow these steps:

0. Export the secret API Key from openai using: `export openAI_api_key="<your_API_key>"`
1. Collect static files: `python manage.py collectstatic`
2. Run the ASGI server: `daphne -b 0.0.0.0 -p 8000 config.asgi:application`
3. Access the application at `GCP - custom URL` or the appropriate URL.

If not pretending to use realtime communication(Chat system), just use:
- Execute in root folder: `python manage.py runserver`

If you want to use chat system:
- Execute in root folder `daphne -b 0.0.0.0 -p 8000 config.asgi:application`

## Project Description

### Overview

Bring-U is an independent web-based project aimed at enhancing the student experience on campus. It provides a platform for food deliveries from local restaurants and carpooling services. The goal is to optimize mobility, reduce waiting times for orders, and allow students to generate additional income. With Bring-U, we envision a university environment where students can meet their on-campus needs more efficiently.

### Features

- **User Access**: Any user within the campus can create an account on this platform.
- **Local Business Interaction**: Users can view local businesses and their products, place orders, and establish contact with service providers.
- **Delivery Services**: Users can take delivery requests and complete deliveries, which is a unique feature aimed at reducing wait times.
- **Additional Income**: The platform not only streamlines university life but also provides students with an opportunity to earn extra income while pursuing their academic activities.

### Integration and Compatibility

Bring-U is a standalone project and is not intended to be part of a larger system. All integrations are locally implemented. The web application is designed to run on popular web browsers such as Chrome and Brave. Additionally, it will be deployed on a chosen cloud server. If the carpooling system is included, we plan to integrate the Google Maps API for location-based features.

### User Base

There is no specific distinction among users of our app. However, we anticipate that the primary user group will be college students, typically aged between seventeen and forty. This age group is more familiar with such platforms and uses them frequently.

# TALLER 01 – GRUPOS 
## Katherin Nathalia Allin Murillo 
## Manuela Caro Villada 
## Dixon Andrés Calderón Ortega 

### Actividad 1: https://github.com/KatherinAllin28/taller1-soft 

### Actividad 2:  

#### ASPECTOS POSITIVOS: 

##### Usabilidad 
- Al estar desarrollado en Django tiene una etsructura clara y que tiene buen potencial de escalabilidad en cuanto a el desarrollo de esta. 
- Tiene archivos muy particulares de Django como views.py, models.py y templates, entre otros, lo cual facilita mucho la interpretación del proyecto en caso de cambiar de personal de desarrollo. 
- Los templates HTML permite separar todo lo que tiene que ver con frontend con la lógica del negocio. 

##### Compatibilidad 
- Django es compatible con diversas bases de datos y navegadores, entonces es un punto a favor en compatibilidad. 

##### Rendimiento 
- Está desarrollado de una forma que no hay tantos ciclos innecesarios, lo cual hace que sea más facil y rapido su procesamiento, ppor ende su rendimiento es bueno. 
- La estructura modular de Django permite de por si un manejo muy eficiente.  

##### Seguridad 
- El uso de Django ya aporta protección contra muchas vulnerabilidades comunes. 
- Por lo que se ve en views.py podemos notar que maneja rutas de autenticación, esto indica que el sistema tiene al menos una capa básica de control de acceso. 

 
#### ASPECTOS POR MEJORAR: 

##### Usabilidad 
- El README puede ser un poco más específico en cuanto a la ejecución del proyecto, su historia, su funcionalidad, las etapas de desarrollo y toda información requerida para la interpretación de este ya sea para uso del usuario dentro del servidor y de posibles desarrolladores. 
- El diseño siempre podrá ser mejor. 

##### Compatibilidad 
- Falta algún archivo guía para la configuración, si se requieren permisos o no para modificar algo, si hay superusuario, tipos tecnologías empleadas como bases de datos, etc. 

##### Rendimiento 
- Realización de pruebas de rendimiento para ver posibles fallas y poder resolverlas antes de ofrecer el producto al público. 

##### Seguridad 
- No tener visible la secret_key en el repositorio ya que este es público y eso puede afectar el proyecto si cae en manos incorrectas. 

 

#### POSIBLES INVERSIONES: 

##### Mejora de interfaz (UI/UX) 
- Invertir en un diseñador UX para hacer el producto más llamativo para sus potenciales clientes. 

##### Automatización y testing 
- Invertir en pruebas automáticas  

##### Escalabilidad en base de datos 
- Considerar PostgreSQL o servicios en la nube como AWS RDS o Google Cloud SQL.
  
### Actividad 3:  
En esta actividad se debía escoger una clase y realizar inversión de dependencia, se escogió la clase loginaccount que se encuentra dentro de "accounts/views.py" donde la clase“loginaccount” dependía directamente de la función “authenticate” de Django, lo que acoplaba fuertemente la lógica de autenticación al framework, lo cual dificultaba el cambio de una implementación futura como, por ejemplo, usar autenticación externa; debido a esto se creó dentro de la carpeta “accounts” la carpeta “services” y dentro de esta la interfaz “auth_interface.py” que define el contrato de autenticación. Luego se implementó “django_auth_service.py”, que usa authenticate internamente. Todo lo anterior para que finalmente loginaccount pasara a depender de IAuthService. 

#### Beneficios: 

- Mejor separación de responsabilidades. 
- Flexibilidad para cambiar de sistema de autenticación sin modificar la vista. 

### Actividad 4: 
Implementamos un patrón de diseño llamado Logger dentro del proyecto, el cual escogimos porque nos parece súper útil en este tipo de proyectos y sobretodo si se desea crecer con el tiempo. Este patrón de diseño es importante por varias razones y a continuación mencionaremos algunas:
#### Depuración: 
Nos ayuda a encontrar errores en el código sin tener que usar print() por todos lados.
#### Monitoreo: 
Podemos ver cómo se está comportando de la app en tiempo real o después de su ejecución, lo cual sirve mucho para analítica de datos y realizar posibles mejoras en la experiencia de uso.
#### Auditoría: 
Guarda información sobre acciones importantes, como accesos, cambios, errores críticos, etc.
#### Escalabilidad:
En caso de que el proyecto crezca, los print() ya son más complejos de usar y ejecutar, mientras que un logger permite guardar información en archivos, enviar mensajes a otros sistemas o filtrarlos por niveles.

### Actividad 5: 
