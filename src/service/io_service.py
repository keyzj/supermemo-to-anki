import logging


def write_cards(course_title, cards, separator):
    file = open(f"{course_title}.txt", 'w')
    for card in cards:
        question = card['question']
        answer = card['answer']
        if question and answer:
            card_str = f"{question}{separator}{answer}\n"
            logging.debug(f"Writing card as string: {card_str}")
            file.write(card_str)
    file.close()
