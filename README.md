# FitManager: Sistema Inteligente para la Gestión Administrativa de Gimnasios

## Descripción del proyecto

FitManager es un sistema desarrollado en Python para facilitar la gestión administrativa de gimnasios pequeños o medianos.  
El sistema permite registrar clientes, administrar membresías, controlar pagos y generar reportes básicos mediante una aplicación de consola organizada y funcional.

Este proyecto forma parte del Proyecto Integrador de la asignatura de Lógica de Programación y busca evidenciar el impacto de las nuevas tecnologías en la sociedad mediante el desarrollo de una solución informática aplicada a una necesidad real.

---

## Problema identificado

Muchos gimnasios administran la información de sus clientes, pagos y membresías de forma manual, utilizando cuadernos, hojas de cálculo o registros poco organizados. Esto puede provocar pérdida de información, errores en el control de pagos y dificultad para conocer el estado de las membresías.

FitManager busca resolver esta problemática mediante un sistema que centraliza la información y permite gestionar los datos de forma más rápida, clara y ordenada.

---

## Objetivo del sistema

Desarrollar un sistema de gestión para gimnasios que permita administrar clientes, membresías y pagos mediante una aplicación desarrollada en Python, aplicando los conocimientos adquiridos durante la asignatura de Lógica de Programación.

---

## Funcionalidades principales

- Registrar clientes.
- Mostrar clientes registrados.
- Buscar clientes por cédula.
- Editar información de clientes.
- Eliminar clientes.
- Registrar membresías.
- Renovar membresías.
- Consultar membresías registradas.
- Registrar pagos.
- Consultar historial de pagos.
- Generar reportes básicos.
- Guardar información en archivos JSON.

---

## Tecnologías utilizadas

- Python 3.13
- JSON
- Visual Studio Code
- GitHub

---

## Contenidos aplicados de Lógica de Programación

Durante el desarrollo del sistema se aplicaron los siguientes contenidos:

- Variables.
- Condicionales.
- Bucles.
- Funciones.
- Listas.
- Diccionarios.
- Manejo de archivos.
- Modularización del código.
- Control de versiones con GitHub.

---

## Estructura del proyecto

```text
FitManager-Gestion-Gimnasios/
│
├── main.py
├── menu.py
├── clientes.py
├── membresias.py
├── pagos.py
├── reportes.py
├── almacenamiento.py
├── requirements.txt
│
├── datos/
│   ├── clientes.json
│   └── pagos.json
│
└── diagramas/
    ├── casos_uso_fitmanager.png
    ├── flujo_general_fitmanager.png
    └── arquitectura_fitmanager.png

## Descripción de archivos

| Archivo | Descripción |
|---|---|
| `main.py` | Archivo principal que inicia la ejecución del sistema FitManager. |
| `menu.py` | Contiene el menú principal y controla la navegación entre las opciones del sistema. |
| `clientes.py` | Permite registrar, mostrar, buscar, editar y eliminar clientes. |
| `membresias.py` | Gestiona el registro, renovación y consulta de membresías. |
| `pagos.py` | Permite registrar pagos y consultar el historial de pagos realizados. |
| `reportes.py` | Genera reportes básicos sobre clientes, pagos y estado del sistema. |
| `almacenamiento.py` | Se encarga de cargar y guardar información en archivos JSON. |
| `requirements.txt` | Indica que el sistema no requiere librerías externas. |
| `datos/clientes.json` | Archivo donde se almacena la información de los clientes registrados. |
| `datos/pagos.json` | Archivo donde se almacena el historial de pagos realizados. |

---

## Instalación y ejecución

### 1. Clonar el repositorio

```bash
git clone URL_DEL_REPOSITORIO
```

### 2. Entrar a la carpeta del proyecto

```bash
cd FitManager-Gestion-Gimnasios
```

### 3. Ejecutar el sistema

```bash
python main.py
```

También se puede ejecutar con:

```bash
py main.py
```

---

## Requisitos

No se requieren librerías externas.

El sistema utiliza únicamente librerías estándar de Python:

- `json`
- `os`
- `datetime`

---

## Diagramas del sistema

El repositorio incluye los siguientes diagramas:

- Diagrama de casos de uso.
- Diagrama de flujo general.
- Diagrama de arquitectura del sistema.

Estos diagramas permiten representar la funcionalidad, el flujo principal y la estructura modular del sistema.

---

## Demostración del sistema

El funcionamiento del sistema permite demostrar las siguientes acciones:

1. Registro de un cliente.
2. Consulta de clientes registrados.
3. Búsqueda de cliente por cédula.
4. Edición de información de cliente.
5. Registro de membresía.
6. Registro de pago.
7. Consulta del historial de pagos.
8. Generación de reportes básicos.

---

## Impacto de la tecnología

FitManager demuestra cómo una solución informática puede mejorar la administración de un gimnasio mediante la digitalización de procesos.

El uso de tecnología permite reducir errores manuales, mejorar el acceso a la información, optimizar la gestión de clientes, controlar pagos y facilitar la administración de membresías.

Este proyecto evidencia que la programación puede aplicarse para resolver problemas reales mediante herramientas accesibles y funcionales.

---

## Integrante

- Wilson Mites

---

## Asignatura

Lógica de Programación

---

## Fecha

28 de Junio del 2026
