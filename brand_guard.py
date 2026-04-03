"""
Copyright (C) 2026 Cristina Voda
This file is part of ALIA-detect.

Licensed under the GNU General Public License v3.0 (GPL-3.0)
"""

import re


CATEGORIES = {
    "sesgo_genero": {
        "keywords": [
            "hombres", "mujeres",
            "liderazgo masculino", "liderazgo femenino",
            "mejor que", "peor que",
            "rol natural", "por naturaleza",
            "profesiones adecuadas",
            "llegar a puestos directivos",
            "carreras técnicas",
            "maternidad", "paternidad"
        ],
        "patterns": [
            "diferencias entre",
            "más adecuado para",
            "suele haber más",
            "afecta a la carrera"
        ]
    },

    "asesoramiento_especializado": {
        "keywords": [
            "diagnóstico", "tratamiento", "medicación",
            "dejar de tomar", "síntomas",
            "denunciar", "demanda", "legal",
            "invertir", "inversión", "préstamo", "deudas",
            "recurrir una multa",
            "datos personales"
        ],
        "patterns": [
            "qué debería hacer",
            "qué me recomiendas",
            "es buena idea",
            "qué opción es mejor",
            "qué pasos debería seguir",
            "puedo denunciar",
            "puedo recurrir"
        ]
    },

    "lenguaje_ofensivo": {
        "keywords": [
            "idiota", "imbécil", "estúpido",
            "tonto", "asqueroso", "mierda", "puta"
        ],
        "patterns": []
    },

    "discurso_odio": {
        "keywords": [
            "odio", "odio a", "no puedo soportar",
            "son inferiores", "no deberían existir",
            "hay que expulsar", "hay que eliminar",
            "asquerosos", "repugnantes"
        ],
        "patterns": [
            "todos los .* son",
            "hay que eliminar a",
            "no puedo soportar .*",
            "odio a .*",
            "los .* son .*"
        ]
    },

    "contenido_sexual": {
        "keywords": [
            "pornografía",
            "contenido sexual",
            "acto sexual",
            "desnudo",
            "explícito"
        ],
        "patterns": [
            "relaciones sexuales",
            "contenido para adultos"
        ]
    }
}

TARGET_GROUPS = [
    "negros", "chinos", "moros", "inmigrantes",
    "musulmanes", "judíos", "gitanos"
]

def brand_guard(prompt: str):
    """
    Analiza un prompt y devuelve posibles riesgos de alineamiento con severidad.
    """
    prompt_lower = prompt.lower()
    findings = []

    for category, rules in CATEGORIES.items():
        # Keywords
        for kw in rules["keywords"]:
            if kw in prompt_lower:
                # Asignar severidad
                severity = "high" if category == "hate_speech" else "medium"
                findings.append({
                    "category": category,
                    "trigger": kw,
                    "type": "keyword",
                    "severity": severity
                })

        for pattern in rules["patterns"]:
            if re.search(pattern, prompt_lower, re.IGNORECASE):
                severity = "high" if category == "hate_speech" else "medium"
                findings.append({
                    "category": category,
                    "trigger": pattern,
                    "type": "pattern",
                    "severity": severity
                })

    if "hate_speech" in CATEGORIES:
        for group in TARGET_GROUPS:
            if group in prompt_lower:
                if "odio" in prompt_lower or "no puedo soportar" in prompt_lower:
                    findings.append({
                        "category": "hate_speech",
                        "trigger": f"hate + group ({group})",
                        "type": "combined_rule",
                        "severity": "high"
                    })

    return findings


def summarize(findings: list) -> str:
    """
    Genera un resumen en lenguaje natural de los hallazgos, incluyendo nivel de riesgo.
    """
    if not findings:
        return "No se detectan riesgos aparentes."

    categories = {f["category"] for f in findings}
    severities = {f.get("severity", "medium") for f in findings}
    summaries = []

    if "hate_speech" in categories:
        summaries.append("El contenido puede incluir discurso de odio.")
    if "specialized_advice" in categories:
        summaries.append(
            "El prompt puede inducir a ofrecer asesoramiento especializado (médico, legal o financiero)."
        )
    if "gender_bias" in categories:
        summaries.append(
            "El prompt puede reforzar estereotipos o sesgos de género."
        )
    if "sexual_content" in categories:
        summaries.append(
            "El prompt puede incluir contenido sexual explícito."
        )
    if "offensive_language" in categories:
        summaries.append(
            "El prompt puede contener lenguaje ofensivo."
        )

    if "high" in severities:
        summaries.append("Nivel de riesgo: ALTO.🔴")
    elif "medium" in severities:
        summaries.append("Nivel de riesgo: MEDIO.🟡")
    else:
        summaries.append("Nivel de riesgo: BAJO.    🟢")

    return " ".join(summaries)