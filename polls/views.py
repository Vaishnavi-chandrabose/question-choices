from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Question
from .models import Choice
from django.http import JsonResponse
from django.utils import timezone
from django.shortcuts import get_object_or_404
import json


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def login(request):
    template = 'login.html'
    return render(request, template)


def questions(request):
    questions = Question.objects.all()
    template = 'database_page.html'  
    context = {'questions': questions}
    return render(request, template, context)


def get_questions(request):
    questions = Question.objects.all()
    question_list = [
        {"id": question.id, "question_text": question.question_text}
        for question in questions
    ]
    return JsonResponse({"questions": question_list})



def add_choice(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)

        if request.method == 'POST':
            data = json.loads(request.body)
            choice_text = data.get('choice_text', '')

            if choice_text:
                new_choice = Choice(question=question, choice_text=choice_text)
                new_choice.save()
                return JsonResponse({'message': 'Choice added successfully'})
            else:
                return JsonResponse({'message': 'Invalid choice text'}, status=400)

    except Question.DoesNotExist:
        return JsonResponse({'message': 'Question not found'}, status=404)


def get_choices(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    choices = question.choice_set.all()
    choices_data = [{'id': choice.id, 'choice_text': choice.choice_text} for choice in choices]
    return JsonResponse({'choices': choices_data})




def add_question(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        question_text = data.get('question_text', '')

        if question_text:
            new_question = Question(question_text=question_text, pub_date=timezone.now())
            new_question.save()
            return JsonResponse({'message': 'Question added successfully'})
        else:
            return JsonResponse({'message': 'Invalid question text'}, status=400)


def delete_question(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
        question.delete()
        return JsonResponse({'message': 'Question deleted successfully'})
    except Question.DoesNotExist:
        return JsonResponse({'message': 'Question not found'}, status=404)


def edit_question(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)

        if request.method == 'POST':
            data = json.loads(request.body)
            new_question_text = data.get('new_question_text', '')

            if new_question_text:
                question.question_text = new_question_text
                question.save()
                return JsonResponse({'message': 'Question updated successfully'})
            else:
                return JsonResponse({'message': 'Invalid question text'}, status=400)
        
        template = 'edit_question.html'  # Create a new template for editing questions
        context = {'question': question}
        return render(request, template, context)

    except Question.DoesNotExist:
        return JsonResponse({'message': 'Question not found'}, status=404)

def update_question_text(request, question_id):
    try:
        question = get_object_or_404(Question, id=question_id)
        updated_text = request.POST.get('updated_question_text', '')
        question.question_text = updated_text
        question.save()
        return JsonResponse({'message': 'Question text updated successfully'})
    except Question.DoesNotExist:
        return JsonResponse({'message': 'Question not found'}, status=404)


def get_question_text(request, question_id):
    try:
        question = Question.objects.get(id=question_id)
        return JsonResponse({'message': 'Question text fetched successfully', 'question_text': question.question_text})
    except Question.DoesNotExist:
        return JsonResponse({'message': 'Question not found'}, status=404)


