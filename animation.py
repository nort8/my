import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Настройка графика
fig, ax = plt.subplots()
ax.set_xlim(0, 2 * np.pi)
ax.set_ylim(-1.5, 1.5)
ax.grid(True)
ax.set_title("Движущаяся точка по синусоиде")

# Создаём данные для синусоиды (она будет статичной)
x = np.linspace(0, 2 * np.pi, 200)
y = np.sin(x)
line, = ax.plot(x, y, 'b-', linewidth=2)   # синяя кривая

# Точка, которую будем двигать
point, = ax.plot([], [], 'ro', markersize=10)   # красная точка

# Текст с координатами
coord_text = ax.text(0.5, 1.2, '', transform=ax.transAxes, fontsize=12, color='red')

# Функция инициализации (запускается один раз)
def init():
    point.set_data([], [])
    coord_text.set_text('')
    return point, coord_text

# Функция обновления для каждого кадра
def update(frame):
    # frame — номер кадра
    x_pos = frame * 0.1                # шаг движения
    if x_pos > 2 * np.pi:
        x_pos = 0                      # зацикливание
    y_pos = np.sin(x_pos)
    point.set_data([x_pos], [y_pos])
    coord_text.set_text(f'x = {x_pos:.2f}, y = {y_pos:.2f}')
    return point, coord_text

# Создаём анимацию: 200 кадров, интервал 50 мс (20 кадров/сек)
ani = animation.FuncAnimation(fig, update, frames=200,
                              init_func=init, interval=50, blit=True)

# Показываем анимацию (откроется окно)
plt.show()

# Если хотите сохранить в GIF, раскомментируйте строку ниже:
# ani.save('sine_wave.gif', writer='pillow', fps=20)
