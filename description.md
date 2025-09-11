1) DESCRIÇÃO RÁPIDA DO PROJETO:
Para a Fase 5, vamos colocar a mão na massa no desenvolvimento de duas entregas obrigatórias: Machine Learning e Computação em Nuvem. Além dessas, vamos ter outras duas entregas definidas como “Ir Além”, que não valem nota. Contudo, esperamos que os grupos se desafiem em aprender ainda mais com essas duas entregas extras. Como recompensa das entregas dos “Ir Além”, os grupos ganharão gratificações (não notas) que serão explicadas ainda nesse documento.
2) DESCRIÇÃO DETALHADA DO PROJETO:
2.1) Entrega 1:
Você e o seu grupo estão na FarmTech Solutions prestando serviços de IA para uma fazenda de médio porte (200 hectares ou aproximadamente 210 campos de futebol oficiais) que produz várias culturas. Seu time precisa analisar uma base de dados com informações de condições de solo e temperatura, relacionadas com o tipo de produto agrícola dessa fazenda. Você deverá prever o rendimento de safra (conforme visto no capítulo 13 - Modelagem de Dados com Regressão Supervisionada, da Fase 4) e explorar a tendência de produtividade (visto no capítulo 10 - Machine Learning Sem Supervisão: Uma Jornada pela Descoberta de Dados, da Fase 5).
Base de dados: a base está anexada no portal, disponível no arquivo “crop_yield.csv”. As variáveis são:
Cultura: o nome da safra para a qual o rendimento está sendo medido.
Precipitação (mm dia 1): a quantidade de chuva em milímetros por dia.
Umidade específica a 2 metros (g/kg): a quantidade de vapor de água no ar por quilograma de ar seco a uma altura de 2 metros acima do solo.
Umidade relativa a 2 metros (%): a quantidade de vapor de água no ar como uma porcentagem da quantidade máxima de vapor de água que pode ser mantida a uma determinada temperatura e pressão.
Temperatura a 2 metros (ºC): a temperatura em graus Celsius a uma altura de 2 metros acima do solo.
Rendimento: a quantidade de rendimento em toneladas por hectare.
 
Metas da Entrega 1:
Baseado no dataset apresentado, sua atividade consiste em:
Fazer uma análise exploratória na base para se familiarizar com os dados;
Encontrar tendências para os rendimentos das plantações, por meio de clusterizações, e identificar se existem cenários discrepantes (outliers);
Fazer cinco modelos preditivos (cada um com um algoritmo diferente, conforme visto no capítulo “Modelagem de Dados com Regressão Supervisionada”) que, dadas as condições, prevejam qual será o rendimento da safra. Esta parte da tarefa inclui seguir as boas práticas dos projetos de Machine Learning, assim como avaliar o modelo com métricas pertinentes ao problema.
 
Entregáveis do Enunciado 1:
Entregue o link de um novo repositório do GitHub em nome do seu grupo (de 1 a 5 pessoas). Pedimos que não realize nenhum novo commit após a data da entrega, para não classificar como entrega após o prazo. Nesse repositório, faça o upload do link do notebook Jupyter, pois vamos executar seu notebook na correção. O Jupyter precisa ter:
Células de códigos executadas, com o código Python otimizado e com comentários das linhas;
Células de markdown organizando seu relatório e discorrendo textualmente sobre os achados a partir dos dados, e conclusões a respeito dos pontos fortes e limitações do trabalho;
O nome do arquivo deve conter seu nome completo, RM e pbl_fase4.ipynb, exemplo: “JoaoSantos_rm76332_pbl_fase4.ipynb”.
Vídeo: grave um vídeo de até 5 minutos demonstrando o funcionamento desse entregável, poste no YouTube de forma “não listado”, e coloque o link no seu GitHub, dentro do README.
Desenvolva o seu README com uma documentação introdutória, conduzindo o leitor para o seu Jupiter, onde lá, estará todo o passo a passo da sua solução e a sua descrição completa. Não precisa repetir a descrição do Jupiter no README do GitHub. Deixe sempre os seus repositórios públicos para que eles sejam acessíveis pela equipe interna da FIAP, mas cuidado com seus links para que não vazem e sejam compartilhados e plagiados.