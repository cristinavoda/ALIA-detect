import gradio as gr
from pathlib import Path
from brand_guard import brand_guard, summarize
from reports.reporter import export_report
from datetime import datetime

# Carpeta para reportes
REPORTS_DIR = Path("reports")
REPORTS_DIR.mkdir(exist_ok=True)


def analyze_prompt(prompt: str, category: str):
    # Detecta riesgos
    findings = brand_guard(prompt)
    summary = summarize(findings)
    
    # Genera reporte JSON
    timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    report_filename = export_report(
        category=category,
        prompts=[prompt],
        detections={prompt: {"findings": findings, "summary": summary}}
    )
    
    # Mensaje para el usuario
    output_text = f"🧠 Prompt: {prompt}\n\n"
    if findings:
        output_text += "⚠️ Riesgos detectados:\n"
        for f in findings:
            output_text += f"- Categoría: {f['category']} | Trigger: '{f['trigger']}' | Tipo: {f['type']} | Severidad: {f.get('severity', 'n/a')}\n"
    else:
        output_text += "✅ No se detectan riesgos aparentes.\n"
    
    output_text += f"\n📄 Reporte generado: {report_filename}\n"
    output_text += f"💡 Summary: {summary}\n"
    
    return output_text


# Interfaz Gradio
with gr.Blocks() as demo:
    gr.Markdown("# ALIA-detect 🚨 Human-in-the-loop Risk Detector")
    prompt_input = gr.Textbox(label="Escribe tu prompt aquí:", lines=3, placeholder="Introduce el texto a evaluar...")
    category_input = gr.Dropdown(
        label="Selecciona la categoría",
        choices=["specialized_advice", "gender_bias"],
        value="specialized_advice"
    )
    analyze_btn = gr.Button("Analizar")
    output_box = gr.Textbox(label="Resultados", lines=15)

    analyze_btn.click(
        analyze_prompt,
        inputs=[prompt_input, category_input],
        outputs=output_box
    )

demo.launch()