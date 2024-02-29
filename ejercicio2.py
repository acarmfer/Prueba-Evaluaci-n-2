class TextFormatter:
    def __init__(self, texto_bruto):
        self.texto_bruto = texto_bruto

    def format_text(self):
        texto_formateado = '.\n'.join(oracion.capitalize() for oracion in self.texto_bruto.split('#')) + '.'
        return texto_formateado

def main():
    texto_bruto = "un día que el viento soplaba con fuerza#mira como se mueve aquella banderola -dijo un monje#lo que se mueve es el viento -respondió otro monje#ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro"

    formatter = TextFormatter(texto_bruto)
    texto_formateado = formatter.format_text()
    print(texto_formateado)
