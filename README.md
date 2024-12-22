# AI Building AI: Simple Tic-Tac-Toe AI

A minimalistic implementation of a Tic-Tac-Toe AI, all code written by ChatGPT. This project showcases how an AI can be used to build another AI to play the classic Tic-Tac-Toe game. Built using Flask for the backend, it provides a lightweight and intuitive experience for users.

## Features
- **AI vs. Player**: Challenge the AI to a game of Tic-Tac-Toe.
- **Flask Backend**: Simple and fast backend setup.
- **Interactive Gameplay**: Engage with the game in real-time through the browser.

## Getting Started

### Prerequisites
- Python 3.7+
- Flask

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/benlaval23/aibuildingai.git
   cd aibuildingai
   ```

2. Set up a virtual environment (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Flask app:
   ```bash
   flask run
   ```

5. Open your browser and go to `http://127.0.0.1:5000/` to start playing!

## How It Works
- The AI uses simple game logic combined with decision-making strategies to play Tic-Tac-Toe efficiently.
- The backend processes player moves and returns the AI's response in real-time.
