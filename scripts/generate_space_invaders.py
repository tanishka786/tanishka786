import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pygame
import os

# Initialize pygame for sounds
pygame.mixer.init()
shoot_sound = pygame.mixer.Sound("sounds/shoot.wav")
explode_sound = pygame.mixer.Sound("sounds/explode.wav")

# Ensure required folders exist
os.makedirs("dist", exist_ok=True)
os.makedirs("sounds", exist_ok=True)

# Generate a blue gradient background
def generate_gradient(ax):
    gradient = np.linspace(0.2, 0.8, 256).reshape(1, -1)  # Blue gradient
    ax.imshow(gradient, extent=[0, 52, -7, 1], aspect='auto', cmap="Blues")

# Generate random GitHub contributions (1 = Alien, 0 = Empty)
def fetch_contributions():
    return np.random.randint(0, 2, (7, 52))  # 7 days x 52 weeks (1 year)

# Create the Space Invaders animation
def create_space_invaders_animation(contributions):
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.set_xticks([])
    ax.set_yticks([])

    spaceship_color = "#C0C0C0"  # Silver
    spaceship_outline = "black"
    invader_colors = ["#FF4500", "#FF1493", "#00FF00", "#FFD700"]  # Vibrant Aliens
    bullet_color = "#FFFF00"  # Yellow Bullet

    def update(frame):
        ax.clear()
        ax.set_xticks([])
        ax.set_yticks([])
        generate_gradient(ax)

        # Draw aliens (GitHub contributions)
        for i in range(7):
            for j in range(52):
                if contributions[i, j] == 1:
                    color = np.random.choice(invader_colors)  # Random vibrant alien
                    ax.plot(j, -i, "o", color=color, markersize=10)

        # Draw spaceship
        ship_x = frame % 52
        ship_y = -7.5
        ax.scatter(ship_x, ship_y, s=400, color=spaceship_color, edgecolors=spaceship_outline, linewidth=2)

        # Draw bullet (shooting upwards)
        bullet_x = ship_x
        bullet_y = -np.random.randint(0, 7)  # Random height
        ax.plot(bullet_x, bullet_y, "|", color=bullet_color, markersize=8)

        # Play shoot sound every few frames
        if frame % 5 == 0:
            shoot_sound.play()

        # Play explosion sound when bullet hits an alien
        if contributions[bullet_y, bullet_x] == 1:
            explode_sound.play()

    ani = animation.FuncAnimation(fig, update, frames=52, interval=200)
    ani.save("dist/github-space-invaders.gif", writer="pillow", fps=10)

def main():
    contributions = fetch_contributions()
    create_space_invaders_animation(contributions)
    print("Space Invaders animation generated successfully!")

if __name__ == "__main__":
    main()
