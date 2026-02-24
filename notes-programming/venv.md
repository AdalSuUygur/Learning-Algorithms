# venv (Virtual Environment)

> **Definition:** Python projelerinde bağımlılıkları (dependencies) izole etmek için kullanılan, her proje için özel bir "Python Kutusu" oluşturan standart araçtır.

* **Concept:** Bu izole kutunun içinde iki temel bileşen bulunur:

1. Proje için özel **Python Interpreter** (Yorumlayıcı).
2. Projeye özgü kurulan **Libraries/Packages** (Kütüphaneler).

## Why Use `venv`? (The Conflict Problem)

`venv` kullanımının temel amacı **Dependency Conflicts** (Bağımlılık Çakışmaları) sorununu önlemektir.

* **Scenario (The Problem):**
* **Project A:** `Django v2.0` gerektiriyor.
* **Project B:** `Django v4.0` gerektiriyor.
* *Result:* Bu kütüphaneler genel sistem (Global Python) üzerine kurulursa, aynı anda var olamazlar. Bir proje çalışırken diğeri hata verir.

* **Solution:** `venv` her proje için izole bir ortam yaratır. Proje A sadece v2.0'ı, Proje B sadece v4.0'ı görür. Projeler birbirini etkilemez.

## How to Use `venv` (Process)

Sanal ortam kullanımı 3 temel adımdan oluşur:

### 1. Creation (Ortam Oluşturma)

Proje klasörü içinde `venv` adında bir alt klasör oluşturur.

* **Command (Windows/PowerShell):**
`python3 -m venv venv`

### 2. Activation (Ortamı Aktifleştirme)

Terminalin genel sistem Python'ı yerine, oluşturulan sanal klasördeki Python'ı ve `pip`'i kullanmasını sağlar.

* **Command (Windows/PowerShell):**
`venv\Scripts\activate`

> **Note:** Başarılı aktivasyon sonrası terminal satırının başında `(venv)` ibaresi belirir.

### 3. Installation & Deactivation (Kurulum ve Çıkış)

Ortam aktifken (`(venv)` ibaresi varken) yapılan yüklemeler sadece o projeye özgüdür.

* **Install:** `pip install requests` (Sadece sanal ortama kurulur).
* **Exit:** İş bitince çıkmak için `deactivate` komutu kullanılır.
