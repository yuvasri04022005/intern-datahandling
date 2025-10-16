semi_structured_data = {
    "name": "Yuva",
    "skills": ["Python", "SQL", "Machine Learning"],
    "education": {"degree": "B.Tech", "department": "AI & DS"}
}
import json
print(json.dumps(semi_structured_data, indent=2))