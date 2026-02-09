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
