# myapp/views.py
from django.shortcuts import render
from .forms import ConditionForm

def condition_view(request):
    output = ""
    if request.method == 'POST':
        form = ConditionForm(request.POST)
        if form.is_valid():
            # Get form data
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            c = form.cleaned_data['c']
            d = form.cleaned_data['d']

            # Evaluate conditions
            if a < b:
                if c > d:
                    output = "Condition 1: a < b and c > d"
                elif c == d:
                    output = "Condition 2: a < b and c == d"
                else:
                    output = "Condition 3: a < b and c < d"
            elif a == b:
                output = "Condition 4: a == b"
            elif c == d:
                output = "Condition 5: c == d"
            else:
                output = "Condition 6: None of the above"
    else:
        form = ConditionForm()

    return render(request, 'myapp/test.html', {'form': form, 'output': output})
