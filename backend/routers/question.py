import datetime

import aiohttp
from fastapi import APIRouter, Body

from backend.database.methods import add_all_questions, get_question
from backend.schemas.question import QuestionResponse, QuestionsNumberRequest

router = APIRouter()


@router.post("/add")
async def add_questions(body: QuestionsNumberRequest = Body(...)) -> QuestionResponse | dict:
    questions_number = body.questions_num
    new_questions: list[QuestionResponse] = []
    async with aiohttp.ClientSession() as session:
        # Until the required number of questions have been added, request again
        while questions_number:
            new_questions.clear()
            url = "https://jservice.io/api/random"
            params = {"count": questions_number}
            async with session.get(url, params=params) as resp:
                received_questions: list[dict] = await resp.json(content_type=None)
            for question in received_questions:
                # Checking for a question in the database
                question_db = await get_question(question_id=question["id"])
                if question_db is None:
                    date_format = "%Y-%m-%dT%H:%M:%S.%fZ"
                    question["created_at"] = datetime.datetime.strptime(
                        question["created_at"], date_format
                    )
                    question["updated_at"] = datetime.datetime.strptime(
                        question["updated_at"], date_format
                    )
                    new_questions.append(QuestionResponse(**question))
            await add_all_questions(new_questions)

            # Calculate: the total number of questions needed minus the number of questions we added
            # Save the new missing number of questions
            questions_number = questions_number - len(new_questions)
    return new_questions[-1] if new_questions else {}
