# Git/GitHub Kullanımı

## 1. Kurulum (Installation)

Öncelikle bilgisayarında Git'in yüklü olup olmadığını kontrol edelim.\
Terminalini (Windows'ta PowerShell veya CMD, Mac/Linux'ta Terminal) aç ve şunu yaz:

```bash
git --version
```

Eğer bir sürüm numarası görüyorsan (örneğin `git version 2.40.0`), kuruludur.\
Hata alıyorsan:

* **Windows:** [git-scm.com](https://git-scm.com/) adresinden indirip kur. Kurulum sırasında "Git Bash" seçeneğini işaretlemeni öneririm, bu sana Windows içinde Linux benzeri bir terminal sağlar.
* **macOS:** Terminale `git` yazarsan otomatik olarak yüklemek isteyip istemediğini sorar veya [Homebrew](https://brew.sh/) varsa `brew install git` yazabilirsin.
* **Linux:** `sudo apt-get install git` (Ubuntu/Debian) veya `sudo dnf install git` (Fedora).

## 2. İlk Ayarlar (Configuration)

Git'i kurduktan sonra **sadece bir kez** yapman gereken kimlik tanıtma işlemi vardır.\
Bu, yaptığın değişikliklerin (commit) senin adınla görünmesini sağlar.

```bash
git config --global user.name "Adın Soyadın"
git config --global user.email "email@adresin.com"
```

### Daha önce giriş yapıp yapmadığını kontrol etmek istiyorsan

Terminalini aç ve sırasıyla şunları dene:

```bash
git config user.name
```

* **Eğer bir isim çıkarsa:** (Örn: `Ahmet Yilmaz`) Harika, ayarların yapılmış demektir.
* **Eğer boş bir satır gelirse:** Hiçbir ayar yapılmamış demektir.

Aynısını e-posta için de yapabilirsin:

```bash
git config user.email
```

### Tüm ayarları alt alta görmek istersen şu komutu kullanabilirsin

```bash
git config --list
```

Bu komuta bastığında ekrana bir sürü yazı gelebilir.

* Listede `user.name=...` ve `user.email=...` satırlarını ara.
* **Önemli Not:** Eğer liste çok uzunsa terminal "sonunu bekleme moduna" geçer (genelde altta `END` veya `:` yazar). Çıkmak için klavyeden **`q`** tuşuna basman yeterlidir.

### "Gördüğüm İsim/Mail Yanlış, Ne Yapacağım?"

Eğer komutları yazdığında eski bir takma adını veya artık kullanmadığın bir mail adresini gördüysen endişelenme. Git'te **"düzenle" diye bir buton yoktur, "üzerine yazma" vardır.**

Doğru bilgileri girmek için kurulum komutlarını tekrar yazman yeterli, eskilerinin üzerine otomatik olarak kaydeder:

```bash
git config --global user.name "Yeni Ve Dogru Adim"
git config --global user.email "dogrumailim@ornek.com"
```

## 3. Git Mantığını Anlamak

Komutlara geçmeden önce şu 3 aşamalı yapıyı kafanda canlandırman çok önemli.

1. **Working Directory (Çalışma Alanı):** Şu an üzerinde çalıştığın dosyalar.
2. **Staging Area (Sahne/Hazırlık):** Fotoğraf çekmeden önceki hazırlık alanı. Kaydetmek istediğin dosyaları buraya seçersin.
3. **Local Repository (Yerel Depo):** Fotoğrafın çekildiği, değişikliğin kalıcı olarak kaydedildiği yer.

## 4. Temel Komutlar Listesi

### Kurulum ve Yapılandırma

> **`git --version`** Sistemde kurulu Git versiyonunu kontrol eder.

* **Örnek Çıktı:** `git version 2.43.0`

> **`git config --global user.name "Ahmet Yılmaz"`** Git yapılandırma ayarlarını yönetir.
> **`git config --global user.email "ahmet@example.com"`** Email Adresi Ayarlama
> **`git config --list`** Yapılandırmaları Listeleme

### Proje Başlatma

> **`git init`**  Bulunduğun klasörü bir Git projesine dönüştürür. O klasörde `.git` adında gizli bir dosya oluşturur.

* Terminalden proje klasörünün uzantısının girip `git init` yazman yeterlidir.

> **`git clone [url]`** GitHub veya GitLab gibi internetteki hazır bir projeyi bilgisayarına indirir.

* *Örnek:* `git clone https://github.com/kullanici/proje.git`

### Değişiklikleri İzleme ve Ekleme

> **`git status`** (En İyi Dostun) Hangi dosyaların değiştiğini, hangilerinin sahneye (staging) atıldığını gösterir.

Kaybolduğun an bunu yaz.

> **`git add [dosya_adı]`** Belirli bir dosyayı sahneye (hazırlık alanına) ekler.

| Komut | Açıklama |
| --- | --- |
| `git add dosya.txt` | Tek dosya ekler |
| `git add .` | Tüm değişiklikleri ekler |
| `git add *.html` | Tüm HTML dosyalarını ekler |
| `git add dizin/` | Dizin içeriğini ekler |
| `git add -A` | Tüm değişiklikleri ekler (silinen dahil) |
| `git add -u` | Sadece değişen ve silinen dosyaları ekler |

* *İpucu:* Tüm dosyaları eklemek için `git add .` (sonundaki noktaya dikkat) kullanılır.

> **`git diff`** Değişiklikleri karşılaştırır.

| Komut | Açıklama |
| --- | --- |
| `git diff` | Working directory vs staging area |
| `git diff --staged` | Staging area vs son commit |
| `git diff HEAD` | Working directory vs son commit |
| `git diff branch1 branch2` | İki branch'i karşılaştır |

### Kaydetme (Commit)

> **`git commit -m "Mesajın"`** Sahneye eklediğin dosyaları kalıcı olarak kaydeder (fotoğrafı çeker).

| Parametre | Açıklama |
| --- | --- |
| `-m "mesaj"` | Commit mesajını belirtir |
| `-a` | Tüm değişen dosyaları otomatik ekler ve commit eder |
| `--amend` | Son commit'i düzenler |

---

### Geçmişi Görme

> **`git log`** Projenin tarihçesini, kimin ne zaman ne değişiklik yaptığını listeler. Çıkmak için klavyeden `q` tuşuna basabilirsin.

| Komut | Açıklama |
| --- | --- |
| `git log` | Standart log görünümü |
| `git log --oneline` | Her commit tek satırda |
| `git log --graph` | Branch grafiği ile |
| `git log --all` | Tüm branch'leri gösterir |
| `git log -n 5` | Son 5 commit'i gösterir |
| `git log --author="İsim"` | Belirli yazara ait commit'ler |

---

### Branch (Dal) Yönetimi

> **`git branch`** Branch'leri listeler veya oluşturur.

| Komut | Açıklama |
| --- | --- |
| `git branch` | Tüm branch'leri listeler |
| `git branch <isim>` | Yeni branch oluşturur |
| `git branch -d <isim>` | Branch'i siler (merge edilmiş) |
| `git branch -D <isim>` | Branch'i zorla siler |
| `git branch -m <eski> <yeni>` | Branch'i yeniden adlandırır |

---

> **`git checkout`** Branch'ler arası geçiş yapar.

* **Branch'e geç:** `git checkout main`
* **Yeni branch oluştur ve geç:** `git checkout -b yeni-ozellik`

> **`git merge`** Bir branch'i mevcut branch'e birleştirir.

### Uzak Repository İşlemleri

> **`git remote`** Uzak repository bağlantılarını yönetir.

| Komut | Açıklama |
| --- | --- |
| `git remote` | Uzak repository'leri listeler |
| `git remote -v` | URL'lerle birlikte listeler |
| `git remote add <isim> <url>` | Yeni uzak repository ekler |
| `git remote remove <isim>` | Uzak repository'yi kaldırır |

---
> **`git push`** Yerel commit'leri uzak repository'ye gönderir.

| Komut | Açıklama |
| --- | --- |
| `git push` | Varsayılan branch'i gönderir |
| `git push origin main` | main branch'ini origin'e gönderir |
| `git push -u origin main` | Upstream bağlantısı kurar (ilk push) |
| `git push --all` | Tüm branch'leri gönderir |

---
> **`git pull`:** Uzak repository'deki değişiklikleri çeker ve birleştirir.

* *Formül:* `git pull` = `git fetch` + `git merge`

> **`git fetch`:** Uzak repository'deki değişiklikleri indirir ama birleştirmez (daha güvenli).

### Geri Alma ve Düzeltme

> `git restore` Dosya değişikliklerini geri alır.

| Komut | Açıklama |
| --- | --- |
| `git restore dosya.txt` | Working directory'deki değişiklikleri geri alır |
| `git restore --staged dosya.txt` | Staging area'dan çıkarır (unstage) |

---
> `git reset` Commit'leri veya staging area'yı sıfırlar.

| Mod | Açıklama |
| --- | --- |
| `--soft` | Commit'i geri alır, değişiklikler staged kalır |
| `--mixed` | Commit'i geri alır, değişiklikler unstaged kalır |
| `--hard` | Commit'i geri alır, değişiklikler **SİLİNİR** (TEHLİKELİ) |

---
> `git revert` Bir commit'in tersini yapan yeni bir commit oluşturur.

* **Reset:** Geçmişi değiştirir (tehlikeli).
* **Revert:** Yeni commit ekler (güvenli).

### Geçici Saklama (Stash)

Değişiklikleri geçici olarak saklamak için kullanılır.

| Komut | Açıklama |
| --- | --- |
| `git stash` | Değişiklikleri saklar |
| `git stash save "mesaj"` | Mesajla birlikte saklar |
| `git stash list` | Tüm stash'leri listeler |
| `git stash pop` | Son stash'i geri getirir ve siler |
| `git stash apply` | Son stash'i geri getirir, silmez |
| `git stash drop` | Son stash'i siler |

---

### Diğer Faydalı Komutlar

> **`git rm`:** Dosyayı hem Git'ten hem de diskten siler.
> `git rm --cached dosya.txt`: Git'ten siler, diskte kalır.
> **`git mv`:** Dosyayı taşır veya yeniden adlandırır (`git mv eski.txt yeni.txt`).
> **`git tag`:** Belirli bir commit'e etiket ekler (`git tag v1.0.0`).

## Altın Kurallar

* **Her gün pull yapın:** Çalışmaya başlamadan önce.
* **Sık commit edin:** Küçük, anlamlı parçalar halinde.
* **Açıklayıcı mesajlar:** Commit mesajlarını özenle yazın.
* **Branch kullanın:** Her özellik için ayrı dal.
* **Push etmeden önce test edin:** Kırık kod göndermeyin.

**Bundan sonrası için:**
Bu temel adımları oturttuktan sonra, kodunu internete (GitHub'a) yüklemek için `git push` ve dallanma (branch) mantığını öğrenmen gerekecek.
