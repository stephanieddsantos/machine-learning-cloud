# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# Enterprise Challenge

## Hephaestus

## 👨‍🎓 Integrantes

- <a href="#">Carlos Mario Vieira de Melo</a>
- <a href="#">Matheus Cardoso Oliveira Lima</a>
- <a href="https://www.linkedin.com/in/silasfr">Silas Fernandes de Souza Fonseca</a>
- <a href="#">Stephanie Dias dos Santos</a>

## 👩‍🏫 Professores

### Tutor(a)

- <a href="https://www.linkedin.com/company/inova-fusca">Leonardo Ruiz Orabona</a>

### Coordenador(a)

- <a href="https://www.linkedin.com/company/inova-fusca">ANDRÉ GODOI CHIOVATO</a>

## 📜 Descrição

### FarmTech na era da cloud computing

**Machine Learning + Cloud Computing**

---

#### 1. Justificativa do Problema

Supondo que nosso grupo é a FarmTech Solutions prestando serviços de IA para uma fazenda de médio porte (200 hectares ou aproximadamente 210 campos de futebol oficiais) que produz várias culturas. Nosso time precisa analisar uma base de dados com informações de condições de solo e temperatura, relacionadas com o tipo de produto agrícola dessa fazenda. Nosso objetivo é prever o rendimento de safra (conforme visto no capítulo 13 - Modelagem de Dados com Regressão Supervisionada, da Fase 4) e explorar a tendência de produtividade (visto no capítulo 10 - Machine Learning Sem Supervisão: Uma Jornada pela Descoberta de Dados, da Fase 5).

---

#### 2. Solução Proposta

Baseado no dataset apresentado, nos propusemos a:

- Fazer uma análise exploratória na base para se familiarizar com os dados;
- Encontrar tendências para os rendimentos das plantações, por meio de clusterizações, e identificar se existem cenários discrepantes (outliers);
- Fazer cinco modelos preditivos (cada um com um algoritmo diferente, conforme visto no capítulo “Modelagem de Dados com Regressão Supervisionada”) que, dadas as condições, prevejam qual será o rendimento da safra. Esta parte da tarefa inclui seguir as boas práticas dos projetos de Machine Learning, assim como avaliar o modelo com métricas pertinentes ao problema.

---

#### 3. Tecnologias Utilizadas

| Camada                  | Ferramentas                                |
| ----------------------- | ------------------------------------------ |
| Coleta IoT              | MQTT, Node-RED                     |
| Armazenamento           | DynamoDB           |
| ETL / Feature Eng.      | Python (Pandas, Numpy)               |
| Modelagem               | TensorFlow, Keras |
| API / Deploy            | TensorFlow Serving, FastAPI, Docker        |
| Visualização            | Grafana ou React                  |

---

## 🗃 Histórico de lançamentos

- 0.1.0 - 12/09/2025

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>
