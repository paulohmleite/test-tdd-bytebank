from datetime import date

class Funcionario:
    def __init__(self, nome, data_nascimento, salario):
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._salario = salario

    @property
    def nome(self):
        return self._nome

    @property
    def salario(self):
        return self._salario

    def idade(self):
        data_nascimento_quebrada = self._data_nascimento.split('/')
        ano_nascimento = data_nascimento_quebrada[-1]
        ano_atual = date.today().year
        return ano_atual - int(ano_nascimento)

    def lastname(self):
        full_name = self.nome.strip()
        broken_name = full_name.split(' ')
        return broken_name[-1]

    def _is_partner(self):
        last_names = ['Bragança', 'Windsor', 'Bourbon', 'Yamata', 'Al Saud', 'Tudor', 'Ptolomeu']
        return (self._salario >= 100000 and (self.lastname() in last_names))


    def decrease_salary(self):
        if self._is_partner():
            decrease = self._salario * 0.1
            self._salario -= decrease

    def calculate_bonus(self):
        valor = self._salario * 0.1
        if valor > 1000:
            raise Exception('The salary is too high to get a bonus!')
        return valor

    def __str__(self):
        return f'Funcionario({self._nome}, {self._data_nascimento}, {self._salario})'