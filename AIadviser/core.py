
import os
from types import SimpleNamespace
from openai import OpenAI

class LiaraLLM:
    """
    Wrapper ساده که متد invoke(prompt) را شبیه به فرمتی که شما در کدتان استفاده می‌کنید،
    پیاده‌سازی می‌کند و خروجی‌ای با فیلد .content برمی‌گرداند.
    """
    def __init__(self, base_url=None, api_key=None, model="openai/gpt-4o-mini", temperature=0.3):
        self.base_url = "https://ai.liara.ir/api/v1/68a1c6d25cf1e1c2c649fb6c"
        self.api_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySUQiOiI2ODlhZWQ4MjFhYTM5ZDAzY2ZhZWY1NTciLCJ0eXBlIjoiYXV0aCIsImlhdCI6MTc1NTg1MDcyNH0.pOa32MUDEQYRvhvmhR4ffJbKX-thYFn43Zc-0EB1xxI"  # کلیدتون
        self.model = model
        self.temperature = temperature

        if not self.base_url or not self.api_key:
            raise ValueError("LIARA_BASE_URL or LIARA_API_KEY not set in environment")

        # نمونه‌سازی کلاینت
        self.client = OpenAI(base_url=self.base_url, api_key=self.api_key)

    def invoke(self, prompt_text):
        completion = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt_text}],
            temperature=self.temperature
        )
        text = completion.choices[0].message.content
        return SimpleNamespace(content=text)


def models():

    #set up our llm model

    llm_liara = LiaraLLM(
        base_url=os.getenv("LIARA_BASE_URL", "https://ai.liara.ir/api/v1/YOUR_APP_ID"),
        api_key=os.getenv("LIARA_API_KEY", "YOUR_LIARA_API_KEY"),
        model=os.getenv("LIARA_MODEL", "openai/gpt-4.1"),
        temperature=0.3
    )

    return(llm_liara)

def final_template(user_answers):

    template_final = ("""
            You are a professional educational and career counselor, specializing in personality-based guidance using psychological analysis.
            Based on the user's provided data, analyze their personality traits, strengths, and potential challenges to recommend personalized academic and career paths.

            User Data:
            - Gender: {gender}
            - Education Level: {education}
            - Preferred Work Environment: {preferred_env}
            - Social Interaction Style: {social_interaction}
            - Physical Skill Level: {physical_skill}
            - Responsibility Preference: {responsibility_pref}
            - Current Major/Field: {major}
            - Location: {city}
            - Contact: {phone}
            - Primary Concerns: {concerns}

            Your Task:
            1. Analyze the user's personality profile by identifying:
            - Key strengths based on their skills and preferences
            - Potential challenges indicated by their concerns
            - Suitable work environments matching their preferences
            - Optimal social interaction styles for their success

            2. Provide 5 personalized recommendations covering:
            - Academic paths (degrees/certifications to pursue)
            - Career fields aligned with their profile
            - Skill development opportunities
            - Work environment suggestions
            - Practical next steps addressing their concerns

            3. Format Requirements:
            - Write the entire response in Persian language
            - Use clear section headers for readability
            - Prioritize recommendations that address their stated concerns
            - Include location-specific suggestions when relevant to {city}
            - Maintain a supportive and professional tone

            Important Considerations:
            - Consider how {physical_skill} might influence career suitability
            - Balance {responsibility_pref} with realistic career progression
            - Address {concerns} directly with actionable solutions
            - Suggest resources accessible in {city} when possible
            """)

    formatted_template_final = template_final.format(**user_answers)

    return formatted_template_final

def generate_final_result(llm_model, final_template_text):

    final_result = llm_model.invoke(final_template_text)
    final_text = final_result.content
    return final_text