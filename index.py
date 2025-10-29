import numpy as np
import matplotlib.pyplot as plt

#Datos

ph_values = [
2.70, 3.00, 3.31, 3.62, 3.96, 4.23, 4.52, 4.84, 5.15, 5.48, 5.81, 6.19, 6.92, 9.74, 11.17, 11.59, 11.79, 11.87, 11.96, 12.03, 12.10, 12.15, 12.20, 12.21, 12.26, 
12.28, 12.30, 12.32, 12.34, 12.36, 12.37, 12.38, 12.39, 12.41, 12.41, 12.42, 12.42, 12.43, 12.44, 12.45,12.45, 12.46, 12.46, 12.47, 12.48, 12.48, 12.49, 12.49, 12.49, 12.51 
]
increment = 0.5

volumes = [i * increment for i in range(len(ph_values))]

#numpy arrays
volumes_np = np.array(volumes)
ph_values_np = np.array(ph_values)

#derivada (pendiente)
dpH_dV = np.gradient(ph_values_np, increment)

# Buscamos el índice del máximo de la derivada
idx_equiv = np.argmax(dpH_dV)
volume_equiv = volumes[idx_equiv]
ph_equiv = ph_values[idx_equiv]

print(f"Punto equivalente aproximado: Volumen = {volume_equiv} , pH = {ph_equiv}")
print(f"Máxima pendiente (derivada) = {dpH_dV[idx_equiv]}, lista de pendientes = {dpH_dV}")
# Grafica de la curva y punto equivalente
plt.plot(volumes, ph_values, marker='o', label='Curva pH')
plt.plot(volume_equiv, ph_equiv, 'ro', label='Punto equivalente')
plt.xlabel('Volumen de descarte')
plt.ylabel('pH')
plt.title('Curva de titulación y punto equivalente')
plt.legend()
plt.grid(True)
plt.show()

#pthon index.py