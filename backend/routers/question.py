from fastapi import APIRouter, Body
import aiohttp
from backend.schemas.question import QuestionsNumberRequest, QuestionResponse
from backend.database.methods import get_question, add_all_questions
import datetime

router = APIRouter()


@router.post("/add")
async def add_questions(body: QuestionsNumberRequest = Body(...)) -> QuestionResponse:
    questions_number = body.questions_num
    new_questions: list[QuestionResponse] = []
    async with aiohttp.ClientSession() as session:
        while questions_number:
            new_questions.clear()
            url = "https://jservice.io/api/random"
            params = {"count": questions_number}
            async with session.get(url, params=params) as resp:
                received_questions: list[dict] = await resp.json(content_type=None)
            for question in received_questions:
                question_db = await get_question(question_id=question["id"])
                if question_db is None:
                    date_format = "%Y-%m-%dT%H:%M:%S.%fZ"
                    question["created_at"] = datetime.datetime.strptime(question["created_at"], date_format)
                    question["updated_at"] = datetime.datetime.strptime(question["updated_at"], date_format)
                    new_questions.append(QuestionResponse(**question))
            await add_all_questions(new_questions)
            questions_number = questions_number - len(new_questions)
    return new_questions[-1] if new_questions else QuestionResponse()
