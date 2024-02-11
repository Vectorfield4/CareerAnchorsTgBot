from typing import List

from Question import Question
from data import questions, categoriesAndQuestions, CareerCategory, NO_CATEGORY
from main import bot
from utils.keyboards import get_test_answer_options_keyboard


def get_questions() -> List[Question]:
    result = [None] * len(questions)
    for categoryAndQuestion in categoriesAndQuestions.items():
        for questionNumber in categoryAndQuestion[1][0]:
            question = Question(
                index=questionNumber-1,
                text=questions[questionNumber-1],
                category=categoryAndQuestion[0])
            result[questionNumber-1] = question
    return result

async def send_question(chat_id: int, question: Question) -> None:
    await bot.send_message(
        chat_id,
        text = question.text,
        reply_markup=get_test_answer_options_keyboard(question.index)
    )
async def send_result(chat_id:int, questions:List[Question]):
    answers = {}
    max_category_sum = 0
    category = None
    for category in CareerCategory:
        answers[category] = 0
    for question in questions:
        answers[question.category] += question.answer
    print("Answers:", answers)
    for answer_category, answer_sum in answers.items():
        category_sum = float(answer_sum) / len(categoriesAndQuestions[answer_category][0])
        if (category_sum > max_category_sum):
            max_category_sum = category_sum
            category = answer_category
    if (max_category_sum >= 5):
        await bot.send_message(
            chat_id,
            text=categoriesAndQuestions[category][1]
        )
    else:
        await bot.send_message(
            chat_id,
            text=NO_CATEGORY
        )