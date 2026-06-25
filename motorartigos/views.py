from django.shortcuts import render
from django.http import Http404

# Colocamos os dados FORA das funções para simular um banco de dados global
ARTIGOS_FALSOS = [
    {
        'id': 1,
        'titulo': 'Agente de IA integrado com Google Sheets no n8n',
        'nivel': 'A',
        'data_publicacao': '2026-06-24',
        'resumo': 'Os agentes de inteligência artificial estão a redefinir a automação moderna. Neste artigo técnico, exploramos como pode desenhar e orquestrar um fluxo...',
        'texto': '<p>Os agentes de inteligência artificial estão a redefinir a automação moderna. Neste artigo técnico, exploramos como pode desenhar e orquestrar um fluxo de trabalho autônomo completo utilizando o <strong>n8n</strong> para capturar, estruturar e validar dados de folhas de cálculo do Google Sheets sem intervenção manual contínua.</p><h3>Porque integrar agentes de IA na folha de cálculo?</h3><p>O Google Sheets serve frequentemente como repositório de dados inicial para equipas de marketing, suporte e vendas.</p>',
        'eixo': {'nome': 'Inteligência Artificial'},
        'autor': {'nome': 'Ana Costa', 'biografia': 'Cientista de Dados especialista em Machine Learning e Inteligência Artificial na nuvem.', 'email': 'ana.costa@exemplo.com'},
    },
    {
        'id': 2,
        'titulo': 'Como passar pela IA em processos seletivos em 2026',
        'nivel': 'I',
        'data_publicacao': '2026-06-23',
        'resumo': 'Com o avanço dos sistemas ATS potenciados por inteligência artificial, muitos perfis qualificados acabam descartados no primeiro estágio...',
        'texto': '<p>Com o avanço dos sistemas ATS (Applicant Tracking Systems) potenciados por inteligência artificial, muitos perfis qualificados acabam descartados no primeiro estágio. Descubra as técnicas cruciais para otimizar o seu portfólio e currículo técnico para leitura de algoritmos.</p><h3>O que procuram os algoritmos de recrutamento?</h3><p>Diferente de uma avaliação humana imediata, o robô procura correspondência de semântica e tokens de linguagens específicas configurados para a vaga.</p>',
        'eixo': {'nome': 'Programação'},
        'autor': {'nome': 'João Silva', 'biografia': 'Especialista em Gestão de Talento, DevOps e transformação ágil de equipas tecnológicas.', 'email': 'joao.silva@exemplo.com'},
    },
    {
        'id': 3,
        'titulo': 'Modelo preditivo: o guia completo para começar do zero',
        'nivel': 'B',
        'data_publicacao': '2026-06-18',
        'resumo': 'Seja bem-vindo ao mundo da inteligência analítica. Se sempre quis entender o que está por trás de sistemas que prevêem vendas...',
        'texto': '<p>Seja bem-vindo ao mundo da inteligência analítica. Se sempre quis entender o que está por trás de sistemas que prevêem vendas ou estimam preços de habitação, este guia prático de análise de regressão foi desenhado precisamente para si.</p><h3>Importância da Engenharia de Variáveis</h3><p>No desenvolvimento de modelos preditivos, a limpeza e a transformação dos dados iniciais representam mais de 70% do sucesso total.</p>',
        'eixo': {'nome': 'Data Science'},
        'autor': {'nome': 'Ana Costa', 'biografia': 'Cientista de Dados especialista em Machine Learning e Inteligência Artificial na nuvem.', 'email': 'ana.costa@exemplo.com'},
    }
]

def index(request):
    # Envia a lista toda para desenhar os cartões
    contexto = {
        'artigos': ARTIGOS_FALSOS
    }
    return render(request, 'index.html', contexto)

def artigo_detalhe(request, id):
    # Simula a procura no banco de dados usando um loop
    artigo_encontrado = None
    for artigo in ARTIGOS_FALSOS:
        if artigo['id'] == id:
            artigo_encontrado = artigo
            break
            
    # Se alguém digitar um ID que não existe (ex: /artigo/99/), mostra o erro 404
    if artigo_encontrado is None:
        raise Http404("Artigo não encontrado.")
        
    # Envia apenas o artigo clicado para a página de detalhes
    contexto = {
        'artigo': artigo_encontrado
    }
    return render(request, 'artigo.html', contexto)