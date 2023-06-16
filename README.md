# Desafio-Aceleradora-Agil
Este repositório contém a solução para o desafio de programação "Clínica de Consultas Ágil" da Aceleradora Ágil. O objetivo do desafio era desenvolver um sistema de clínica de consultas que permite cadastrar pacientes, marcar consultas, cancelar consultas e exibir informações relevantes ao usuário.

## Funcionalidades implementadas

- Cadastro de paciente: o programa permite cadastrar pacientes, solicitando o nome e o telefone do usuário. Também trata erros de duplicidade de cadastro.
- Marcações de consultas: é possível visualizar a lista de pacientes cadastrados e selecionar um paciente para agendar uma consulta. O usuário informa o dia, a hora e a especialidade desejada para a consulta.
- Cancelamento de consultas: o programa exibe a lista de agendamentos existentes e permite selecionar um agendamento para cancelar. O usuário confirma o cancelamento e a consulta é removida da lista.
- Tratamento de erros: foram implementadas validações para evitar duplicidade de cadastro, marcação de consultas em dias/horários já agendados e marcação de consultas retroativas.

Além disso, há duas versões do código disponíveis neste repositório:
1. `clinica_sem_banco_de_dados.py`: implementação sem o uso de banco de dados.
2. `clinica_com_banco_de_dados.py`: implementação utilizando um banco de dados MySQL para armazenar informações dos pacientes.

## Tecnologias utilizadas

- Python
- MySQL (somente na versão com banco de dados)
