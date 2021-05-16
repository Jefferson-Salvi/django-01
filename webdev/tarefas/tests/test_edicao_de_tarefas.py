import pytest
from django.urls import reverse
from pytest_django.asserts import assertContains

from webdev.tarefas.models import Tarefa


@pytest.fixture
def tarefas_pendente(db):
    return Tarefa.objects.create(nome='Tarefa 1', feita=False)




@pytest.fixture
def resposta_com_tarefa_pendente(client, tarefas_pendente):
    resp = client.post(reverse('tarefas:detalhe', kwargs={'tarefa_id': tarefas_pendente.id}),
                       data={'feita': 'true', 'nome': f'{tarefas_pendente.nome}-editada'})
    return resp

def test_status_code(resposta_com_tarefa_pendente):
    assert resposta_com_tarefa_pendente.status_code == 302

def test_tarefa_feita(resposta_com_tarefa_pendente):
    assert Tarefa.objects.first().feita

import pytest
from django.urls import reverse
from pytest_django.asserts import assertContains

from webdev.tarefas.models import Tarefa


@pytest.fixture
def tarefas_feita(db):
    return Tarefa.objects.create(nome='Tarefa 1', feita=True)




@pytest.fixture
def resposta_com_tarefa_feita(client, tarefas_feita):
    resp = client.post(reverse('tarefas:detalhe', kwargs={'tarefa_id': tarefas_feita.id}),
                       data={ 'nome': f'{tarefas_feita.nome}-editada'})
    return resp

def test_tarefa_pendente(resposta_com_tarefa_feita):
    assert not Tarefa.objects.first().feita

