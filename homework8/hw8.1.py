import numpy as np
import matplotlib.pyplot as plt

def make_sine_wave(x, A, w):
    return A * np.sin(w * x)

def main():
    x = np.linspace(0, 2*np.pi, 1000)
    
    amplitudes = np.array([0.5, 1, 1.5, 2, 2.5])
    frequencies = np.array([1, 2, 3, 4, 5])
    
    plt.figure(figsize=(12, 8))
    
    for A, w in zip(amplitudes, frequencies):
        y = make_sine_wave(x, A, w)
        
        plt.plot(x, y, label=f'A={A}, w={w}')
    
    plt.title('Sine Waves')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    
    plt.show()

if __name__ == "__main__":
    main()
