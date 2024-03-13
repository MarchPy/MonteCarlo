# Monte Carlo: Simulação de Investimentos e Análise de Resultados

## Introdução

Esse código permite analisar o potencial de retorno do investimento ao longo do tempo com base em simulações realistas dos retornos mensais dos ativos escolhidos.

1. **Classe `InvestmentSimulator`:** Esta classe é responsável por realizar a simulação de investimento.
2. **Inicialização:** No método `__init__`, são passados os ativos a serem simulados, o valor inicial do investimento, o número de simulações a serem executadas e o horizonte de tempo em meses para a simulação.
3. **Método `_fetch_data`:** Este método baixa os dados dos ativos utilizando a biblioteca yfinance.
4. **Método `_calculate_monthly_returns`:** Calcula os retornos mensais dos ativos com base nos dados baixados.
5. **Método `_simulate_investment`:** Realiza a simulação de investimento. Ele itera sobre o número de simulações e, para cada simulação, calcula o valor do investimento ao longo do tempo com base nos retornos mensais.
6. **Método `calculate_statistics`:** Calcula estatísticas sobre os resultados das simulações, como o lucro final médio, o desvio padrão do lucro final e os percentis do lucro final.
7. **Execução:** No bloco `__main__`, criamos uma instância do `InvestmentSimulator` com os ativos desejados, um valor inicial de investimento de R$ 10.000,00, 10 anos de simulação e 10.000 simulações. Em seguida, calculamos as estatísticas dos resultados das simulações e as imprimimos.

## Resultado

1. **Lucro final médio:** Este valor indica o lucro médio obtido após o período de investimento, considerando todas as simulações realizadas. No contexto desta simulação, o lucro médio é de R$ X.XX.
2. **Desvio padrão do lucro final:** O desvio padrão mede o quanto os resultados variam em relação à média. Quanto maior o desvio padrão, maior a dispersão dos resultados em torno da média. Neste caso, o desvio padrão do lucro final é de R$ X.XX, indicando a volatilidade dos retornos do investimento.
3. **5º percentil do lucro final:** Este valor indica o lucro final abaixo do qual 5% das simulações caíram. Em outras palavras, é o pior cenário esperado com 95% de confiança. Neste caso, o 5º percentil do lucro final é de R$ X.XX.
4. **50º percentil do lucro final:** Este valor representa a mediana dos lucros finais. Metade das simulações resultou em um lucro final menor que esse valor, enquanto a outra metade resultou em um lucro final maior. Neste contexto, o 50º percentil do lucro final é de R$ X.XX.
5. **95º percentil do lucro final:** Este valor indica o lucro final abaixo do qual 95% das simulações caíram. Em outras palavras, é o melhor cenário esperado com 95% de confiança. Neste caso, o 95º percentil do lucro final é de R$ X.XX.

Essas estatísticas fornecem uma visão abrangente do potencial de retorno do investimento ao longo do tempo, considerando as simulações realizadas com os ativos escolhidos. Elas ajudam a entender o intervalo de resultados possíveis, a volatilidade do investimento e os cenários extremos esperados.
