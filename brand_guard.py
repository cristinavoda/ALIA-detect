"""
ALIA-detect
Human-in-the-loop risk detector for LLM alignment.
Focus: Gender bias & Specialized advice.
"""

CATEGORIES = {
    "gender_bias": {
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

    "specialized_advice": {
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
    }
}


def brand_guard(prompt: str):
    """
    Analiza un prompt y devuelve posibles riesgos de alineamiento.
    """
    prompt_lower = prompt.lower()
    findings = []

    for category, rules in CATEGORIES.items():
        
        for kw in rules["keywords"]:
            if kw in prompt_lower:
                findings.append({
                    "category": category,
                    "trigger": kw,
                    "type": "keyword"
                })

        
        for pattern in rules["patterns"]:
            if pattern in prompt_lower:
                findings.append({
                    "category": category,
                    "trigger": pattern,
                    "type": "pattern"
                })

    return findings