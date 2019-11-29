from django.shortcuts import render, redirect
from .models import Person, Street, Address, Flat
from . import forms
import datetime
from . import utils
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

default_start_date = f'{datetime.date.today():%Y-%m-%d}'


class Generate(LoginRequiredMixin, View):
    """
    Здесь сделать запрос на логин
    после логина показывать только разрешенные пользователю дома подьезды
    добывить выход на квитанции...
    """

    def get(self, request, date=f'{datetime.date.today():%Y-%m-%d}'):
        user_groups = request.user.groups.values()
        permit_entrance = []
        for group in user_groups:
            if 'подъезд' in group['name'] and group['name'][0].isdigit():
                permit_entrance.append(int(group['name'][0]))

        permit_entrance = [x for x in range(1,9)] if request.user.is_staff else permit_entrance
        person = Person.objects.all()[0] #get(user=request.user)

        entrance = request.GET.get("entrance", False)
        if not entrance:
            flat = Flat.objects.get(person=person)
            entrance = flat.entrance

        # chois_form = forms.Homepage_Form_Unique()
        # tmp = permit_entrance.pop(permit_entrance.index(entrance))
        # permit_entrance.insert(0, tmp)
        # test = [[x, x] for x in permit_entrance]
        # chois_form.fields['entrance'].choices = test
        entrance = int(entrance)
        if entrance not in permit_entrance:
            con = {
                # 'chois_form': chois_form,
                'permit_entrance': permit_entrance,
                'access_denied': True
            }
            return render(request, 'duty/duty.html', context=con)
        revers = request.GET.get("revers", False)
        revers = False if (revers == 'false' or not revers) else True
        dt = [int(x) for x in date.split('-')]
        start_day = datetime.date(dt[0], dt[1], dt[2])
        flats = utils.gen(start_day, entrance, revers)
        con = {
            # 'chois_form': chois_form,
            'permit_entrance': permit_entrance,
            'entrance': entrance,
            'revers': revers,
            'flats': flats,
            'start_day': start_day,
        }
        return render(request, 'duty/duty.html', context=con)


class FlatUpdate(LoginRequiredMixin, View):

    def get(self, request, id):
        start_day = request.GET.get('start_day', '')
        flat = Flat.objects.get(id=id)
        bound_form = forms.FlatForm(instance=flat)
        con = {
            'form': bound_form,
            'start_day': start_day,
            'view': 'update',
            'flat_id': id,
        }
        return render(request, 'duty/flat_update.html', context=con)

    def post(self, request, id):
        start_day = request.POST.get('start_day', '')

        flat = Flat.objects.get(id=id)
        bound_form = forms.FlatForm(request.POST, instance=flat)
        # print(f'day {start_day}')
        if bound_form.is_valid():
            bound_form.save()
            return redirect('generate', start_day)
        con = {
            'form': bound_form,
            'start_day': start_day,
            'view': 'update',
            'flat_id': id,
        }
        return render(request, 'duty/flat_update.html', context=con)


class FlatCreate(LoginRequiredMixin, View):
    def get(self, request):
        form = forms.FlatForm()
        con = {
            'form': form,
            'view': 'create'
        }
        return render(request, 'duty/flat_update.html', context=con)

    def post(self, request):
        bound_form = forms.FlatForm(request.POST)
        if bound_form.is_valid():
            bound_form.save()
            return redirect('generate')
        con = {
            'form': bound_form,
        }
        return render(request, 'duty/flat_update.html', context=con)


class FlatDelete(LoginRequiredMixin, View):
    def get(self, request, id):
        fl = Flat.objects.get(id=id)
        fl.delete()
        return redirect('generate')


class PersonUpdate(LoginRequiredMixin, View):
    def get(self, request, id):
        person = Person.objects.get(id=id)
        bound_form = forms.PersonForm(instance=person)
        con = {
            'form': bound_form,
            'person': person
        }
        return render(request, 'duty/person_update.html', context=con)

    def post(self, request, id):
        usr = request.user
        person = Person.objects.get(id=id)
        if not usr.is_staff:
            print('Ты не пройдешь!!!!')
            return redirect('generate')
        bound_form = forms.PersonForm(request.POST, instance=person)
        if bound_form.is_valid():
            bound_form.save()
            return redirect('generate')
        con = {
            'form': bound_form,
            'person': person
        }
        return render(request, 'duty/person_update.html', context=con)


class PersonCreate(LoginRequiredMixin, View):
    def get(self, request):
        form = forms.PersonForm()
        con = {
            'form': form
        }
        return render(request, 'duty/person_update.html', context=con)

    def post(self, request):
        bound_form = forms.PersonForm(request.POST)
        if bound_form.is_valid():
            bound_form.save()
            return redirect('generate')
        con = {
            'form': bound_form
        }
        return render(request, 'duty/person_update.html', context=con)


def home(request):
    return render(request, 'duty/index.html', context={})
