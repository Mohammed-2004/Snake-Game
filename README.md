# 🐍 Smart Snake Game (AI-Powered)

A classic **Snake Game** rebuilt using **Python** and **Pygame**, but powered by an **AI (A\* Pathfinding Algorithm)** to automatically and intelligently guide the snake to the food!

---

## 📚 Project Description

This project demonstrates a smart snake that autonomously plays the classic snake game by calculating the optimal path to the food while avoiding collisions with itself and randomly generated walls. The snake dynamically grows in size, increases speed over time, and reacts in real-time to the changing game environment.

---

## 🧠 AI Algorithm

- **A\* (A-star) Search Algorithm**  
  The AI uses A\* search to find the shortest safe path to the food, considering:
  - Snake’s current body
  - Wall obstacles
  - Grid boundaries
  
The heuristic used is the **Manhattan Distance** for efficient navigation.

---

## 🎮 Gameplay Features

- Automatic snake movement driven by AI.
- Randomly generated walls as dynamic obstacles.
- Speed increases as the snake eats more food.
- Sound effects for eating and game over.
- Colorful GUI with growing snake animations.
- Game Over screen and clean exit handling.

---

## 💻 Project Type

- **Type**: Desktop Application
- **Platform**: Windows, Linux, MacOS

---

## 🛠️ Technologies Used

- **Python 3.x**
- **Pygame** (for graphics, sounds, and input handling)
- **Heapq** (for AI's priority queue)
- **Random** (to generate food and wall positions)
- **Sys** (for system exit and event handling)

---

## 🎨 Game Design

| Element    | Color  |
|------------|--------|
| Snake Head | Green  |
| Snake Body | Light Green |
| Food       | Red   |
| Walls      | Gray   |
| Background | Black  |

---

## 🚀 How to Run

1. **Install Python 3.x** on your system.
2. **Install required library**:
   ```bash
   pip install pygame

---

## 🎯 How to Play

- The snake automatically moves toward the food using the AI.
- You don't need to control the snake manually.
- The goal is to **eat as much food as possible** without crashing into walls or the snake's own body.
- Each time the snake eats food:
  - The snake grows longer.
  - The speed slightly increases.
  - A sound effect plays (`eat.wav`).
- If the snake collides with itself or a wall:
  - The game ends.
  - A game over sound (`gameover.wav`) is played.
- You can exit the game at any time by closing the game window.

---
