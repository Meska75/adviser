from django.shortcuts import render
from AIadviser.core import *
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='accounts:login')
def questions_view(request):
    return render(request , 'AIadviser/adviser-AI.html')

@login_required(login_url='accounts:login')
def airesult (request):
    if request.method == 'POST':
        answers = {
            'gender': request.POST.get('gender'),
            'education': request.POST.get('education'),
            'preferred_env': request.POST.get('preferred_env'),
            'social_interaction': request.POST.get('social_interaction'),
            'physical_skill': request.POST.get('physical_skill'),
            'responsibility_pref': request.POST.get('responsibility_pref'),
            'major': request.POST.get('major'),
            'city': request.POST.get('city'),
            'phone': request.POST.get('phone'),
            'concerns': request.POST.get('concerns'),
        }
        prompt = final_template(answers)
        llm = models()
        ai_result = generate_final_result(llm, prompt)
        content = {
            'answers': answers,
            'ai_result': ai_result,
        }

        return render(request, 'AIadviser/adviser-result.html', {'content':content})
    
    else:
        return render(request, 'AIadviser/adviser-result.html', {'content':"no result return, try agian!"})

