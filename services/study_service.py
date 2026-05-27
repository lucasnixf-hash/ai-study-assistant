from agents.tutor_agent import tutor_stream_chat
from agents.quiz_agent import generate_quiz_stream
from agents.grader_agent import grade_answer_stream

def route_stream(task_type, payload):
    if task_type == "tutor":
        return tutor_stream_chat(payload["question"], payload["history"])
    if task_type == "quiz":
        return generate_quiz_stream(payload["topic"])
    if task_type == "grade":
        return grade_answer_stream(payload["question"], payload["student_answer"])
    raise ValueError("未知任务类型")