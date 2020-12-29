class VerificandoNumero:

    @staticmethod
    def eh_numero(x):
        numero = x.replace('.','').replace(',','',1)
        return numero.isdigit()

    @staticmethod
    def eh_opcao(y):
        if VerificandoNumero.eh_numero(y):
            for i in [1,2,3,4,5]:
                if int(y) == int(i):
                    return True
        return False