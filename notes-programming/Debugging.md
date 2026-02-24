# Debugging (Hata Ayıklama)

> **Definition:** Yazılımda oluşan hataları (**Bugs**) bulma, izole etme ve düzeltme sürecidir.

* **Debug Mode:** Bir geliştiricinin kodun çalışma anındaki (*runtime*) tüm davranışlarını analiz etmesini sağlayan kritik yapıdır.
* **Scope:** Genellikle söz dizimi hatalarından ziyade, programın beklenmedik şekilde davrandığı **Logical Errors** (Mantıksal Hatalar) ve **Runtime Errors** için kullanılır.

## Key Functions (Temel İşlevler)

* **Value Tracking (Değer Takibi):** Hangi değişkenin, hangi kod satırında, hangi değere sahip olduğunu anlık olarak görüntüleme.
* **Flow Control (Akış Takibi):** Programın `if/else` blokları veya `for/while` döngüleri içinde beklenen mantıksal yolu izleyip izlemediğini kontrol etme.
* **External Interaction:** Sunucu veya veritabanı gibi dış kaynaklarla yapılan iletişimde giden **Request** (İstek) ve gelen **Response** (Cevap) verilerinin doğruluğunu inceleme.

### Debugging Process (Nasıl Yapılır?)

1. **Set Breakpoint:** Debug işleminin başlamasını istediğiniz kod satırının yanına bir "durma noktası" (kırmızı nokta/işaretleyici) koyulur.

2. **Start Debug Mode:** Program standart çalıştırma yerine debug modunda başlatılır.\
*Example:* **VS Code** gibi IDE'lerde genellikle `F5` kısayolu veya `Run -> Start Debugging` menüsü kullanılır.

3. **Step-by-Step Execution:** Program breakpoint'te durur. Geliştirici, akışı manuel olarak yönetir:\
**Step Over:** Fonksiyonun içine girmeden bir sonraki satıra geçmek.\
**Step Into:** Fonksiyonun detayına girerek satır satır incelemek.
