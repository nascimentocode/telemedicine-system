from django.shortcuts import render, redirect
from medico.models import DadosMedico, Especialidades, DatasAbertas, is_medico
from .models import Consulta, Documento
from datetime import datetime
from django.contrib import messages
from django.contrib.messages import constants


# Create your views here.
def home(request):
    if request.method == "GET":
        medico_filtrar = request.GET.get("medico")
        especialidades_filtrar = request.GET.getlist("especialidades")

        medicos = DadosMedico.objects.all()

        if medico_filtrar:
            medicos = medicos.filter(nome__icontains=medico_filtrar)

        if especialidades_filtrar:
            medicos = medicos.filter(especialidade_id__in=especialidades_filtrar)

        especialidades = Especialidades.objects.all()

        return render(
            request,
            "home.html",
            {
                "medicos": medicos,
                "especialidades": especialidades,
                "is_medico": is_medico(request.user),
            },
        )


def escolher_horario(request, id_dados_medicos):
    if request.method == "GET":
        medico = DadosMedico.objects.get(id=id_dados_medicos)
        datas_abertas = (
            DatasAbertas.objects.filter(user=medico.user)
            .filter(data__gte=datetime.now())
            .filter(agendado=False)
            .order_by("data")
        )

        return render(
            request,
            "escolher_horario.html",
            {
                "medico": medico,
                "datas_abertas": datas_abertas,
                "is_medico": is_medico(request.user),
            },
        )


def agendar_horario(request, id_data_aberta):
    if request.method == "GET":
        data_aberta = DatasAbertas.objects.get(id=id_data_aberta)

        horario_agendado = Consulta(paciente=request.user, data_aberta=data_aberta)
        horario_agendado.save()

        data_aberta.agendado = True
        data_aberta.save()

        messages.add_message(
            request, constants.SUCCESS, "Consulta agendada com sucesso"
        )

        return redirect("/pacientes/minhas_consultas/")


def minhas_consultas(request):
    if request.method == "GET":
        especialidade_consulta_filtrar = request.GET.get("especialidades")
        data_consulta_filtrar = request.GET.get("data")

        minhas_consultas = (
            Consulta.objects.filter(paciente=request.user)
            .filter(data_aberta__data__gte=datetime.now())
            .order_by("data_aberta__data")
        )

        print(minhas_consultas.values("data_aberta__data"))

        # if especialidade_consulta_filtrar:
        #     dado_medico = DadosMedico.objects.get(
        #         user=minhas_consultas.data_aberta.user
        #     )
        #     minhas_consultas = dado_medico.objects.filter(
        #         especialidade=especialidade_consulta_filtrar
        #     )

        if data_consulta_filtrar:
            minhas_consultas = minhas_consultas.filter(
                data_aberta__data__icontains=data_consulta_filtrar
            )

        return render(
            request,
            "minhas_consultas.html",
            {
                "minhas_consultas": minhas_consultas,
                "is_medico": is_medico(request.user),
            },
        )


def consulta(request, id_consulta):
    if request.method == "GET":
        consulta = Consulta.objects.get(id=id_consulta)
        dado_medico = DadosMedico.objects.get(user=consulta.data_aberta.user)
        documentos = Documento.objects.filter(consulta=consulta)

        return render(
            request,
            "consulta.html",
            {
                "consulta": consulta,
                "dado_medico": dado_medico,
                "documentos": documentos,
            },
        )


def cancelar_consulta(request, id_consulta):
    consulta = Consulta.objects.get(id=id_consulta)

    if request.user != consulta.paciente:
        messages.add_message(request, constants.ERROR, "Essa consulta não é sua")
        return redirect("/pacientes/minhas_consultas/")

    consulta.status = "C"
    consulta.save()

    return redirect(f"/pacientes/consulta/{id_consulta}")
