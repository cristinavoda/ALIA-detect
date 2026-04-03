# ALIA-detect – Human-in-the-loop Risk Detector

**Autor:** Cristina Voda  
**Proyecto:** Demo de detección de riesgos en prompts con Python + Gradio  

---

## Descripción

ALIA-detect es una aplicación interactiva que permite detectar riesgos en prompts de texto, tales como:

- Discurso de odio
- Sesgos de género
- Asesoramiento especializado (legal, médico, financiero)
- Lenguaje ofensivo
- Contenido sexual explícito

Los resultados se muestran con **colores según severidad** y se pueden exportar en **reportes JSON**.

---

## Demo Interactivo

Ejecuta el demo con:

```bash
python app.py.
Luego abre el enlace que Gradio genera en tu navegador.

Funcionalidades
Interfaz limpia en español
Botones predefinidos para pruebas rápidas
Resúmenes de riesgo en lenguaje natural
Colores visuales según severidad (verde, naranja, rojo)
Reportes JSON automáticos
Captura

Instalación
Clona el repositorio:
git clone https://github.com/cristinavoda/ALIA-detect.git
cd ALIA-detect
Crea un entorno virtual (opcional):
python -m venv venv
.\venv\Scripts\activate
Instala dependencias:
pip install -r requirements.txt
Ejecuta el demo:
python app.py
Licencia

GPL-3.0 License

Contacto

Cristina Voda – LinkedIn


---

## 3️⃣ Archivos importantes

- `requirements.txt`:

```text
gradio
pathlib

Agrega cualquier otra librería que uses (re, datetime, etc. si no son estándar).

.gitignore:
venv/
__pycache__/
reports/
*.pyc
=======
# ALIA-detect

**ALIA-detect** es una herramienta experimental de detección de riesgos de alineamiento en modelos de lenguaje,
diseñada específicamente para el desafío **ALIA-40B Instruido**.

El proyecto explora cómo ciertos *prompts cuidadosamente formulados* pueden inducir respuestas problemáticas
relacionadas con **asesoramiento especializado** y **sesgos de género**, facilitando su análisis y reporte.

---

## Objetivo

Ayudar a identificar comportamientos no alineados en LLMs mediante:

- generación sistemática de prompts de riesgo
- detección basada en reglas y palabras clave (human-in-the-loop)
- resultados explicables y reproducibles

---

## Categorías abordadas

Actualmente el proyecto se centra en:

- **Asesoramiento especializado**
  - consejos médicos, legales o financieros sin disclaimers
  - autoridad indebida o respuestas prescriptivas
- **Sesgos de género**
  - estereotipos
  - lenguaje discriminatorio
  - generalizaciones injustificadas

El diseño permite extender fácilmente a otras categorías del desafío ALIA.

---

## Estructura del proyecto

ALIA-detect/
│
├── prompts/
│ ├── specialized_advice.txt
│ └── gender_bias.txt
│
├── brand_guard.py
├── examples.py
├── requirements.txt
└── README.md

---

## Instalación

```bash
git clone https://github.com/cristinavoda/ALIA-detect.git
cd ALIA-detect
python -m venv venv
venv\Scripts\activate
source venv/bin/activate
pip install -r requirements.txt
python examples.py

 Autora

Cristina Voda
>>>>>>> 9044519352f8dcf1e78d107064162a90e0e1fb5c
