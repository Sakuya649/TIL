import numpy as np
import matplotlib.pyplot as plt

def dft(x):
    '''
    DFTの実装
    引数：入力信号の離散時間領域の値を持つ1次元のNumPy配列
    戻り値：離散周波数領域の値をもつ1次元のNumPy配列
    '''

    N = len(x)
    X = np.zeros(N, dtype=complex)
    
    # DFTの計算
    for i in range(N):
        for k in range(N):
            X[i] += x[k] * np.exp(-2j * np.pi * i * k / N)
    return X

if __name__ == '__main__':
    # テストデータの生成
    x = np.array([1.0, 2.0, 3.0, 4.0])
    # ライブラリを使用した時の結果
    print(np.fft.fft(x))

    # 実装したDFTの結果
    print(dft(x))
