# testes/teste_registro.py
# Testes das operações de registro diário

import os
import unittest

from banco import Banco
from modelos.registro import Registro
from modelos.usuario import Usuario


class TestRegistro(unittest.TestCase):

    def setUp(self):
        self.banco = Banco("teste_registro.db")

        self.banco.criar_tabelas_usuarios()
        self.banco.criar_tabelas_registros()

        usuario = Usuario("Teste", "teste@email.com", "Senha123")
        self.banco.cadastrar_usuario(usuario)

        self.id_usuario = self.banco.consultar_usuario_email(
            "teste@email.com"
        )[0]

    def tearDown(self):
        if os.path.exists("teste_registro.db"):
            os.remove("teste_registro.db")

    def test_cadastrar_e_listar_registro(self):

        registro = Registro(
            self.id_usuario,
            "25/11/2026",
            "Dia estável.",
        )

        self.assertTrue(self.banco.cadastrar_registro(registro))

        registros = self.banco.listar_registros(self.id_usuario)

        self.assertEqual(len(registros), 1)
        self.assertEqual(registros[0][3], "Dia estável.")

    def test_deletar_registro(self):

        registro = Registro(
            self.id_usuario,
            "25/11/2026",
            "Registro para excluir.",
        )

        self.banco.cadastrar_registro(registro)

        id_registro = self.banco.listar_registros(
            self.id_usuario
        )[0][0]

        self.assertTrue(
            self.banco.deletar_registro(id_registro, self.id_usuario)
        )

        registros = self.banco.listar_registros(self.id_usuario)

        self.assertEqual(len(registros), 0)


if __name__ == "__main__":
    unittest.main()