import json

def load_candidates():
    with open("candidates.json", "r", encoding="utf-8") as file:
        return json.load(file)

def get_candidates_all():
    """возвращает список всех кандидатов"""
    return load_candidates()

def get_candidate_by_pk(id):
    """возвращает одного кандидата по его id"""
    for candidate in load_candidates(id):
        if candidate['id'] == id:
            return candidate
    return 'Not found'

def get_candidates_by_name(candidate_name):
    result = []
    for candidate in load_candidates():
        if candidate_name.lower() in candidate['name'].lower():
            result.append(candidate)
    return result


def get_candidates_by_skill(skill):
    """возвращает кандидатов по навыку"""
    result = []
    for candidate in load_candidates():
        skills = candidate['skills'].lower().split(', ')
        if skill in skills:
            result.append(candidate)
    return result