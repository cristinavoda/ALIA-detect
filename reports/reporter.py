"""
Copyright (C) 2026 Cristina Voda
This file is part of ALIA-detect.

Licensed under the GNU General Public License v3.0 (GPL-3.0)
You may obtain a copy of the License at https://www.gnu.org/licenses/gpl-3.0.txt
"""
import json
from datetime import datetime
from pathlib import Path


def export_report(category: str, prompts: list, detections: dict) -> str:
    """
    Exporta un reporte JSON con los resultados del análisis.
    """

    timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")

    report = {
        "project": "ALIA-detect",
        "category": category,
        "timestamp_utc": timestamp,
        "total_prompts": len(prompts),
        "results": []
    }

    for prompt in prompts:
        flags = detections.get(prompt, [])
        report["results"].append({
            "prompt": prompt,
            "flags": flags,
            "risk_detected": len(flags) > 0
        })

    Path("reports").mkdir(exist_ok=True)

    filename = f"reports/{category}_report_{timestamp}.json"
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)

    return filename