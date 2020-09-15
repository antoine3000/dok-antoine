---
title: Pomodoro code
---

# How I want to use my pomodoro

- Press the left button to start the timer
- If it's running, press the left button to pause the timer
- If it's paused, press the left button to resume the timer
- If it's paused, press the right button to stop the timer
- When it's running, the LEDs light up one by one until the time limit
- When it's running and it's a work period, LEDs are red
- When it's running and it's a break period, LEDs are green
- When it's paused, all the LEDs are light up and blue

<video><source src="pomo-playground.mp4"></video>

# The code that does this

For this software I am using the Arduino framework. This framework, like any other framework, is a collection of shortcuts that aims to make the programmer's life easier. At the end of the day, the code you write using a framework is compiled into its original language, which is, in this case, C ++.

<pre>
bool button_left;
bool button_right;
bool is_active = false;
bool is_paused = false;
int counter = 0;
int steps = 10;
int pomo = 30 * 600;
int pomo_work = pomo / 6 * 5;
int pomo_break = pomo / 6 * 1;

void setup() {
  CircuitPlayground.begin();
}

void on_second(int counter) {
  CircuitPlayground.clearPixels();
  if (counter <= pomo_work) {
    // work
    for (int i = 0; i <= steps; i++) {
      if (counter > pomo_work / steps * i) {
        CircuitPlayground.setPixelColor(i, 255,   0,   0);
      }
    }
  } else if (counter > pomo_work && counter <= pomo) {
    // break
    for (int i = 0; i <= steps; i++) {
      if (counter - pomo_work > pomo_break / steps * i) {
        CircuitPlayground.setPixelColor(i, 0,   255,   0);
      }
    }
  }
}

void bip() {
  CircuitPlayground.playTone(200, 10);
}

void loop() {
  button_left = CircuitPlayground.leftButton();
  button_right = CircuitPlayground.rightButton();

  if (counter > pomo) {
    CircuitPlayground.clearPixels();
    counter = 0;
  }

  if (button_left) {
    CircuitPlayground.clearPixels();
    if (!is_active) {
      is_active = true;
      bip();
    } else if (is_active && !is_paused) {
      is_paused = true;
      bip();
    } else if (is_paused) {
      is_paused = false;
      bip();
    }
  }

  if (button_right) {
    if (is_active && is_paused) {
      is_active = false;
      is_paused = false;
      counter = 0;
      CircuitPlayground.clearPixels();
      bip();
    }
  }

  if (is_active && !is_paused) {
    counter = counter + 1;
  }

  if (is_paused) {
    for (int i = 0; i <= steps; i++) {
      CircuitPlayground.setPixelColor(i, 0,   0,   55);
    }
  }

  if (counter % 10 == 0) {
    on_second(counter);
  }

  delay(100);
}
</pre>