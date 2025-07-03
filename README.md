# Parça Envanter Sistemi

Bu proje, Django kullanılarak geliştirilmiş basit bir parça envanter yönetim sistemidir. Kullanıcıların parça bilgilerini eklemesine, düzenlemesine, silmesine ve listelemesine olanak tanır.

## Özellikler

- Kullanıcı kaydı ve girişi
- Parça ekleme, düzenleme ve silme
- Parçaları listeleme ve arama
- Parça fotoğrafları yükleme

## Kurulum

Projeyi yerel ortamınızda çalıştırmak için aşağıdaki adımları izleyin:

1.  **Depoyu Klonlayın:**
    ```bash
    git clone https://github.com/bhdrgngr/gemini-test.git
    cd gemini-test
    ```

2.  **Sanal Ortam Oluşturun ve Aktive Edin:**
    ```bash
    python -m venv venv
    # Windows
    .\venv\Scripts\activate
    # macOS/Linux
    source venv/bin/activate
    ```

3.  **Bağımlılıkları Yükleyin:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Veritabanı Migrasyonlarını Uygulayın:**
    ```bash
    python manage.py migrate
    ```

5.  **Süper Kullanıcı Oluşturun (İsteğe Bağlı):**
    Yönetici paneline erişmek için bir süper kullanıcı oluşturabilirsiniz:
    ```bash
    python manage.py createsuperuser
    ```

6.  **Geliştirme Sunucusunu Başlatın:**
    ```bash
    python manage.py runserver
    ```

Tarayıcınızda `http://127.0.0.1:8000/` adresine giderek uygulamaya erişebilirsiniz.

## Kullanım

-   **Kayıt Olma/Giriş Yapma:** Uygulamayı kullanmaya başlamak için bir hesap oluşturun veya mevcut bir hesapla giriş yapın.
-   **Parça Yönetimi:** Giriş yaptıktan sonra, parçaları ekleyebilir, mevcut parçaları düzenleyebilir veya silebilirsiniz.

## Katkıda Bulunma

Katkılarınızı memnuniyetle karşılarız! Lütfen bir pull request göndermeden önce değişikliklerinizi test ettiğinizden emin olun.

## Lisans

Bu proje MIT Lisansı altında lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasına bakın.
