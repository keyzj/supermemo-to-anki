import json
import logging

from bs4 import BeautifulSoup

from src.utils import check_response


def get_courses(requests_session, user_id):
    url = f"https://app.supermemo.com/api/users/{user_id}/learntCourses?includeTestCourses=true"
    response = requests_session.get(url)
    check_response(200, response.status_code, response, 'get_courses')

    courses = response.json()

    parse_fields = ['title', 'id', 'allPages']
    parsed = []
    for course in courses:
        mapped = {}
        for key, value in course.items():
            if key in parse_fields:
                mapped[key] = value
        if len(mapped.keys()) > 0:
            parsed.append(mapped)

    return parsed


def clear_content_str(content_str):
    logging.debug(f"Clearing content_str: {content_str}")

    res = content_str.replace('&#160;', ' ')
    res = BeautifulSoup(res, "lxml").text
    res = res.replace('\r', ' ').replace('\n', ' ').replace('\xa0', '').strip()

    return res


def clear_card_content(raw_content):
    json_content = json.loads(raw_content)
    content_str = json_content['content']
    return clear_content_str(content_str)


def get_cards(requests_session, user_id, course_id, limit):
    if limit >= 1000:
        raise NotImplementedError('Be nice to SuperMemo and implement pagination!')

    url = f"https://app.supermemo.com/api/users/{user_id}/courses/{course_id}/pages?limit={limit}&lt=0&rt=0"
    response = requests_session.get(url)
    check_response(200, response.status_code, response, 'get_cards')

    cards = response.json()

    parse_fields = ['pageNumber', 'question', 'answer', 'courseId']
    parsed = []
    for card in cards:
        card_content = card['content']
        mapped = {}
        for key, value in card_content.items():
            if key in parse_fields:
                if key in ['question', 'answer']:
                    mapped[key] = clear_card_content(value)
                else:
                    mapped[key] = value
        if len(mapped.keys()) > 0:
            parsed.append(mapped)

    return parsed
