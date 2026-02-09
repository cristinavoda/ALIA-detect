import json
from datetime import datetime
from pathlib import Path


def export_report(category, prompts, detections):
    """
    Exporta un reporte JSON con prompts analizados y detecciones.
    """
    timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")

    report = {
        "project": "ALIA-detect",
        "category": category,
        "timestamp_utc": timestamp,
        "total_prompts": len(prompts),
        "detections": []
    }

    for prompt, flags in detections.items():
        report["detections"].append({
            "prompt": prompt,
            "flags": flags,
            "risk_detected": len(flags) > 0
        })

    Path("reports").mkdir(exist_ok=True)

    filename = f"reports/{category}_report_{timestamp}.json"
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)

    return filename