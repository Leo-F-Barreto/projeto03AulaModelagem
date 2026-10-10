class ContaBancaria:
    def __init__(self, saldo_inicial: float = 0.0):
        self.saldo_corrente = saldo_inicial
        self.saldo_poupanca = 0.0  # Nova funcionalidade

    def depositar(self, valor: float):
        if valor <= 0:
            raise ValueError("Valor de depósito inválido")
        self.saldo_corrente += valor

    def sacar(self, valor: float):
        if valor <= 0:
            raise ValueError("Valor de saque inválido")
        if valor > self.saldo_corrente:
            raise ValueError("Saldo insuficiente na conta corrente")
        self.saldo_corrente -= valor

    # --- Nova Funcionalidade: Investimento em Poupança ---
    
    def investir_poupanca(self, valor: float):
        """Transfere valor da conta corrente para a poupança."""
        if valor <= 0:
            raise ValueError("Valor de investimento inválido")
        if valor > self.saldo_corrente:
            raise ValueError("Saldo insuficiente na conta corrente para investir")
        
        self.saldo_corrente -= valor
        self.saldo_poupanca += valor

    def resgatar_poupanca(self, valor: float):
        """Resgata valor da poupança de volta para a conta corrente."""
        if valor <= 0:
            raise ValueError("Valor de resgate inválido")
        if valor > self.saldo_poupanca:
            raise ValueError("Saldo insuficiente na poupança")
        
        self.saldo_poupanca -= valor
        self.saldo_corrente += valor
