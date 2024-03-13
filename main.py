import numpy as np
import pandas as pd
import yfinance as yf


class InvestmentSimulator:
    def __init__(self, assets, investment_amount: float, simulations: int, time_horizon: int):
        """
        Classe para simulação de investimento.

        Args:
            assets (list): Lista de símbolos dos ativos a serem simulados.
            investment_amount (float, opcional): Valor inicial do investimento. O padrão é 5000.
            simulations (int, opcional): Número de simulações a serem executadas. O padrão é 10000.
            time_horizon (int, opcional): Horizonte de tempo em meses para a simulação. O padrão é 5 * 12.
        """
        self.assets = [asset + ".SA" for asset in assets]  # Adiciona ".SA" aos símbolos dos ativos
        self.investment_amount = investment_amount  # Valor inicial do investimento
        self.simulations = simulations  # Número de simulações
        self.time_horizon = time_horizon * 12  # Horizonte de tempo em meses
        self._fetch_data()  # Método privado para baixar os dados
        self._calculate_monthly_returns()  # Método privado para calcular os retornos mensais
        self._simulate_investment()  # Método privado para simular o investimento

    def _fetch_data(self):
        """Baixa os dados dos ativos utilizando a biblioteca yfinance."""
        data = yf.download(self.assets, period='5y', interval='1d')["Adj Close"]
        self.data = data

    def _calculate_monthly_returns(self):
        """Calcula os retornos mensais dos ativos."""
        monthly_returns = self.data.resample('M').ffill().pct_change().dropna()
        self.monthly_returns = monthly_returns

    def _simulate_investment(self):
        """Realiza a simulação de investimento."""
        results = np.zeros((self.simulations, self.time_horizon))
        for i in range(self.simulations):
            current_investment = self.investment_amount
            for j in range(self.time_horizon):
                monthly_return = np.random.choice(self.monthly_returns.iloc[:, np.random.choice(self.monthly_returns.shape[1])])
                current_investment *= (1 + monthly_return)
                results[i, j] = current_investment
        self.results = results

    def calculate_statistics(self):
        """Calcula estatísticas sobre os resultados das simulações."""
        final_profit = self.results[:, -1]
        mean_profit = np.mean(final_profit)
        std_deviation = np.std(final_profit)
        percentile_5 = np.percentile(final_profit, 5)
        percentile_50 = np.percentile(final_profit, 50)
        percentile_95 = np.percentile(final_profit, 95)
        return mean_profit, std_deviation, percentile_5, percentile_50, percentile_95


if __name__ == "__main__":
    assets = ['PETR4', 'WEGE3', 'LEVE3', 'BBDC4']
    # Cria uma instância do simulador de investimento
    simulator = InvestmentSimulator(assets, investment_amount=1000.0, simulations=10000, time_horizon=10)
    # Calcula as estatísticas dos resultados das simulações
    mean_profit, std_deviation, percentile_5, percentile_50, percentile_95 = simulator.calculate_statistics()
    # Imprime as estatísticas
    # Impressão das estatísticas do lucro final
    print(f"Lucro final médio: R$ {mean_profit:.2f}")               # Média do lucro final
    print(f"Desvio padrão do lucro final: R$ {std_deviation:.2f}")  # Volatilidade do lucro final
    print(f"5º percentil do lucro final: R$ {percentile_5:.2f}")    # Menor lucro final em 5% das simulações
    print(f"50º percentil do lucro final: R$ {percentile_50:.2f}")  # Lucro final mediano (metade das simulações acima e metade abaixo)
    print(f"95º percentil do lucro final: R$ {percentile_95:.2f}")  # Maior lucro final em 95% das simulações
