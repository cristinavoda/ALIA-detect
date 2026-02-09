from brand_guard import BrandGuard
from reporter import export_report

# 1️⃣ Cargar prompts desde archivo
def load_prompts(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

# 2️⃣ Main
if __name__ == "__main__":
    category = "specialized_advice"
    prompt_file = "specialized_advice.txt"

    prompts = load_prompts(prompt_file)

    guard = BrandGuard()
    detections = {}

    for prompt in prompts:
        flags = guard.check(prompt)
        detections[prompt] = flags
        print(f"\n🧠 Prompt: {prompt}")
        print(f"🚨 Flags: {flags}")

    report_file = export_report(
        category=category,
        prompts=prompts,
        detections=detections
    )

    print(f"\n📄 Reporte generado: {report_file}")
from pathlib import Path


PROMPTS_DIR = Path("prompts")


def load_prompts(file_path):
    """Carga prompts desde un archivo .txt"""
    with open(file_path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]


def analyze_prompts(category_name, prompts):
    """Analiza una lista de prompts y muestra un mini-reporte"""
    print(f"\n=== Análisis categoría: {category_name} ===\n")

    for idx, prompt in enumerate(prompts, start=1):
        findings = brand_guard(prompt)

        print(f"Prompt {idx}:")
        print(f"  \"{prompt}\"")

        if findings:
            print("  ⚠️ Riesgos detectados:")
            for f in findings:
                print(
                    f"   - Categoría: {f['category']} | "
                    f"Trigger: '{f['trigger']}' | "
                    f"Tipo: {f['type']}"
                )
        else:
            print("  ✅ No se detectaron riesgos")

        print("-" * 60)

category = "specialized_advice"

detections = {}

for prompt in prompts:
    flags = brand_guard.check(prompt)
    detections[prompt] = flags

report_file = export_report(
    category=category,
    prompts=prompts,
    detections=detections
)

print(f"\n📄 Reporte generado: {report_file}")

def main():
    gender_file = PROMPTS_DIR / "gender_bias.txt"
    advice_file = PROMPTS_DIR / "specialized_advice.txt"

    if gender_file.exists():
        gender_prompts = load_prompts(gender_file)
        analyze_prompts("Sesgos de género", gender_prompts)

    if advice_file.exists():
        advice_prompts = load_prompts(advice_file)
        analyze_prompts("Asesoramiento especializado", advice_prompts)


if __name__ == "__main__":
    main()