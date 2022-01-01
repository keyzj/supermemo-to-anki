import logging
import os

from dotenv import load_dotenv
from selenium import webdriver

from src.service.auth_service import auth_by_credentials, prepare_auth_session
from src.service.io_service import write_cards
from src.service.supermemo_service import get_courses, get_cards


def init_logger(log_level_root):
    logging.basicConfig(level=log_level_root, format='%(asctime)s %(process)d-%(levelname)s-%(name)s: %(message)s')


def read_envs():
    load_dotenv(verbose=True)
    envs = {
        'driver_path': os.getenv('DRIVER_PATH'),
        'email': os.getenv('EMAIL'),
        'pw': os.getenv('PW'),
        'user_id': os.getenv('USER_ID'),
        'delimiter': os.getenv('DELIMITER'),
        'log_level_root': os.getenv('LOGGING_LEVEL_ROOT', 'INFO')
    }
    return envs


def main():
    envs = read_envs()
    init_logger(envs['log_level_root'])

    driver = webdriver.Chrome(envs['driver_path'])

    base_url = "https://app.supermemo.com/"
    driver.get(base_url)

    auth_by_credentials(driver, envs['email'], envs['pw'])

    s = prepare_auth_session(driver)
    driver.close()

    user_id = envs['user_id']
    courses = get_courses(s, user_id)
    logging.info(f"Got: {len(courses)} total courses: {courses}")

    for course in courses:
        total_cards = course['allPages']
        course_title = course['title']
        logging.info(f"Request total cards: {total_cards} from course: {course_title}")
        cards = get_cards(s, user_id, course['id'], total_cards)

        logging.info(f"Got: {len(cards)} cards from course: {course_title}")
        write_cards(course_title, cards, envs['delimiter'])


if __name__ == '__main__':
    main()
