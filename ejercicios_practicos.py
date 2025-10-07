# Ejercicios Prácticos: Expresiones Aritméticas

## 📝 Instrucciones

- Resuelve los ejercicios en orden
- Intenta predecir el resultado antes de ejecutar el código
- Verifica tus respuestas con Python
- Si te equivocas, analiza por qué

# 🟢 NIVEL 1: Básico (Precedencia Simple)

print("=== NIVEL 1: Básico ===")

### Ejercicio 1.1: Predice el Resultado
print("\n--- Ejercicio 1.1 ---")
print("5 + 3 * 2")
resultado_1_1 = 5 + 3 * 2
print(f"Tu predicción: 11")
print(f"Resultado real: {resultado_1_1}")
print(f"Explicación: Multiplicación primero (3 * 2 = 6), luego suma (5 + 6 = 11)")

### Ejercicio 1.2: Paréntesis
print("\n--- Ejercicio 1.2 ---")
print("(5 + 3) * 2")
resultado_1_2 = (5 + 3) * 2
print(f"Tu predicción: 16")
print(f"Resultado real: {resultado_1_2}")
print(f"Explicación: Paréntesis primero (5 + 3 = 8), luego multiplicación (8 * 2 = 16)")

### Ejercicio 1.3: División
print("\n--- Ejercicio 1.3 ---")
print("10 / 2")
print("10 // 2")
print("10 % 2")
resultado_1_3a = 10 / 2
resultado_1_3b = 10 // 2
resultado_1_3c = 10 % 2
print(f"Tus predicciones: 5.0, 5, 0")
print(f"Resultados reales: {resultado_1_3a}, {resultado_1_3b}, {resultado_1_3c}")
print(f"Explicación:")
print("- 10 / 2 = 5.0 (división normal, siempre float)")
print("- 10 // 2 = 5 (división entera)")
print("- 10 % 2 = 0 (resto, 10 es divisible por 2)")

### Ejercicio 1.4: Potencia
print("\n--- Ejercicio 1.4 ---")
print("2 ** 3")
print("2 ^ 3")
resultado_1_4a = 2 ** 3
resultado_1_4b = 2 ^ 3
print(f"Tus predicciones: 8, 1")
print(f"Resultados reales: {resultado_1_4a}, {resultado_1_4b}")
print(f"Explicación:")
print("- 2 ** 3 = 8 (potencia correcta: 2×2×2)")
print("- 2 ^ 3 = 1 (XOR bit a bit, NO potencia)")

### Ejercicio 1.5: Negación
print("\n--- Ejercicio 1.5 ---")
print("5 - -3")
print("-5 * -3")
resultado_1_5a = 5 - -3
resultado_1_5b = -5 * -3
print(f"Tus predicciones: 8, 15")
print(f"Resultados reales: {resultado_1_5a}, {resultado_1_5b}")
print(f"Explicación:")
print("- 5 - (-3) = 5 + 3 = 8 (restar negativo = sumar)")
print("- -5 * -3 = 15 (negativo × negativo = positivo)")

# 🟡 NIVEL 2: Intermedio (Expresiones Complejas)

print("\n\n=== NIVEL 2: Intermedio ===")

### Ejercicio 2.1: Múltiples Operadores
print("\n--- Ejercicio 2.1 ---")
print("2 + 3 * 4 - 5")
resultado_2_1 = 2 + 3 * 4 - 5
print(f"Tu predicción: 9")
print(f"Resultado real: {resultado_2_1}")
print(f"Paso a paso:")
print("1. 3 * 4 = 12 (multiplicación primero)")
print("2. 2 + 12 = 14 (suma)")
print("3. 14 - 5 = 9 (resta)")

### Ejercicio 2.2: División y Multiplicación
print("\n--- Ejercicio 2.2 ---")
print("20 / 4 * 2")
print("20 / (4 * 2)")
resultado_2_2a = 20 / 4 * 2
resultado_2_2b = 20 / (4 * 2)
print(f"Tus predicciones: 10.0, 2.5")
print(f"Resultados reales: {resultado_2_2a}, {resultado_2_2b}")
print(f"Explicación:")
print("- 20 / 4 * 2: Izquierda a derecha → (20/4)*2 = 5.0*2 = 10.0")
print("- 20 / (4 * 2): Paréntesis primero → 20/8 = 2.5")

### Ejercicio 2.3: Módulo en Expresión
print("\n--- Ejercicio 2.3 ---")
print("17 % 5 + 2 * 3")
resultado_2_3 = 17 % 5 + 2 * 3
print(f"Tu predicción: 8")
print(f"Resultado real: {resultado_2_3}")
print(f"Paso a paso:")
print("1. 17 % 5 = 2 (resto de 17÷5)")
print("2. 2 * 3 = 6 (multiplicación)")
print("3. 2 + 6 = 8 (suma)")

### Ejercicio 2.4: Potencias Anidadas
print("\n--- Ejercicio 2.4 ---")
print("2 ** 3 ** 2")
print("(2 ** 3) ** 2")
resultado_2_4a = 2 ** 3 ** 2
resultado_2_4b = (2 ** 3) ** 2
print(f"Tus predicciones: 512, 64")
print(f"Resultados reales: {resultado_2_4a}, {resultado_2_4b}")
print(f"Explicación:")
print("- 2 ** 3 ** 2: Derecha a izquierda → 2**(3**2) = 2**9 = 512")
print("- (2 ** 3) ** 2: Paréntesis primero → 8**2 = 64")

### Ejercicio 2.5: Expresión Compleja
print("\n--- Ejercicio 2.5 ---")
print("10 + 5 * 2 - 8 / 4 + 3")
resultado_2_5 = 10 + 5 * 2 - 8 / 4 + 3
print(f"Tu predicción: 21.0")
print(f"Resultado real: {resultado_2_5}")
print(f"Paso a paso:")
print("1. 5 * 2 = 10 (multiplicación)")
print("2. 8 / 4 = 2.0 (división)")
print("3. 10 + 10 = 20 (suma, izq a der)")
print("4. 20 - 2.0 = 18.0 (resta)")
print("5. 18.0 + 3 = 21.0 (suma)")

# 🔴 NIVEL 3: Avanzado (Problemas del Mundo Real)

print("\n\n=== NIVEL 3: Avanzado ===")

### Ejercicio 3.1: Cálculo de Impuestos
print("\n--- Ejercicio 3.1 ---")
price = 100
tax_rate = 0.15
total = price * (1 + tax_rate)
print(f"Calcula el total con impuesto del 15% sobre una compra de $100")
print(f"Precio: ${price}")
print(f"Tasa de impuesto: {tax_rate*100}%")
print(f"Total = precio * (1 + tasa_impuesto)")
print(f"Total = {price} * (1 + {tax_rate})")
print(f"Total = ${total}")

### Ejercicio 3.2: Conversión de Temperatura
print("\n--- Ejercicio 3.2 ---")
celsius = 25
fahrenheit = (celsius * 9 / 5) + 32
print(f"Convierte 25°C a Fahrenheit usando la fórmula: F = (C × 9/5) + 32")
print(f"F = ({celsius} × 9/5) + 32")
print(f"F = {fahrenheit}°F")

### Ejercicio 3.3: Promedio de Calificaciones
print("\n--- Ejercicio 3.3 ---")
grade1 = 85
grade2 = 90
grade3 = 78
average = (grade1 + grade2 + grade3) / 3
print(f"Calcula el promedio de 3 calificaciones: 85, 90, 78")
print(f"Promedio = (calificación1 + calificación2 + calificación3) / 3")
print(f"Promedio = ({grade1} + {grade2} + {grade3}) / 3")
print(f"Promedio = {average:.2f}")

### Ejercicio 3.4: Dividir Cuenta
print("\n--- Ejercicio 3.4 ---")
total_bill = 127.50
num_people = 4
per_person = total_bill / num_people
print(f"4 amigos van a cenar. La cuenta es $127.50. Calcula cuánto paga cada uno.")
print(f"Por persona = cuenta_total / número_personas")
print(f"Por persona = {total_bill} / {num_people}")
print(f"Por persona = ${per_person:.2f}")

### Ejercicio 3.5: Tiempo Restante
print("\n--- Ejercicio 3.5 ---")
total_minutes = 125
hours = total_minutes // 60
minutes = total_minutes % 60
print(f"Tienes 125 minutos. ¿Cuántas horas y minutos son?")
print(f"Horas = minutos_totales // 60")
print(f"Minutos = minutos_totales % 60")
print(f"Horas = {total_minutes} // 60 = {hours}")
print(f"Minutos = {total_minutes} % 60 = {minutes}")
print(f"Resultado: {hours} horas y {minutes} minutos")

# 📊 Ejercicios de Debugging

print("\n\n=== DEBUGGING ===")

### Debug 1: Encuentra el Error
print("\n--- Debug 1 ---")
print("Este código debería calcular el promedio")
a = 10
b = 20
c = 30
# Código incorrecto
average_incorrecto = a + b + c / 3
print(f"Código incorrecto: average = a + b + c / 3")
print(f"Resultado incorrecto: {average_incorrecto}")

# Código correcto
average_correcto = (a + b + c) / 3
print(f"Código correcto: average = (a + b + c) / 3")
print(f"Resultado correcto: {average_correcto}")
print(f"¿Qué está mal? Solo divide c por 3, no la suma total")

### Debug 2: Encuentra el Error
print("\n--- Debug 2 ---")
print("Calcular 20% de descuento sobre $50")
price = 50
discount = 20
# Código incorrecto
final_incorrecto = price - discount * price
print(f"Código incorrecto: final = price - discount * price")
print(f"Resultado incorrecto: ${final_incorrecto}")

# Código correcto
final_correcto = price * (1 - discount / 100)
print(f"Código correcto: final = price * (1 - discount / 100)")
print(f"Resultado correcto: ${final_correcto}")
print(f"¿Qué está mal? Multiplica descuento por precio (20 * 50 = 1000) en lugar de calcular el porcentaje")

# 🎯 PROYECTO FINAL: Calculadora de Expresiones

print("\n\n=== PROYECTO FINAL: Calculadora de Expresiones ===")

def calculadora_basica():
    """Calculadora básica de expresiones"""
    print("\n=== CALCULADORA BÁSICA ===")
    print("Operadores: +, -, *, /, //, %, **")
    print("Escribe 'salir' para terminar")
    
    while True:
        expression = input("\nIngresa una expresión: ")
        
        if expression.lower() == 'salir':
            print("¡Hasta luego!")
            break
        
        try:
            result = eval(expression)
            print(f"Resultado: {result}")
            print(f"Tipo: {type(result).__name__}")
        except ZeroDivisionError:
            print("❌ Error: División por cero")
        except:
            print("❌ Error: Expresión inválida")

def calculadora_avanzada():
    """Calculadora avanzada con historial"""
    print("\n=== CALCULADORA AVANZADA ===")
    print("Operadores: +, -, *, /, //, %, **")
    print("Comandos: 'salir', 'historial'")
    
    history = []
    
    while True:
        expression = input("\nIngresa una expresión o comando: ").strip()
        
        if expression.lower() == 'salir':
            print("¡Gracias por usar la calculadora!")
            break
        
        if expression.lower() == 'historial':
            if history:
                print("\n=== HISTORIAL ===")
                for i, (expr, res) in enumerate(history, 1):
                    print(f"{i}. {expr} = {res}")
            else:
                print("\nNo hay historial aún.")
            continue
        
        if not expression:
            continue
        
        try:
            print(f"\nEvaluando: {expression}")
            print("-" * 30)
            
            result = eval(expression)
            
            print(f"Resultado: {result}")
            print(f"Tipo: {type(result).__name__}")
            
            if isinstance(result, float) and result.is_integer():
                print(f"Nota: El resultado es un número entero: {int(result)}")
            
            history.append((expression, result))
            
        except ZeroDivisionError:
            print("❌ Error: División por cero")
        except SyntaxError:
            print("❌ Error: Sintaxis inválida")
        except NameError:
            print("❌ Error: Variable no definida")
        except Exception as e:
            print(f"❌ Error: {e}")

# Ejecutar el programa principal
if __name__ == "__main__":
    print("=" * 60)
    print("EJERCICIOS PRÁCTICOS: EXPRESIONES ARITMÉTICAS")
    print("=" * 60)
    
    # Preguntar si quieren ejecutar las calculadoras
    input("\nPresiona Enter para ver los resultados de todos los ejercicios...")
    
    # Las calculadoras se ejecutan después de mostrar todos los resultados
    print("\n" + "=" * 60)
    print("¿Quieres probar las calculadoras?")
    print("1. Calculadora Básica")
    print("2. Calculadora Avanzada")
    print("3. Salir")
    
    while True:
        opcion = input("\nElige una opción (1-3): ")
        if opcion == '1':
            calculadora_basica()
        elif opcion == '2':
            calculadora_avanzada()
        elif opcion == '3':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Elige 1, 2 o 3.")

print("\n" + "=" * 60)
print("¡Todos los ejercicios completados! 🎉")
print("=" * 60)