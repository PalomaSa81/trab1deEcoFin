#Para usar Streamlit criamos um ambiente virtual, então, lembre-se, no TERMINAL:

#Sempre navegue para a pasta do usuário (cd C:\Users\usuario).

#Ative o ambiente virtual (myenv\Scripts\activate).

#Navegue para a área de trabalho (cd Desktop).

#Rode seu código (streamlit run hello_world.py).

import streamlit as st

st.set_page_config(layout="wide") #tem que ser a primeira coisa do código

# Título grande
with st.container():
    st.title("Análise comparativa: Vivara e Trackfield de 2021 a 2023")

# Lista de indicadores
indicadores = ['Giro do Ativo Total',
    'Giro de Contas a Pagar',
    'Giro de Contas a Receber',
    'Giro de Estoques',
    'Grau de Utilização do Capital de Terceiros',
    'Índice de Cobertura de Caixa',
    'Índice de Cobertura de Juros',
    'Índice Payout',
    'Índice de Retenção',
    'Liquidez Corrente',
    'Liquidez Seca',
    'Margem Bruta',
    'Multiplicador do Capital Próprio',
    'Nível de Endividamento',
    'Prazo Médio de Contas a Receber',
    'Prazo Médio de Estoques',
    'Prazo Médio de Pagamentos',
    'ROA',
    'ROE']

# Dicionário mapeando indicadores às imagens
imagens = {
    'Giro do Ativo Total': 'grafico_Giro_Ativo_Total.png',
    'Giro de Contas a Pagar': 'grafico_Giro_Contas_Pagar.png',
    'Giro de Contas a Receber': 'grafico_Giro_Contas_Receber.png',
    'Giro de Estoques': 'grafico_Giro_Estoques.png',
    'Grau de Utilização do Capital de Terceiros': 'grafico_Grau_Utilizacao_Capital_Terceiros.png',
    'Índice de Cobertura de Caixa': 'grafico_Indice_Cobertura_Caixa.png',
    'Índice de Cobertura de Juros': 'grafico_Indice_Cobertura_Juros.png',
    'Índice Payout': 'grafico_Indice_Payout.png',
    'Índice de Retenção': 'grafico_Indice_Retencao.png',
    'Liquidez Corrente': 'grafico_Liquidez Corrente.png',
    'Liquidez Seca': 'grafico_Liquidez Seca.png',
    'Margem Bruta': 'grafico_Margem_Bruta.png',
    'Multiplicador do Capital Próprio': 'grafico_Multiplicador_Capital_Proprio.png',
    'Nível de Endividamento': 'grafico_Nível de Endividamento.png',
    'Prazo Médio de Contas a Receber': 'grafico_Prazo_Medio_Contas_Receber.png',
    'Prazo Médio de Estoques': 'grafico_Prazo_Medio_Estoques.png',
    'Prazo Médio de Pagamentos': 'grafico_Prazo_Medio_Pagamentos.png',
    'ROA': 'grafico_ROA.png',
    'ROE': 'grafico_ROE.png'
     #...
}

# Dicionário mapeando indicadores às imagens, títulos e textos
indicadores_info = {
    'Giro do Ativo Total': {
        'imagem': 'grafico_Giro_Ativo_Total.png',
        'titulo': 'Eficiência na Utilização dos Ativos',
        'texto': 'Medida da eficiência com que a empresa utiliza seus ativos para gerar receita. Um giro alto indica que a empresa está gerando mais receita por unidade monetária de ativos.'
    },
    'Giro de Contas a Pagar': {
        'imagem': 'grafico_Giro_Contas_Pagar.png',
        'titulo': 'Velocidade de Pagamento das Dívidas',
        'texto': 'Avalia a rapidez com que a empresa paga seus fornecedores. Um giro alto indica boa gestão de caixa e negociação de prazos.'
    },
    'Giro de Contas a Receber': {
        'imagem': 'grafico_Giro_Contas_Receber.png',
        'titulo': 'Eficiência na Cobrança de Clientes',
        'texto': 'Indica a velocidade com que a empresa recebe o pagamento de seus clientes. Um giro alto sinaliza uma gestão de crédito eficiente.'
    },
    'Giro de Estoques': {
        'imagem': 'grafico_Giro_Estoques.png',
        'titulo': 'Rotatividade dos Estoques',
        'texto': 'Medida da velocidade com que os produtos são vendidos e repostos. Um giro alto indica uma boa gestão de estoque e menor risco de obsolescência.'
    },
    'Grau de Utilização do Capital de Terceiros': {
        'imagem': 'grafico_Grau_Utilizacao_Capital_Terceiros.png',
        'titulo': 'Dependência de Capital de Terceiros',
        'texto': 'Indica a proporção do capital de terceiros (dívidas) em relação ao capital próprio. Um grau alto pode sinalizar maior risco financeiro.'
    },
    'Índice de Cobertura de Caixa': {
        'imagem': 'grafico_Indice_Cobertura_Caixa.png',
        'titulo': 'Capacidade de Pagar Dívidas de Curto Prazo',
        'texto': 'Avalia a capacidade da empresa de honrar suas obrigações de curto prazo com o caixa disponível.'
    },
    'Índice de Cobertura de Juros': {
        'imagem': 'grafico_Indice_Cobertura_Juros.png',
        'titulo': 'Capacidade de Pagar Encargos Financeiros',
        'texto': 'Indica a margem de segurança da empresa para pagar seus juros. Um índice alto indica menor risco de insolvência.'
    },
    'Índice Payout': {
        'imagem': 'grafico_Indice_Payout.png',
        'titulo': 'Proporção de Lucros Distribuídos',
        'texto': 'Indica a porcentagem dos lucros distribuídos aos acionistas em forma de dividendos.'
    },
    'Índice de Retenção': {
        'imagem': 'grafico_Indice_Retencao.png',
        'titulo': 'Proporção de Lucros Reinvestidos',
        'texto': 'Indica a porcentagem dos lucros reinvestidos na empresa para financiar o crescimento.'
    },
    'Liquidez Corrente': {
        'imagem': 'grafico_Liquidez Corrente.png',
        'titulo': 'Capacidade de Pagar Dívidas de Curto Prazo',
        'texto': 'Avalia a capacidade da empresa de honrar suas obrigações de curto prazo com os ativos circulantes.'
    },
    'Liquidez Seca': {
        'imagem': 'grafico_Liquidez Seca.png',
        'titulo': 'Capacidade de Pagar Dívidas Exigíveis Imediatamente',
        'texto': 'Similar à liquidez corrente, mas exclui os estoques da análise, fornecendo uma medida mais conservadora.'
    },
    'Margem Bruta': {
        'imagem': 'grafico_Margem_Bruta.png',
        'titulo': 'Rentabilidade das Vendas',
        'texto': 'Indica a porcentagem da receita que sobra após deduzir o custo dos produtos vendidos.'
    },
    'Multiplicador do Capital Próprio': {
        'imagem': 'grafico_Multiplicador_Capital_Proprio.png',
        'titulo': 'Ampliação dos Ativos em Relação ao Patrimônio Líquido',
        'texto': 'Indica quantas vezes o patrimônio líquido é multiplicado para gerar o ativo total.'
    },
    'Nível de Endividamento': {
        'imagem': 'grafico_Nível de Endividamento.png',
        'titulo': 'Proporção de Dívidas',
        'texto': 'Indica a proporção de dívidas em relação ao patrimônio líquido. Um nível alto pode sinalizar maior risco financeiro.'
    },
    'Prazo Médio de Contas a Receber': {
        'imagem': 'grafico_Prazo_Medio_Contas_Receber.png',
        'titulo': 'Tempo Médio para Receber dos Clientes',
        'texto': 'Indica o número médio de dias que a empresa leva para receber o pagamento de seus clientes.'
    },
    'Prazo Médio de Estoques': {
        'imagem': 'grafico_Prazo_Medio_Estoques.png',
        'imagem': 'grafico_Prazo_Medio_Estoques.png',
        'texto': 'Indica o número médio de dias que os produtos permanecem em estoque.'
    },
    'Prazo Médio de Pagamentos': {
        'imagem': 'grafico_Prazo_Medio_Pagamentos.png',
        'texto': 'Indica o número médio de dias que a empresa leva para pagar seus fornecedores.'
    },
    'ROA': {
        'imagem': 'grafico_ROA.png',
        'titulo': 'Retorno Sobre o Ativo Total',
        'texto': 'Medida da rentabilidade da empresa em relação ao ativo total. Um ROA alto indica que a empresa está gerando lucros significativos em relação ao valor de seus ativos.'
    },
    'ROE': {
        'imagem': 'grafico_ROE.png',
        'titulo': 'Retorno Sobre o Patrimônio Líquido',
        'texto': 'Demonstra a rentabilidade dos investimentos dos acionistas. Um ROE alto indica que a empresa está gerando lucros significativos em relação ao capital investido pelos acionistas.'
    }
}




#Colunas, para serem de tamanhos diferentes: st.columns([1, 2, 3])
col1, col2 = st.columns(2)

with col1:
    indicador_selecionado = st.selectbox('Selecione um indicador:', indicadores)
    st.image(imagens[indicador_selecionado], use_column_width=True, width=750)

with col2:
    #st.header("Indicador 1")
    #st.write("Um Texto Genérico sobre Finanças: A gestão financeira pessoal é fundamental para alcançar a liberdade financeira. Planejar o orçamento, investir de forma inteligente e economizar são a chave para construir um futuro mais seguro. Ao entender os conceitos básicos de finanças, como juros compostos, inflação e diversificação de investimentos, é possível tomar decisões mais conscientes e alcançar seus objetivos. No entanto, é importante lembrar que a educação financeira é um processo contínuo e que o mercado financeiro está em constante mudança.")
    #indicador_selecionado = st.selectbox('Selecione um indicador:', indicadores)
    info = indicadores_info[indicador_selecionado]
    st.header(info['titulo'])
    st.write(info['texto'])
#Colunas das Empresas
col1, col2 = st.columns(2)

with col1:
    st.header('Vivara')
    st.write('Este é o texto da primeira coluna. Você pode adicionar qualquer tipo de conteúdo aqui, como gráficos, imagens, etc.')

with col2:
    st.header('Trackfield')
    st.write('Este é o texto da segunda coluna. O Streamlit oferece uma grande variedade de componentes para criar interfaces interativas.')


# Criando a sidebar
st.sidebar.image("uff.png")
st.sidebar.write("Este projeto foi desenvolvido por (nossos nomes aqui).")
pdf_file = r"C:\Users\usuario\Desktop\meu_relatorio.pdf"
with st.sidebar:
    with open(pdf_file, "rb") as pdf:
        st.download_button(
            label="Download: relatorio_completo.pdf",
            data=pdf.read(),
            file_name="relatorio_completo.pdf",
            mime="application/pdf"
    )