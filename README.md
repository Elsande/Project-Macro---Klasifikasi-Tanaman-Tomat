# Macro-Project-IL

## Pengenalan
Proyek Macro-Project-IL merupakan bagian dari studi independen Infinite Learning 2024, yang bertujuan untuk mengembangkan model klasifikasi gambar menggunakan TensorFlow dan TensorFlow Hub. Proyek ini menggunakan model ResNet-v2 yang telah terlatih sebelumnya untuk mengklasifikasikan gambar ke dalam berbagai kategori.

## Tim

| Nama           | Role                | GitHub Link                           |
|----------------|---------------------|---------------------------------------|
| Dheo Putranta Pandia   | ML Engineer      | [dheepss123](https://github.com/dheepss123)   |
| Iffo Elsande Pratama Putra   | Data Engineer      | [Elsande](https://github.com/Elsande)   |
| Iqbal Maulana   | Data Engineer | [IqbalMaulana7](https://github.com/IqbalMaulana7) |
| Rizky Hardian  | ML OPS   | [RizkyHardian](https://github.com/RizkyHardian)  |
| Yumna Ilahi      | Design Reasercher  | [Yumnailahi04](https://github.com/Yumnailahi04)         |

## Cara Penggunaan
Untuk menggunakan proyek ini, ikuti langkah-langkah berikut:

1. **Persiapan Lingkungan**: Pastikan Anda memiliki Python dan TensorFlow terinstal. Proyek ini membutuhkan TensorFlow versi 2.x.

2. **Kloning Repositori**: Klon repositori ini menggunakan git:
    ```bash
    git clone <[url-repositori](https://github.com/dheepss123/Macro-Project-IL.git)>
    ```
4. **Menjalankan Notebook**: Buka notebook `Project_Notebook.ipynb` menggunakan Jupyter Notebook atau Google Colab dan jalankan semua sel.

5. **Pelatihan Model**: Ikuti instruksi dalam notebook untuk melatih model klasifikasi gambar.

## Model
Model yang digunakan dalam proyek ini adalah ResNet-v2 yang telah terlatih sebelumnya, diakses melalui TensorFlow Hub. Model ini merupakan salah satu model klasifikasi gambar yang paling populer dan efektif, yang mampu mengidentifikasi berbagai kategori gambar dengan akurasi tinggi.

URL Model TensorFlow Hub: `https://tfhub.dev/google/imagenet/resnet_v2_50/classification/4`

## Konfigurasi
Proyek ini menggunakan beberapa callback TensorFlow untuk meningkatkan proses pelatihan, termasuk `ModelCheckpoint` untuk menyimpan model terbaik, `EarlyStopping` untuk menghentikan pelatihan ketika tidak ada peningkatan, dan `ReduceLROnPlateau` untuk menyesuaikan learning rate.

## Visualisasi
Proyek ini menyediakan visualisasi akurasi dan loss selama pelatihan, memungkinkan pengguna untuk memantau kinerja model secara real-time.

## Kontribusi
Kami menyambut kontribusi dari komunitas! Jika Anda ingin berkontribusi pada proyek ini, silakan fork repositori ini dan kirimkan pull request Anda.
