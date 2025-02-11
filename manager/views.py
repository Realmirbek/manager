from .models import Candidate, Mentor, ActionHistory
from .forms import CandidateForm, MentorForm
from django.shortcuts import render, get_object_or_404, redirect


def candidate_list(request):
    not_contacted = Candidate.objects.filter(status='thinking')
    contacted = Candidate.objects.filter(status='contacted')
    passed_test_candidates = Candidate.objects.filter(status='passed_test')


    return render(request, 'manager/candidate_list.html', {
        'not_contacted': not_contacted,
        'contacted': contacted,
        'passed_test_candidates': passed_test_candidates,

    })

def candidate_detail(request, candidate_id):
    candidate = get_object_or_404(Candidate, id=candidate_id)
    return render(request, 'manager/candidate_detail.html', {'candidate': candidate})


# 📌 Добавление нового стажера
def add_candidate(request):
    if request.method == "POST":
        form = CandidateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('candidate_list')
    else:
        form = CandidateForm()
    return render(request, 'manager/add_candidate.html', {'form': form})

# 📌 Добавление нового ментора
def add_mentor(request):
    if request.method == "POST":
        form = MentorForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('mentor_list')
            except IntegrityError as e:
                form.add_error(None, f"Ошибка при сохранении: {e}")
    else:
        form = MentorForm()
    return render(request, 'manager/add_mentor.html', {'form': form})

# 📌 Отметить, что связались со стажером
def mark_contacted(request, candidate_id):
    candidate = get_object_or_404(Candidate, id=candidate_id)
    candidate.status = 'contacted'
    candidate.save()

    ActionHistory.objects.create(
        action_type='candidate_contacted',
        candidate=candidate,
        details=f"Статус стажера {candidate.name} изменен на 'связались'"
    )
    return redirect('candidate_list')

# 📌 Назначение ментора для стажера (только для тех, с кем связались)

def mark_status(request, candidate_id, status):
    candidate = get_object_or_404(Candidate.objects.filter(is_deleted=False), id=candidate_id)
    candidate.status = "passed_test"
    candidate.save()

    ActionHistory.objects.create(
        action_type=f"candidate_test",
        candidate=candidate,
        details=f"Статус стажера {candidate.name} изменен на '{status}'"
    )

    return redirect('candidate_list')


def assign_mentor(request, candidate_id):
    candidate = get_object_or_404(Candidate, id=candidate_id, status='contacted')
    mentors = Mentor.objects.all()

    if request.method == "POST":
        mentor_id = request.POST.get('mentor_id')
        if mentor_id:  # Проверяем, что mentor_id вообще пришёл
            mentor = get_object_or_404(Mentor, id=mentor_id)
            candidate.mentor = mentor
            candidate.save()

            # Логируем действие
            ActionHistory.objects.create(
                action_type='mentor_assigned',
                candidate=candidate,
                mentor=mentor,
                details=f"Ментор {mentor.name} был назначен стажеру {candidate.name}"
            )

            return redirect('candidate_list')
        else:
            return render(request, 'manager/assign_mentor.html', {
                'candidate': candidate,
                'mentors': mentors,
                'error': "Выберите ментора!",  # Сообщение об ошибке
            })

    return render(request, 'manager/assign_mentor.html', {
        'candidate': candidate,
        'mentors': mentors
    })
# 📌 Редактирование стажера
def edit_candidate(request, candidate_id):
    candidate = get_object_or_404(Candidate, id=candidate_id)
    if request.method == "POST":
        form = CandidateForm(request.POST, instance=candidate)
        if form.is_valid():
            form.save()
            return redirect('candidate_list')
    else:
        form = CandidateForm(instance=candidate)
    return render(request, 'manager/edit_candidate.html', {'form': form})

# 📌 Просмотр списка менторов
def mentor_list(request):
    mentors = Mentor.objects.all()  # Получаем всех менторов
    return render(request, 'manager/mentor_list.html', {'mentors': mentors})

# 📌 Редактирование ментора
def edit_mentor(request, mentor_id):
    mentor = get_object_or_404(Mentor, id=mentor_id)
    if request.method == "POST":
        form = MentorForm(request.POST, instance=mentor)
        if form.is_valid():
            form.save()
            return redirect('mentor_list')
    else:
        form = MentorForm(instance=mentor)
    return render(request, 'manager/edit_mentor.html', {'form': form})

# 📌 Удаление пользователя (стажера или ментора) навсегда
def delete_forever(request, model_name, user_id):
    if model_name == "candidate":
        user = get_object_or_404(Candidate, id=user_id)
    elif model_name == "mentor":
        user = get_object_or_404(Mentor, id=user_id)
    else:
        return redirect('candidate_list')  # Если пришел неправильный тип, возвращаем на список

    user.delete()  # Удаляем пользователя навсегда
    return redirect('mentor_list' if model_name == "mentor" else 'candidate_list')  # Перенаправляем обратно на список


def statistics_view(request):
    total_interns = Candidate.objects.count()  # Общее количество стажеров
    interns_with_mentor = Candidate.objects.filter(mentor__isnull=False).count()  # Количество стажеров с ментором
    interns_without_mentor = total_interns - interns_with_mentor  # Количество стажеров без ментора

    return render(request, 'manager/statistics.html', {
        'total_interns': total_interns,
        'interns_with_mentor': interns_with_mentor,
        'interns_without_mentor': interns_without_mentor,
    })

# views.py
def action_history(request):
    history = ActionHistory.objects.all().order_by('-timestamp')  # Сортируем по времени, от последнего
    return render(request, 'manager/action_history.html', {
        'history': history
    })






