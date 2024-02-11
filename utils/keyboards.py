from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from data.answerOptions import START_TEST


def get_test_answer_options_keyboard(questionIndex):
    kb = InlineKeyboardMarkup(
        resize_keyboard=True,
        row_width=5,
        inline_keyboard=[
            [InlineKeyboardButton(text=str(option), callback_data=str(questionIndex) + " " + str(option))
             for option in range(1, 6)],
            [InlineKeyboardButton(text=str(option), callback_data=str(questionIndex) + " " + str(option))
             for option in range(6, 11)]
        ])
    return kb

def get_start_test_answer():
    kb = InlineKeyboardMarkup(
        resize_keyboard=True,
        row_width=1,
        inline_keyboard=[[InlineKeyboardButton(text=START_TEST, callback_data=START_TEST)]])
    return kb