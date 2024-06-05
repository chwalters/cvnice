from typing import Optional
from services.basic_lingua.blingua_sdk_python.src.blinguasdk import BlinguaSDK
from services.basic_lingua.blingua_sdk_python.src.blinguasdk.models import errors

prompts_by_job_category = {
}

DEFAULT_IT_PROMPTS = dict(
    keywords=dict(
        question="In the job offer, what keywords are found that describe the technologies, skills and programming languages the applicant should have experience with? Show the results as an array of keywords in JSON.  If there are no keywords found, return an empty JSON array.",
        result_path="keywords"
    ),
    title=dict(
        question="What is the job title in the job offer?",
        result_path="title"
    ),
    location=dict(
        question="What is the location of the job in the job offer?",
        result_path="location"
    ),
    company=dict(
        question="What is the hiring company or organization of the job in the job offer?",
        result_path="company"
    ),
    hiring_manager_email=dict(
        question="What is the hiring manager's email or contact email of the job in the job offer? Only return a valid email address or nothing at all.",
        result_path="hiring_manager.email"
    ),
    hiring_manager_name=dict(
        question="What is the hiring manager's name of the job in the job offer?  If not provided, return nothing at all.",
        result_path="hiring_manager.name"
    ),
    hiring_manager_phone=dict(
        question="What is the hiring manager's telephone number of the job in the job offer? If not provided, return nothing at all.",
        result_path="hiring_manager.phone"
    ),
    job_type=dict(
        question="Which of the following best describes the type of the job in the job offer: Full Time, Part Time, Contractor, Intern, Apprentice, or Other?",
        result_path="job_type"
    ),
    work_mode=dict(
        question="Which of the following best describes where the work can be performed of the job in the job offer: Remote, Onsite, Hybrid, or Other?",
        result_path="work_mode"
    ),
    url=dict(
        question="What is the web link or contact URL of the job in the job offer? Only return a valid URL, and if not provided, return nothing at all.",
        result_path="url"
    )
)

def get_job_prompts(job_category: str, defaults: Optional[dict]) -> Optional[dict]:
    prompts: Optional[dict] = prompts_by_job_category.get(job_category, None)
    if prompts is None:
        prompts = defaults
        if prompts is not None:
            prompts_by_job_category[job_category] = prompts
    return prompts


class Prompter:

    def __init__(self, api_key: str):
        self.sdk = BlinguaSDK()
        self.api_key = api_key

    def qna(self, question: str, input_text: str) -> Optional[str]:
        result_text: Optional[str] = None
        try:
           res = self.sdk.text_qna_wrapper_text_qna_question_post(
                question=question,
                request_body=input_text,
                api_key=self.api_key
            )
           if res is not None and res.text_result is not None:
               result_text = res.text_result.results
        except errors.SDKError as e:
            result_text = "Not available"
        return result_text

    def summarize(self, input_text: str, summary_length: str = "short") -> Optional[str]:
        result_text = None
        try:
            res = self.sdk.text_summarize_wrapper_text_summarize_summary_length_post(
                summary_length = summary_length,
                request_body = input_text,
                api_key = self.api_key
            )
            if res is not None and res.text_result is not None:
                result_text = res.text_result.results
        except errors.SDKError as e:
            result_text = "Not available"

        return result_text
