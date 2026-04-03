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
