from aiogram.filters import CommandStart
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery

from data import START_MESSAGE, TEST_HOW_IMPORTANT, TEST_AGREEMENT_DEGREE
from data.answerOptions import START_TEST
from main import dp, bot
from utils.functions import get_questions, send_question, send_result
from utils.keyboards import get_start_test_answer

questions = get_questions()

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await bot.send_message(
        message.chat.id,
        START_MESSAGE,
        reply_markup=get_start_test_answer()
    )

@dp.callback_query()
async def process_answer(callback: CallbackQuery) -> None:
    if (callback.data == START_TEST):
        await bot.send_message(
            callback.from_user.id,
            TEST_HOW_IMPORTANT
        )
        await send_question(callback.from_user.id, questions[0])
        return
    questionIndex = int(callback.data.split()[0])
    if (questionIndex == 20):
        await bot.send_message(
            callback.from_user.id,
            text=TEST_AGREEMENT_DEGREE
        )
    answer = int(callback.data.split()[1])
    nextQuestionIndex = questionIndex + 1
    questions[questionIndex].answer = answer
    if (nextQuestionIndex < len(questions)):
        nextQuestion = questions[nextQuestionIndex]
        await send_question(callback.from_user.id, nextQuestion)
    else:
        await send_result(callback.from_user.id, questions)