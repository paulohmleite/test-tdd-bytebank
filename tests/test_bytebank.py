

from codigo.bytebank import Funcionario
import pytest
from pytest import mark


class TestClass:
    def test_quando_idade_recebe_13_03_2000_deve_retornar_22(self):
        # Given-Contexto
        entrada = '13/03/2000' 
        esperado = 22

        funcionario_teste = Funcionario('Teste', entrada, 1111)

        # When-ação
        resultado = funcionario_teste.idade()

        # Then-desfecho
        assert resultado == esperado

    def test_quando_sobrenome_recebe_Lucas_Carvalho_deve_retornar_Carvalho(self):
        # given
        input = ' Lucas Carvalho '
        expected = 'Carvalho'

        # when
        lucas = Funcionario(input, '11/11/2000', 1200)

        #then
        result = lucas.lastname()

        assert result == expected


    # @mark.skip
    def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
        input_salary = 100000
        input_name = 'Paulo Bragança'
        expected = 90000

        test_func = Funcionario(input_name, '11/11/2000', input_salary)

        test_func.decrease_salary()
        result = test_func.salario
        
        assert result == expected

    @mark.calculate_bonus
    def test_when_calculate_bonus_receive_1000_must_return_100(self):
        input_salary = 1000
        expected = 100


        test_func = Funcionario('Test', '11/11/2000', input_salary)
        result = test_func.calculate_bonus()
        
        assert result == expected

    @mark.calculate_bonus
    def test_when_calculate_bonus_receive_1000000_must_return_exception(self):
        with pytest.raises(Exception):
            input_salary = 1000000

            test_func = Funcionario('Test', '11/11/2000', input_salary)
            result = test_func.calculate_bonus()
            
            assert result


    def test_retorno_str(self):
        input_name, input_birth_date, input_salary = 'Teste', '12/03/2000', 1000
        expected = 'Funcionario(Teste, 12/03/2000, 1000)'

        test_func = Funcionario(input_name, input_birth_date, input_salary, )
        result = test_func.__str__()

        return result == expected


