casa = int(input('escreva o valor da casa que voce quer comprar'))
salario = int(input('escreva o valor do seu salario'))
anos = int(input('em quantos anos voce quer pagar essa casa?'))
mensalidade = casa / (anos * 12)
salarioporcent = salario / 100 * 30
if mensalidade > salarioporcent:
    print('a sua mensalidade a pagar é R${:.2f}, e como 30% do seu salário é de R${:.2f}, nao podemos fazer o emprestimo'.format(mensalidade, salarioporcent))
elif mensalidade <= salarioporcent:
    print('a sua mensalidade a pagar é R${:.2f}, e como 30% do seu salário é de R${:.2f}, podemos fazer o emprestimo'.format(mensalidade, salarioporcent))
