## Requisitos Funcionais
* **RF-01 (Event-Driven):** WHEN o usuário calcular o frete e o carrinho atingir o limite regional, THE SYSTEM SHALL zerar o frete.
* **RF-02 (Ubiquitous):** THE SYSTEM SHALL responder 90% resquisições em menos de 2s.
* **RF-03 (Event-Driven):** WHEN o usuário aplicar o cupom 'PROMO10', THE SYSTEM SHALL aplicar 10% sobre o valor total do carrinho.

## Regras de Negócio e Exceções
* **RB-01 (Ubiquitous)**: THE SYSTEM SHALL calcular o valor total adicionando a taxa de frete padrão de R$ 15,00 ao subtotal do carrinho.
* **RB-02 (Event-Driven):** WHEN a região de entrega for "Norte" ou "Nordeste", THE SYSTEM SHALL adicionar uma taxa adicional de R$ 10,00 sobre a taxa base de frete.
* **RB-03 (Unwanted Behavior)**: IF a região de entrega for diferente de "Norte" e "Nordeste" AND o subtotal do carrinho for maior ou igual a R$ 250,00, THEN THE SYSTEM SHALL conceder frete grátis (taxa = R$ 0,00)
* **RB-04 (Unwanted Behavior):** IF valor <= 0, THEN exibir erro 'Valor de carrinho inválido'.
* **RB-05 (Unwanted Behavior)**: IF a região de entrega for "Norte" ou "Nordeste" AND o subtotal do carrinho for superior a R$ 300,00, THEN THE SYSTEM SHALL conceder frete grátis (taxa = R$ 0,00).