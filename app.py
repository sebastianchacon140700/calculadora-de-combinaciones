from flask import Flask, render_template, request
import math

app = Flask(__name__,
static_folder='estilos')

# Fórmulas
def combinaciones_sin_repeticion(n, r):
    return math.comb(n, r)

def combinaciones_con_repeticion(n, r):
    return math.comb(n + r - 1, r)

def variaciones_sin_repeticion(n, r):
    return math.perm(n, r)

def variaciones_con_repeticion(n, r):
    return n ** r

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    error = None
    formula = ""

    if request.method == 'POST':
        try:
            n = int(request.form['n'])
            r = int(request.form['r'])
            tipo = request.form['tipo']

            if n < 0 or r < 0:
                error = "Solo se permiten números enteros positivos."
            elif tipo in ['comb_sin', 'var_sin'] and r > n:
                error = f"En { 'combinaciones' if tipo == 'comb_sin' else 'variaciones' } sin repetición, r no puede ser mayor que n."
            else:
                if tipo == 'comb_sin':
                    resultado = combinaciones_sin_repeticion(n, r)
                    formula = "C(n, r) = n! / (r! * (n - r)!)"
                elif tipo == 'comb_con':
                    resultado = combinaciones_con_repeticion(n, r)
                    formula = "C(n + r - 1, r) = (n + r - 1)! / (r! * (n - 1)!)"
                elif tipo == 'var_sin':
                    resultado = variaciones_sin_repeticion(n, r)
                    formula = "V(n, r) = n! / (n - r)!"
                elif tipo == 'var_con':
                    resultado = variaciones_con_repeticion(n, r)
                    formula = "V(n, r) = n^r"
        except ValueError:
            error = "Debe ingresar solo números enteros."

    return render_template('index.html', resultado=resultado, formula=formula, error=error)

if __name__ == '__main__':
    app.run(debug=True)

