# MEDIA SERVICE

<hr>

## API DOCUMENTATION

## Facebook

### Endpoints

### 1. `/`, `/public`

**Method:** `GET`

#### Query Parameters:

- `link` (string, majburiy): Facebook havolasi.

#### Response:

- **200 OK**: So'rov muvaffaqiyatli amalga oshirilsa.
    ```json
    {
      "status": "ok",
      "data": {
        "type": "image",
        "post_id": "qhm5pvnpjgptF3iM",
        "download_url": "http://media-service.uz/facebook/public/qhm5pvnpjgptF3iM/download"
      }
    }
    ```

- **400 Bad Request**: Agar so'rovda xatolik bo'lsa yoki noto'g'ri parametrlar yuborilgan bo'lsa.
    ```json
    {
        "status": "failed",
        "reason": "Error message"
    }
    ```

- **500 Internal Server Error**: Server ichki xatoligi yuz bergan bo'lsa.
    ```json
    {
        "status": "failed",
        "reason": "An internal server error occurred. Please try again later."
    }
    ```

### 2. `/public/{post_id}/download`, `/public/{post_id}/{ind}/download`

**Method:** `GET`

#### Path Parameters:

- `post_id` (string, majburiy): Post Id
- `ind` (string, ixtyoriy): Post index

#### Response:

- **200 OK**: So'rov muvaffaqiyatli amalga oshirilsa.
    ```
    Streaming response
    ```

- **400 Bad Request**: Agar so'rovda xatolik bo'lsa yoki noto'g'ri parametrlar yuborilgan bo'lsa.
    ```json
    {
        "status": "failed",
        "reason": "Error message"
    }
    ```

- **500 Internal Server Error**: Server ichki xatoligi yuz bergan bo'lsa.
    ```json
    {
        "status": "failed",
        "reason": "An internal server error occurred. Please try again later."
    }
    ```

### 3. `{post_id}/download`, `/{post_id}/{ind}/download`

**Method:** `GET`

#### Path Parameters:

- `post_id` (string, majburiy): Post Id
- `ind` (string, ixtyoriy): Post index

#### Query Parameters:

- `bot_id` (string, majburiy): Bot id

#### Response:

- **200 OK**: So'rov muvaffaqiyatli amalga oshirilsa.
    ```json
    {
      "status": "ok",
      "data": {
          "chat_id": 0,
          "message_id": 0
      } 
    }
    ```

- **400 Bad Request**: Agar so'rovda xatolik bo'lsa yoki noto'g'ri parametrlar yuborilgan bo'lsa.
    ```json
    {
        "status": "failed",
        "reason": "Error message"
    }
    ```

- **500 Internal Server Error**: Server ichki xatoligi yuz bergan bo'lsa.
    ```json
    {
        "status": "failed",
        "reason": "An internal server error occurred. Please try again later."
    }
    ```

<hr>

## Instagram

### Endpoints

### 1. `/`, `/public`

**Method:** `GET`

#### Query Parameters:

- `link` (string, majburiy): Instagram havolasi.

#### Response:

- **200 OK**: So'rov muvaffaqiyatli amalga oshirilsa.
    ```json
    {
        "status": "ok",
        "data": {
            "type": "video",
            "post_id": "DAZyNfuImOV",
            "title": "Where do you want to go?",
            "download_url": "http://media-service.uz/instagram/public/DAZyNfuImOV/download",
            "thumnail_url": "https://instagram.fsap12-1.fna.fbcdn.net/v/t51.2885-15/464157231_522316883903995_8694829477000956934_n.jpg?stp=dst-jpg_e15&_nc_ht=instagram.fsap12-1.fna.fbcdn.net&_nc_cat=107&_nc_ohc=TQnOZ5aYcDQQ7kNvgHJVuxl&_nc_gid=52d5c62c3d9d4a89a6cb02ba7fb211fb&edm=APs17CUBAAAA&ccb=7-5&oh=00_AYAwtdIArWZobIuimBP-rJWEyL-VDLCz5pY1Xj-AAV8JFQ&oe=67225CE8&_nc_sid=10d13b"
        }
    }
    ```

- **400 Bad Request**: Agar so'rovda xatolik bo'lsa yoki noto'g'ri parametrlar yuborilgan bo'lsa.
    ```json
    {
        "status": "failed",
        "reason": "Error message"
    }
    ```

- **500 Internal Server Error**: Server ichki xatoligi yuz bergan bo'lsa.
    ```json
    {
        "status": "failed",
        "reason": "An internal server error occurred. Please try again later."
    }
    ```

### 2. `/public/{post_id}/download`, `/public/{post_id}/{ind}/download`

**Method:** `GET`

#### Path Parameters:

- `post_id` (string, majburiy): Post Id
- `ind` (string, ixtyoriy): Post index
-

#### Response:

- **200 OK**: So'rov muvaffaqiyatli amalga oshirilsa.
    ```
    Streaming response
    ```

- **400 Bad Request**: Agar so'rovda xatolik bo'lsa yoki noto'g'ri parametrlar yuborilgan bo'lsa.
    ```json
    {
        "status": "failed",
        "reason": "Error message"
    }
    ```

- **500 Internal Server Error**: Server ichki xatoligi yuz bergan bo'lsa.
    ```json
    {
        "status": "failed",
        "reason": "An internal server error occurred. Please try again later."
    }
    ```

### 3. `{post_id}/download`, `/{post_id}/{ind}/download`

**Method:** `GET`

#### Path Parameters:

- `post_id` (string, majburiy): Post Id
- `ind` (string, ixtyoriy): Post index

#### Query Parameters:

- `bot_id` (string, majburiy): Bot id

#### Response:

- **200 OK**: So'rov muvaffaqiyatli amalga oshirilsa.
    ```json
    {
      "status": "ok",
      "data": {
          "chat_id": 0,
          "message_id": 0
      } 
    }
    ```

- **400 Bad Request**: Agar so'rovda xatolik bo'lsa yoki noto'g'ri parametrlar yuborilgan bo'lsa.
    ```json
    {
        "status": "failed",
        "reason": "Error message"
    }
    ```

- **500 Internal Server Error**: Server ichki xatoligi yuz bergan bo'lsa.
    ```json
    {
        "status": "failed",
        "reason": "An internal server error occurred. Please try again later."
    }
    ```

<hr>

## Pinterest

### Endpoints

### 1. `/`, `/public`

**Method:** `GET`

#### Query Parameters:

- `link` (string, majburiy): Pinterest havolasi.

#### Response:

- **200 OK**: So'rov muvaffaqiyatli amalga oshirilsa.
    ```json
    {
        "status": "ok",
        "data": {
            "type": "image",
            "post_id": "5feEhMHWZ",
            "title": "How To Tie A Simple Knot (Oriental Knot) | Ties.com",
            "download_url": "http://media-service.uz/pinterest/public/5feEhMHWZ/download"
        }
    }
    ```

- **400 Bad Request**: Agar so'rovda xatolik bo'lsa yoki noto'g'ri parametrlar yuborilgan bo'lsa.
    ```json
    {
        "status": "failed",
        "reason": "Error message"
    }
    ```

- **500 Internal Server Error**: Server ichki xatoligi yuz bergan bo'lsa.
    ```json
    {
        "status": "failed",
        "reason": "An internal server error occurred. Please try again later."
    }
    ```

### 2. `/public/{post_id}/download`, `/public/{post_id}/{ind}/download`

**Method:** `GET`

#### Path Parameters:

- `post_id` (string, majburiy): Post Id
- `ind` (string, ixtyoriy): Post index

#### Response:

- **200 OK**: So'rov muvaffaqiyatli amalga oshirilsa.
    ```
    Streaming response
    ```

- **400 Bad Request**: Agar so'rovda xatolik bo'lsa yoki noto'g'ri parametrlar yuborilgan bo'lsa.
    ```json
    {
        "status": "failed",
        "reason": "Error message"
    }
    ```

- **500 Internal Server Error**: Server ichki xatoligi yuz bergan bo'lsa.
    ```json
    {
        "status": "failed",
        "reason": "An internal server error occurred. Please try again later."
    }
    ```

### 3. `{post_id}/download`, `/{post_id}/{ind}/download`

**Method:** `GET`

#### Path Parameters:

- `post_id` (string, majburiy): Post Id
- `ind` (string, ixtyoriy): Post index

#### Query Parameters:

- `bot_id` (string, majburiy): Bot id

#### Response:

- **200 OK**: So'rov muvaffaqiyatli amalga oshirilsa.
    ```json
    {
      "status": "ok",
      "data": {
          "chat_id": 0,
          "message_id": 0
      } 
    }
    ```

- **400 Bad Request**: Agar so'rovda xatolik bo'lsa yoki noto'g'ri parametrlar yuborilgan bo'lsa.
    ```json
    {
        "status": "failed",
        "reason": "Error message"
    }
    ```

- **500 Internal Server Error**: Server ichki xatoligi yuz bergan bo'lsa.
    ```json
    {
        "status": "failed",
        "reason": "An internal server error occurred. Please try again later."
    }
    ```

<hr>

## Tiktok

### Endpoints

### 1. `/`, `/public`

**Method:** `GET`

#### Query Parameters:

- `link` (string, majburiy): TikTok havolasi.

#### Response:

- **200 OK**: So'rov muvaffaqiyatli amalga oshirilsa.
    ```json
    {
        "status": "ok",
        "data": {
            "post_id": "7416843869133851909",
            "title": "Майкал Джексон жив с вероятностью 99%",
            "download_url": "http://media-service.uz/tiktok/public/7416843869133851909/download",
            "link": "https://www.tiktok.com/@alexhistorykorol/video/7416843869133851909?is_from_webapp=1&sender_device=pc"
        }
    }
    ```

- **400 Bad Request**: Agar so'rovda xatolik bo'lsa yoki noto'g'ri parametrlar yuborilgan bo'lsa.
    ```json
    {
        "status": "failed",
        "reason": "Error message"
    }
    ```

- **500 Internal Server Error**: Server ichki xatoligi yuz bergan bo'lsa.
    ```json
    {
        "status": "failed",
        "reason": "An internal server error occurred. Please try again later."
    }
    ```

### 2. `/public/{post_id}/download`

**Method:** `GET`

#### Path Parameters:

- `post_id` (string, majburiy): Post ID

#### Response:

- **200 OK**: So'rov muvaffaqiyatli amalga oshirilsa.
    ```
    Streaming response
    ```

- **400 Bad Request**: Agar so'rovda xatolik bo'lsa yoki noto'g'ri parametrlar yuborilgan bo'lsa.
    ```json
    {
        "status": "failed",
        "reason": "Error message"
    }
    ```

- **500 Internal Server Error**: Server ichki xatoligi yuz bergan bo'lsa.
    ```json
    {
        "status": "failed",
        "reason": "An internal server error occurred. Please try again later."
    }
    ```

### 3. `{post_id}/download`

**Method:** `GET`

#### Path Parameters:

- `post_id` (string, majburiy): Post ID

#### Query Parameters:

- `bot_id` (string, majburiy): Bot id

#### Response:

- **200 OK**: So'rov muvaffaqiyatli amalga oshirilsa.
    ```json
    {
      "status": "ok",
      "data": {
          "chat_id": 0,
          "message_id": 0
      } 
    }
    ```

- **400 Bad Request**: Agar so'rovda xatolik bo'lsa yoki noto'g'ri parametrlar yuborilgan bo'lsa.
    ```json
    {
        "status": "failed",
        "reason": "Error message"
    }
    ```

- **500 Internal Server Error**: Server ichki xatoligi yuz bergan bo'lsa.
    ```json
    {
        "status": "failed",
        "reason": "An internal server error occurred. Please try again later."
    }
    ```

<hr>

## Track

### Endpoints

### 1. `/search`, `/public/search`

**Method:** `GET`

#### Query Parameters:

- `query` (string, majburiy): Qidirish uchun query

#### Response:

- **200 OK**: So'rov muvaffaqiyatli amalga oshirilsa.
    ```json
    {
        "status": "ok",
        "data": [
            {
                "id": "k-3Ow2_RjSI",
                "title": "What is Salome?",
                "performer": "Bram Bos",
                "duration": 255.0,
                "thumbnail_url": "https://i.ytimg.com/vi/k-3Ow2_RjSI/hq720.jpg?sqp=-oaymwEcCOgCEMoBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLDrzKBcaeb6gjToXdYhxddyFyAp3A",
                "lyrics": "http://media-service.uz/track/public/k-3Ow2_RjSI/lyrics",
                "download_url": "http://media-service.uz/track/public/k-3Ow2_RjSI/download"
            },
            {
                "id": "SsWrY77o77o",
                "title": "Anjelah Johnson - Nail Salon  (Stand Up Comedy)",
                "performer": "Comedy Time",
                "duration": 262.0,
                "thumbnail_url": "https://i.ytimg.com/vi/SsWrY77o77o/hqdefault.jpg?sqp=-oaymwEcCOADEI4CSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLDehfAwg7AeFOonllu95K5YWkcHWg",
                "lyrics": "http://media-service.uz/track/public/SsWrY77o77o/lyrics",
                "download_url": "http://media-service.uz/track/public/SsWrY77o77o/download"
            },
            {
                "id": "_bPjsDcPHks",
                "title": "Diamond Platnumz ft Rayvanny - Salome (Traditional Official Music video)",
                "performer": "Diamond Platnumz",
                "duration": 211.0,
                "thumbnail_url": "https://i.ytimg.com/vi/_bPjsDcPHks/hq720.jpg?sqp=-oaymwE2COgCEMoBSFXyq4qpAygIARUAAIhCGAFwAcABBvABAfgB_gmAAtAFigIMCAAQARhyIFwoIzAP&rs=AOn4CLAQCL-txZYcMH_iTqovpD3dZ52joA",
                "lyrics": "http://media-service.uz/track/public/_bPjsDcPHks/lyrics",
                "download_url": "http://media-service.uz/track/public/_bPjsDcPHks/download"
            },
            {
                "id": "ri73kcEh00c",
                "title": "Diamond Platnumz ft Rayvanny Salome ( Club Bangger Official Audio )",
                "performer": "Diamond Platnumz",
                "duration": 212.0,
                "thumbnail_url": "https://i.ytimg.com/vi/ri73kcEh00c/hq720.jpg?sqp=-oaymwE2COgCEMoBSFXyq4qpAygIARUAAIhCGAFwAcABBvABAfgB1AaAAuADigIMCAAQARhyIFgoOTAP&rs=AOn4CLC4RPVdUr1YWV_1VZ4bwov40OTOvg",
                "lyrics": "http://media-service.uz/track/public/ri73kcEh00c/lyrics",
                "download_url": "http://media-service.uz/track/public/ri73kcEh00c/download"
            },
            {
                "id": "_BvUz5PFjl8",
                "title": "Natural Sound Sequence: Nail Salon edition",
                "performer": "Gerilee Rosado",
                "duration": 64.0,
                "thumbnail_url": "https://i.ytimg.com/vi/_BvUz5PFjl8/hqdefault.jpg?sqp=-oaymwEcCOADEI4CSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLBnYH7BJ-ozeoRDBXW-16TytOaYkw",
                "lyrics": "http://media-service.uz/track/public/_BvUz5PFjl8/lyrics",
                "download_url": "http://media-service.uz/track/public/_BvUz5PFjl8/download"
            },
            {
                "id": "zI3PvaWu9hU",
                "title": "Hey Saloma Salom Subhas || High Quality Audio  Vidyasagar Hits",
                "performer": "MUSIC LOVER MELOPHILE",
                "duration": 320.0,
                "thumbnail_url": "https://i.ytimg.com/vi/zI3PvaWu9hU/hq720.jpg?sqp=-oaymwEcCOgCEMoBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLAHltzLlB9aIV4oOOlzPFc8WaVCfg",
                "lyrics": "http://media-service.uz/track/public/zI3PvaWu9hU/lyrics",
                "download_url": "http://media-service.uz/track/public/zI3PvaWu9hU/download"
            },
            {
                "id": "ATZeD--wKBc",
                "title": "Muhammad Yusuf - Mendan salom (audio 2022)",
                "performer": "NevoMusic",
                "duration": 216.0,
                "thumbnail_url": "https://i.ytimg.com/vi/ATZeD--wKBc/hq720.jpg?sqp=-oaymwEcCOgCEMoBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLAasopJwItHXVhQf4SUfx2VFH_0jA",
                "lyrics": "http://media-service.uz/track/public/ATZeD--wKBc/lyrics",
                "download_url": "http://media-service.uz/track/public/ATZeD--wKBc/download"
            },
            {
                "id": "Hf8TtLmWWsI",
                "title": "Diamond Platnumz ft Rayvanny Salome ( Traditional Official Audio )",
                "performer": "Diamond Platnumz",
                "duration": 212.0,
                "thumbnail_url": "https://i.ytimg.com/vi/Hf8TtLmWWsI/hq720.jpg?sqp=-oaymwE2COgCEMoBSFXyq4qpAygIARUAAIhCGAFwAcABBvABAfgB_gmAAtAFigIMCAAQARhlIFYoQTAP&rs=AOn4CLBf0HFXuuP3kXvL2loiS3GzNCGIKw",
                "lyrics": "http://media-service.uz/track/public/Hf8TtLmWWsI/lyrics",
                "download_url": "http://media-service.uz/track/public/Hf8TtLmWWsI/download"
            },
            {
                "id": "fIkOe2QCZio",
                "title": "Diamond Platnumz - SALOME AUDIO MAKING PART 1 ( WASAFI STUDIO)",
                "performer": "Diamond Platnumz",
                "duration": 567.0,
                "thumbnail_url": "https://i.ytimg.com/vi/fIkOe2QCZio/hq720.jpg?sqp=-oaymwE2COgCEMoBSFXyq4qpAygIARUAAIhCGAFwAcABBvABAfgB1AaAAuADigIMCAAQARhlIGUoSDAP&rs=AOn4CLAhGVZ7-OIeXfvvoHuVS5o19vwXkA",
                "lyrics": "http://media-service.uz/track/public/fIkOe2QCZio/lyrics",
                "download_url": "http://media-service.uz/track/public/fIkOe2QCZio/download"
            }
        ]
    }
    ```

- **400 Bad Request**: Agar so'rovda xatolik bo'lsa yoki noto'g'ri parametrlar yuborilgan bo'lsa.
    ```json
    {
        "status": "failed",
        "reason": "Error message"
    }
    ```

- **500 Internal Server Error**: Server ichki xatoligi yuz bergan bo'lsa.
    ```json
    {
        "status": "failed",
        "reason": "An internal server error occurred. Please try again later."
    }
    ```

### 2. `/{track}/lyrics`, `/public/{track}/lyrics`

**Method:** `GET`

#### Path Parameters:

- `track` (string, majburiy): Track id

#### Response:

- **200 OK**: So'rov muvaffaqiyatli amalga oshirilsa.
    ```json
    {
        "status": "ok",
        "data": "Text"
    }
    ```

- **400 Bad Request**: Agar so'rovda xatolik bo'lsa yoki noto'g'ri parametrlar yuborilgan bo'lsa.
    ```json
    {
        "status": "failed",
        "reason": "Error message"
    }
    ```

- **500 Internal Server Error**: Server ichki xatoligi yuz bergan bo'lsa.
    ```json
    {
        "status": "failed",
        "reason": "An internal server error occurred. Please try again later."
    }
    ```

### 3. `/public/popular`, `/popular`

**Method:** `GET`

#### Query Parameters:

- `country_code` (string, ixtyoriy): Country ("UZ", "RU", "US")
- `limit` (int, ixtyoriy): limit

#### Response:

- **200 OK**: So'rov muvaffaqiyatli amalga oshirilsa.
    ```json
    {
        "status": "ok",
        "data": [
            {
                "id": "4HnXpSQ_wOU",
                "title": "Ikrom Ali Singer - Soxta Hijoblilar ( Piono Version)|#soxtahijoblilar #soxtamuslimalar #hijoblilar",
                "performer": "IKROM_ALI_SINGER OFFICIAL",
                "duration": 113.0,
                "thumbnail_url": "https://i.ytimg.com/vi/4HnXpSQ_wOU/hq720.jpg?sqp=-oaymwEcCOgCEMoBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLD0T7bjIVo6b34loYNCXgi19ZBi_g"
            },
            {
                "id": "fXglXSAN0oE",
                "title": "Есенин",
                "performer": "Navai - Topic",
                "duration": 171.0,
                "thumbnail_url": "https://i.ytimg.com/vi/fXglXSAN0oE/hq720.jpg?sqp=-oaymwEcCOgCEMoBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLDx_ZhoTS-976YfHFoRcGCapkPvcA"
            },
            {
                "id": "qrjbA_xIAxM",
                "title": "O Melhor no Que Faz 3.0 - ( slowed ) - DJ BRYAN 7",
                "performer": "Ikeraus 🎼",
                "duration": 146.0,
                "thumbnail_url": "https://i.ytimg.com/vi/qrjbA_xIAxM/hqdefault.jpg?sqp=-oaymwEcCOADEI4CSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLAwpm51XlU4NtyxYmQDQcTbWUPoUg"
            }
        ]
    }
    ```

- **400 Bad Request**: Agar so'rovda xatolik bo'lsa yoki noto'g'ri parametrlar yuborilgan bo'lsa.
    ```json
    {
        "status": "failed",
        "reason": "Error message"
    }
    ```

- **500 Internal Server Error**: Server ichki xatoligi yuz bergan bo'lsa.
    ```json
    {
        "status": "failed",
        "reason": "An internal server error occurred. Please try again later."
    }
    ```

### 4. `/recognize-from-youtube`, `/public/recognize-from-youtube`,

**Method:** `GET`

#### Query Parameters:

- `link` (string, majburiy): Youtube link

#### Response:

- **200 OK**: So'rov muvaffaqiyatli amalga oshirilsa.
    ```json
    {
        "status": "ok",
        "data": [
            {
                "id": "rVORdn4Xpzk",
                "title": "The Weeknd, Playboi Carti - Timeless (Official Audio)",
                "performer": "The Weeknd",
                "duration": 257.0,
                "thumbnail_url": "https://i.ytimg.com/vi/rVORdn4Xpzk/hq720.jpg?sqp=-oaymwEcCOgCEMoBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLA4lVYqxywwwqH_wrnaAl_2z9JbxQ",
                "lyrics": "http://media-service.uz/track/public/rVORdn4Xpzk/lyrics",
                "download_url": "http://media-service.uz/track/public/rVORdn4Xpzk/download"
            },
            {
                "id": "5EpyN_6dqyk",
                "title": "The Weeknd – Timeless with Playboi Carti (Official Music Video)",
                "performer": "The Weeknd",
                "duration": 257.0,
                "thumbnail_url": "https://i.ytimg.com/vi/5EpyN_6dqyk/hq720.jpg?sqp=-oaymwEcCOgCEMoBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLC8rZllcYT7LToUskOi9Ajiq2VQMg",
                "lyrics": "http://media-service.uz/track/public/5EpyN_6dqyk/lyrics",
                "download_url": "http://media-service.uz/track/public/5EpyN_6dqyk/download"
            },
            {
                "id": "16jA-6hiSUo",
                "title": "The Weeknd, Playboi Carti - Timeless (Official Lyric Video)",
                "performer": "The Weeknd",
                "duration": 257.0,
                "thumbnail_url": "https://i.ytimg.com/vi/16jA-6hiSUo/hq720.jpg?sqp=-oaymwEcCOgCEMoBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLAtHyAYBMCIgxXTIymVMucT3k70Ew",
                "lyrics": "http://media-service.uz/track/public/16jA-6hiSUo/lyrics",
                "download_url": "http://media-service.uz/track/public/16jA-6hiSUo/download"
            },
            {
                "id": "GF8E8oxp_zw",
                "title": "The Weeknd - Timeless (Lyrics) Feat. Playboi Carti",
                "performer": "Lost Panda",
                "duration": 256.0,
                "thumbnail_url": "https://i.ytimg.com/vi/GF8E8oxp_zw/hq720.jpg?sqp=-oaymwEcCOgCEMoBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLAmvQD-R3DUlZD4_gidgQQBZbjjIg",
                "lyrics": "http://media-service.uz/track/public/GF8E8oxp_zw/lyrics",
                "download_url": "http://media-service.uz/track/public/GF8E8oxp_zw/download"
            },
            {
                "id": "SRVsesZamZw",
                "title": "The Weeknd - Timeless (Live From Sao Paolo / 2024)",
                "performer": "The Weeknd",
                "duration": 180.0,
                "thumbnail_url": "https://i.ytimg.com/vi/SRVsesZamZw/hqdefault.jpg?sqp=-oaymwEcCOADEI4CSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLAVnXsUBIAZnQx4_x81Ppl2oW-sbg",
                "lyrics": "http://media-service.uz/track/public/SRVsesZamZw/lyrics",
                "download_url": "http://media-service.uz/track/public/SRVsesZamZw/download"
            }
        ]
    }
    ```

- **400 Bad Request**: Agar so'rovda xatolik bo'lsa yoki noto'g'ri parametrlar yuborilgan bo'lsa.
    ```json
    {
        "status": "failed",
        "reason": "Error message"
    }
    ```

- **500 Internal Server Error**: Server ichki xatoligi yuz bergan bo'lsa.
    ```json
    {
        "status": "failed",
        "reason": "An internal server error occurred. Please try again later."
    }
    ```

### 5. `/recognize-from-instagram`, `/public/recognize-from-instagram`,

**Method:** `GET`

#### Query Parameters:

- `link` (string, majburiy): Instagram link

#### Response:

- **200 OK**: So'rov muvaffaqiyatli amalga oshirilsa.
    ```json
    {
        "status": "ok",
        "data": [
            {
                "id": "POci7_vW4aM",
                "title": "Javohir Usmon  - Sevmay qo'ydingiz",
                "performer": "Dilnavo Records ",
                "duration": 243.0,
                "thumbnail_url": "https://i.ytimg.com/vi/POci7_vW4aM/hq720.jpg?sqp=-oaymwE2COgCEMoBSFXyq4qpAygIARUAAIhCGAFwAcABBvABAfgB_gmAAtAFigIMCAAQARhMIFYoZTAP&rs=AOn4CLBtmusFLDU6XGprewtuDGET0SRlCA",
                "lyrics": "http://media-service.uz/track/public/POci7_vW4aM/lyrics",
                "download_url": "http://media-service.uz/track/public/POci7_vW4aM/download"
            }
        ]
    }
    ```

- **400 Bad Request**: Agar so'rovda xatolik bo'lsa yoki noto'g'ri parametrlar yuborilgan bo'lsa.
    ```json
    {
        "status": "failed",
        "reason": "Error message"
    }
    ```

- **500 Internal Server Error**: Server ichki xatoligi yuz bergan bo'lsa.
    ```json
    {
        "status": "failed",
        "reason": "An internal server error occurred. Please try again later."
    }
    ```

### 6. `/recognize-from-tiktok`, `/public/recognize-from-tiktok`,

**Method:** `GET`

#### Query Parameters:

- `link` (string, majburiy): Tiktok link

#### Response:

- **200 OK**: So'rov muvaffaqiyatli amalga oshirilsa.
    ```json
    {
        "status": "ok",
        "data": [
            {
                "id": "fFyarF9DMcY",
                "title": "фрози (frozy) - kompa pasión (slowed) [Ultra Records]",
                "performer": "Ultra Records",
                "duration": 174.0,
                "thumbnail_url": "https://i.ytimg.com/vi/fFyarF9DMcY/hq720.jpg?sqp=-oaymwEcCOgCEMoBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLAoE_NDl3xxyeau7VuiLAehfi2Kmg",
                "lyrics": "http://media-service.uz/track/public/fFyarF9DMcY/lyrics",
                "download_url": "http://media-service.uz/track/public/fFyarF9DMcY/download"
            },
            {
                "id": "Tc6d3t19YD4",
                "title": "фрози - kompa pasión (slowed)",
                "performer": "Minimal Sounds",
                "duration": 175.0,
                "thumbnail_url": "https://i.ytimg.com/vi/Tc6d3t19YD4/hq720.jpg?sqp=-oaymwEcCOgCEMoBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLCEHfmr9puBGfHvNi3SBx71InBAgw",
                "lyrics": "http://media-service.uz/track/public/Tc6d3t19YD4/lyrics",
                "download_url": "http://media-service.uz/track/public/Tc6d3t19YD4/download"
            },
            {
                "id": "-w5K08th9OA",
                "title": "фрози (frozy) - kompa pasión [Ultra Records]",
                "performer": "Ultra Records",
                "duration": 148.0,
                "thumbnail_url": "https://i.ytimg.com/vi/-w5K08th9OA/hq720.jpg?sqp=-oaymwEcCOgCEMoBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLAeuZK-D5v09eldpZphB5wc-lj53w",
                "lyrics": "http://media-service.uz/track/public/-w5K08th9OA/lyrics",
                "download_url": "http://media-service.uz/track/public/-w5K08th9OA/download"
            },
            {
                "id": "cyC2Up5OEOE",
                "title": "фрози (frozy) - kompa pasión (ULTRA slowed + reverb)",
                "performer": "happiTY",
                "duration": 245.0,
                "thumbnail_url": "https://i.ytimg.com/vi/cyC2Up5OEOE/hq720.jpg?sqp=-oaymwE2COgCEMoBSFXyq4qpAygIARUAAIhCGAFwAcABBvABAfgB_gmAAtAFigIMCAAQARhlIGUoZTAP&rs=AOn4CLA-q8fTgOFDmuKu0-B-Q78nb514jA",
                "lyrics": "http://media-service.uz/track/public/cyC2Up5OEOE/lyrics",
                "download_url": "http://media-service.uz/track/public/cyC2Up5OEOE/download"
            },
            {
                "id": "zgPIfFM3pFc",
                "title": "Jason Derulo, Frozy & Tomo - From The Islands (Kompa Passion) (Official Music Video)",
                "performer": "Jason Derulo",
                "duration": 169.0,
                "thumbnail_url": "https://i.ytimg.com/vi/zgPIfFM3pFc/hq720.jpg?sqp=-oaymwEcCOgCEMoBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLD8ix1fSjawK4iudlcm3jcacy7KeQ",
                "lyrics": "http://media-service.uz/track/public/zgPIfFM3pFc/lyrics",
                "download_url": "http://media-service.uz/track/public/zgPIfFM3pFc/download"
            }
        ]
    }
    ```

- **400 Bad Request**: Agar so'rovda xatolik bo'lsa yoki noto'g'ri parametrlar yuborilgan bo'lsa.
    ```json
    {
        "status": "failed",
        "reason": "Error message"
    }
    ```

- **500 Internal Server Error**: Server ichki xatoligi yuz bergan bo'lsa.
    ```json
    {
        "status": "failed",
        "reason": "An internal server error occurred. Please try again later."
    }
    ```

### 7. `/recognize-from-twitter`, `/recognize-from-twitter`,

**Method:** `GET`

#### Query Parameters:

- `link` (string, majburiy): Twitter link

#### Response:

- **200 OK**: So'rov muvaffaqiyatli amalga oshirilsa.
    ```json
    {
        "status": "ok",
        "data": [
            {
                "id": "DzVycgM8XHQ",
                "title": "Why Me",
                "performer": "Kris Kristofferson",
                "duration": 209.0,
                "thumbnail_url": "https://i.ytimg.com/vi/DzVycgM8XHQ/hq720.jpg?sqp=-oaymwEcCOgCEMoBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLAX6YnFOc_4lTPaUy4E4YHW63TrKA",
                "lyrics": "http://media-service.uz/track/public/DzVycgM8XHQ/lyrics",
                "download_url": "http://media-service.uz/track/public/DzVycgM8XHQ/download"
            },
            {
                "id": "Mx7JKp2TV8o",
                "title": "Why Me",
                "performer": "Kris Kristofferson",
                "duration": 178.0,
                "thumbnail_url": "https://i.ytimg.com/vi/Mx7JKp2TV8o/hq720.jpg?sqp=-oaymwEcCOgCEMoBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLCv598Ekk5iQWJPWt6sFwRCrnGFdg",
                "lyrics": "http://media-service.uz/track/public/Mx7JKp2TV8o/lyrics",
                "download_url": "http://media-service.uz/track/public/Mx7JKp2TV8o/download"
            },
            {
                "id": "PHSDYsHu0zA",
                "title": "Josh Turner - Why Me (Official Audio) ft. Kris Kristofferson",
                "performer": "Josh Turner",
                "duration": 181.0,
                "thumbnail_url": "https://i.ytimg.com/vi/PHSDYsHu0zA/hq720.jpg?sqp=-oaymwEcCOgCEMoBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLB8QUHZonClBWr8FO04Rq75cQuDkA",
                "lyrics": "http://media-service.uz/track/public/PHSDYsHu0zA/lyrics",
                "download_url": "http://media-service.uz/track/public/PHSDYsHu0zA/download"
            },
            {
                "id": "UONKp02bFsY",
                "title": "Why Me (Remastered)",
                "performer": "Kris Kristofferson",
                "duration": 180.0,
                "thumbnail_url": "https://i.ytimg.com/vi/UONKp02bFsY/hq720.jpg?sqp=-oaymwEcCOgCEMoBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLDcLQ9ukh1Jb1-6dMX2SPIzxus6vg",
                "lyrics": "http://media-service.uz/track/public/UONKp02bFsY/lyrics",
                "download_url": "http://media-service.uz/track/public/UONKp02bFsY/download"
            },
            {
                "id": "ZhAziWgpfcQ",
                "title": "FIRST TIME HEARING Kris Kristofferson  - Why Me REACTION",
                "performer": "Rob Squad Reactions",
                "duration": 521.0,
                "thumbnail_url": "https://i.ytimg.com/vi/ZhAziWgpfcQ/hq720.jpg?sqp=-oaymwEcCOgCEMoBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLDIynNU5-4fYUKM4zCHzjUA8lrxQA",
                "lyrics": "http://media-service.uz/track/public/ZhAziWgpfcQ/lyrics",
                "download_url": "http://media-service.uz/track/public/ZhAziWgpfcQ/download"
            }
        ]
    }
    ```

- **400 Bad Request**: Agar so'rovda xatolik bo'lsa yoki noto'g'ri parametrlar yuborilgan bo'lsa.
    ```json
    {
        "status": "failed",
        "reason": "Error message"
    }
    ```

- **500 Internal Server Error**: Server ichki xatoligi yuz bergan bo'lsa.
    ```json
    {
        "status": "failed",
        "reason": "An internal server error occurred. Please try again later."
    }
    ```

### 8. `/recognize-from-pinterest`, `/public/recognize-from-pinterest`,

**Method:** `GET`

#### Query Parameters:

- `link` (string, majburiy): Pinterest link

#### Response:

- **200 OK**: So'rov muvaffaqiyatli amalga oshirilsa.
    ```json
    {
        "status": "ok",
        "data": [
            {
                "id": "PZtwxD5Myk0",
                "title": "David Kushner - Daylight (Lyric Video)",
                "performer": "David Kushner",
                "duration": 214.0,
                "thumbnail_url": "https://i.ytimg.com/vi/PZtwxD5Myk0/hq720.jpg?sqp=-oaymwEcCOgCEMoBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLCc9y2x4wfjwuICGJw3KtZlttLeGw",
                "lyrics": "http://media-service.uz/track/public/PZtwxD5Myk0/lyrics",
                "download_url": "http://media-service.uz/track/public/PZtwxD5Myk0/download"
            },
            {
                "id": "5ugce5j-r3E",
                "title": "Daylight (Cinematic)",
                "performer": "David Kushner",
                "duration": 243.0,
                "thumbnail_url": "https://i.ytimg.com/vi/5ugce5j-r3E/hq720.jpg?sqp=-oaymwEcCOgCEMoBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLDziqCLTwsFVoxfutGrtlrGCO-IMg",
                "lyrics": "http://media-service.uz/track/public/5ugce5j-r3E/lyrics",
                "download_url": "http://media-service.uz/track/public/5ugce5j-r3E/download"
            },
            {
                "id": "MoN9ql6Yymw",
                "title": "David Kushner - Daylight (Official Music Video)",
                "performer": "David Kushner",
                "duration": 230.0,
                "thumbnail_url": "https://i.ytimg.com/vi/MoN9ql6Yymw/hq720.jpg?sqp=-oaymwEcCOgCEMoBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLDxI8o0eLW-S9vVI6TbNs8tVAdVEw",
                "lyrics": "http://media-service.uz/track/public/MoN9ql6Yymw/lyrics",
                "download_url": "http://media-service.uz/track/public/MoN9ql6Yymw/download"
            },
            {
                "id": "73E0BnFs7S4",
                "title": "David Kushner - Daylight (Lyrics)",
                "performer": "7clouds",
                "duration": 209.0,
                "thumbnail_url": "https://i.ytimg.com/vi/73E0BnFs7S4/hq720.jpg?sqp=-oaymwEcCOgCEMoBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLAQ4rl5Oe51cnH2ygSALoC-1Sl2Ww",
                "lyrics": "http://media-service.uz/track/public/73E0BnFs7S4/lyrics",
                "download_url": "http://media-service.uz/track/public/73E0BnFs7S4/download"
            },
            {
                "id": "PQg_Lsl0sWk",
                "title": "Daylight (Slowed + Reverb)",
                "performer": "David Kushner",
                "duration": 236.0,
                "thumbnail_url": "https://i.ytimg.com/vi/PQg_Lsl0sWk/hq720.jpg?sqp=-oaymwEcCOgCEMoBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLAnDh1UFmEp_BmpOnB2pgRJgsjocA",
                "lyrics": "http://media-service.uz/track/public/PQg_Lsl0sWk/lyrics",
                "download_url": "http://media-service.uz/track/public/PQg_Lsl0sWk/download"
            }
        ]
    }
    ```

- **400 Bad Request**: Agar so'rovda xatolik bo'lsa yoki noto'g'ri parametrlar yuborilgan bo'lsa.
    ```json
    {
        "status": "failed",
        "reason": "Error message"
    }
    ```

- **500 Internal Server Error**: Server ichki xatoligi yuz bergan bo'lsa.
    ```json
    {
        "status": "failed",
        "reason": "An internal server error occurred. Please try again later."
    }
    ```

### 9. `/recognize-from-facebook`, `/public/recognize-from-facebook`,

**Method:** `GET`

#### Query Parameters:

- `link` (string, majburiy): Facebook link

#### Response:

- **200 OK**: So'rov muvaffaqiyatli amalga oshirilsa.
    ```json
    {
        "status": "ok",
        "data": [
            {
                "id": "1aWeSyz2aj8",
                "title": "Unforgettable",
                "performer": "John Mcneill",
                "duration": 218.0,
                "thumbnail_url": "https://i.ytimg.com/vi/1aWeSyz2aj8/hq720.jpg?sqp=-oaymwEcCOgCEMoBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLCVjWCZarEAbmsjEcGMi_BTn9KEmQ",
                "lyrics": "http://media-service.uz/track/public/1aWeSyz2aj8/lyrics",
                "download_url": "http://media-service.uz/track/public/1aWeSyz2aj8/download"
            },
            {
                "id": "a-VHMf4VS70",
                "title": "July 6, 2024",
                "performer": "JimmyZN",
                "duration": 210.0,
                "thumbnail_url": "https://i.ytimg.com/vi/a-VHMf4VS70/hqdefault.jpg?sqp=-oaymwE2COADEI4CSFXyq4qpAygIARUAAIhCGAFwAcABBvABAfgB5gKAAugCigIMCAAQARhlIFooWjAP&rs=AOn4CLB3Q6OZUEYeyv6gR9pC-vKWwj8GDw",
                "lyrics": "http://media-service.uz/track/public/a-VHMf4VS70/lyrics",
                "download_url": "http://media-service.uz/track/public/a-VHMf4VS70/download"
            },
            {
                "id": "YBeTnPjdemI",
                "title": "January 12, 2024",
                "performer": "Troyce Hendricks",
                "duration": 210.0,
                "thumbnail_url": "https://i.ytimg.com/vi/YBeTnPjdemI/hqdefault.jpg?sqp=-oaymwE2COADEI4CSFXyq4qpAygIARUAAIhCGAFwAcABBvABAfgB5gKAAugCigIMCAAQARgTICsofzAP&rs=AOn4CLDlwUjIpvG3gdL2Hzfa1bE_HfuRSg",
                "lyrics": "http://media-service.uz/track/public/YBeTnPjdemI/lyrics",
                "download_url": "http://media-service.uz/track/public/YBeTnPjdemI/download"
            },
            {
                "id": "bXHqn44HhtI",
                "title": "Killing Me Softly",
                "performer": "William Marks - Topic",
                "duration": 267.0,
                "thumbnail_url": "https://i.ytimg.com/vi/bXHqn44HhtI/hq720.jpg?sqp=-oaymwEcCOgCEMoBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLBSqgWAPxafs85jSuw3gtkGmjvvuQ",
                "lyrics": "http://media-service.uz/track/public/bXHqn44HhtI/lyrics",
                "download_url": "http://media-service.uz/track/public/bXHqn44HhtI/download"
            },
            {
                "id": "KqNfz_B4vUc",
                "title": "paulunforgettable",
                "performer": "events by carla",
                "duration": 212.0,
                "thumbnail_url": "https://i.ytimg.com/vi/KqNfz_B4vUc/hq720.jpg?sqp=-oaymwEcCOgCEMoBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLBW0v1_1ak347_CeVRvJYTPUtbL_g",
                "lyrics": "http://media-service.uz/track/public/KqNfz_B4vUc/lyrics",
                "download_url": "http://media-service.uz/track/public/KqNfz_B4vUc/download"
            }
        ]
    }
    ```

- **400 Bad Request**: Agar so'rovda xatolik bo'lsa yoki noto'g'ri parametrlar yuborilgan bo'lsa.
    ```json
    {
        "status": "failed",
        "reason": "Error message"
    }
    ```

- **500 Internal Server Error**: Server ichki xatoligi yuz bergan bo'lsa.
    ```json
    {
        "status": "failed",
        "reason": "An internal server error occurred. Please try again later."
    }
    ```

### 10. `/public/{track}/download`

**Method:** `GET`

#### Path Parameters:

- `track` (string, majburiy): Track Id

#### Response:

- **200 OK**: So'rov muvaffaqiyatli amalga oshirilsa.
    ```
    Streaming response
    ```

- **400 Bad Request**: Agar so'rovda xatolik bo'lsa yoki noto'g'ri parametrlar yuborilgan bo'lsa.
    ```json
    {
        "status": "failed",
        "reason": "Error message"
    }
    ```

- **500 Internal Server Error**: Server ichki xatoligi yuz bergan bo'lsa.
    ```json
    {
        "status": "failed",
        "reason": "An internal server error occurred. Please try again later."
    }
    ```

### 11. `/{track}/download`

**Method:** `GET`

#### Path Parameters:

- `track` (string, majburiy): Track Id

#### Query Parameters:

- `bot_id` (string, majburiy): Bot id

#### Response:

- **200 OK**: So'rov muvaffaqiyatli amalga oshirilsa.
    ```json
    {
      "status": "ok",
      "data": {
          "chat_id": 0,
          "message_id": 0
      } 
    }
    ```

- **400 Bad Request**: Agar so'rovda xatolik bo'lsa yoki noto'g'ri parametrlar yuborilgan bo'lsa.
    ```json
    {
        "status": "failed",
        "reason": "Error message"
    }
    ```

- **500 Internal Server Error**: Server ichki xatoligi yuz bergan bo'lsa.
    ```json
    {
        "status": "failed",
        "reason": "An internal server error occurred. Please try again later."
    }
    ```

<hr>

## Twitter

### Endpoints

### 1. `/`, `/public`

**Method:** `GET`

#### Query Parameters:

- `link` (string, majburiy): Twitter link

#### Response:

- **200 OK**: So'rov muvaffaqiyatli amalga oshirilsa.
    ```json
    {
        "status": "ok",
        "data": {
            "type": "video",
            "post_id": "1841330673405063297",
            "title": "Text TRUMP to 88022",
            "download_url": "http://media-service.uz/twitter/public/1841330673405063297/download",
            "thumbnail_url": "https://pbs.twimg.com/amplify_video_thumb/1849833703096078336/img/a9_n30wYBH9dj3k7.jpg"
        }
    }
    ```

- **400 Bad Request**: Agar so'rovda xatolik bo'lsa yoki noto'g'ri parametrlar yuborilgan bo'lsa.
    ```json
    {
        "status": "failed",
        "reason": "Error message"
    }
    ```

- **500 Internal Server Error**: Server ichki xatoligi yuz bergan bo'lsa.
    ```json
    {
        "status": "failed",
        "reason": "An internal server error occurred. Please try again later."
    }
    ```

### 2. `/public/{post_id}/download`, `/public/{post_id}/{ind}/download`

**Method:** `GET`

#### Path Parameters:

- `post_id` (string, majburiy): Post Id
- `ind` (string, ixtyoriy): Post index

#### Response:

- **200 OK**: So'rov muvaffaqiyatli amalga oshirilsa.
    ```
    Streaming response
    ```

- **400 Bad Request**: Agar so'rovda xatolik bo'lsa yoki noto'g'ri parametrlar yuborilgan bo'lsa.
    ```json
    {
        "status": "failed",
        "reason": "Error message"
    }
    ```

- **500 Internal Server Error**: Server ichki xatoligi yuz bergan bo'lsa.
    ```json
    {
        "status": "failed",
        "reason": "An internal server error occurred. Please try again later."
    }
    ```

### 3. `{post_id}/download`, `/{post_id}/{ind}/download`

**Method:** `GET`

#### Path Parameters:

- `post_id` (string, majburiy): Post Id
- `ind` (string, ixtyoriy): Post index

#### Query Parameters:

- `bot_id` (string, majburiy): Bot id

#### Response:

- **200 OK**: So'rov muvaffaqiyatli amalga oshirilsa.
    ```json
    {
      "status": "ok",
      "data": {
          "chat_id": 0,
          "message_id": 0
      } 
    }
    ```

- **400 Bad Request**: Agar so'rovda xatolik bo'lsa yoki noto'g'ri parametrlar yuborilgan bo'lsa.
    ```json
    {
        "status": "failed",
        "reason": "Error message"
    }
    ```

- **500 Internal Server Error**: Server ichki xatoligi yuz bergan bo'lsa.
    ```json
    {
        "status": "failed",
        "reason": "An internal server error occurred. Please try again later."
    }
    ```

<hr>

## Video

### Endpoints

### 1. `/search`, `/public/search`

**Method:** `GET`

#### Query Parameters:

- `query` (string, majburiy): Qidirish uchun query
- `limit` (int, ixtyoriy): qidirish limiti
- `offset` (int, ixtyoriy): qidirish offseti

#### Response:

- **200 OK**: So'rov muvaffaqiyatli amalga oshirilsa.
    ```json
    {
        "status": "ok",
        "data": [
            {
                "id": "SoPxkuyuRN4",
                "title": "Jasmin - Salam (Premyera)",
                "channel": "August Records",
                "duration": 159.0,
                "thumbnail_url": "https://i.ytimg.com/vi/SoPxkuyuRN4/hq720.jpg?sqp=-oaymwEcCOgCEMoBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLDBaSJ37_euSIZ-TxB6peQj2QZeVw",
                "detail": "http://media-service.uz/video/public/SoPxkuyuRN4"
            },
            {
                "id": "wq-aO_FGoB0",
                "title": "SHOXRUX - SALOM [FT.SARVAR] 2006",
                "channel": "SHOXRUX TV",
                "duration": 219.0,
                "thumbnail_url": "https://i.ytimg.com/vi/wq-aO_FGoB0/hqdefault.jpg?sqp=-oaymwE2COADEI4CSFXyq4qpAygIARUAAIhCGAFwAcABBvABAfgB_gSAAuADigIMCAAQARhJIGUoXjAP&rs=AOn4CLDIRJvCaPAYr4qnJ6naJdqTPt1l7Q",
                "detail": "http://media-service.uz/video/public/wq-aO_FGoB0"
            },
            {
                "id": "UZHz3d8DHXA",
                "title": "Shohruhxon - Salom sevgi | Шохруххон - Салом севги",
                "channel": "RizaNovaUZ",
                "duration": 233.0,
                "thumbnail_url": "https://i.ytimg.com/vi/UZHz3d8DHXA/hq720.jpg?sqp=-oaymwEcCOgCEMoBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLAQVKMYbWkvO1Trghp2vEkl4dphKQ",
                "detail": "http://media-service.uz/video/public/UZHz3d8DHXA"
            },
            {
                "id": "M1RxN4VIdT4",
                "title": "‘‘Привет Дармаеди’’ (salom darmayedlar) 1-qism.         KATTA ISHKAL 😅",
                "channel": "MURAD BUXARSKIY 😂",
                "duration": 1347.0,
                "thumbnail_url": "https://i.ytimg.com/vi/M1RxN4VIdT4/hqdefault.jpg?sqp=-oaymwEcCOADEI4CSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLCM3k3ifG98gbnPRHGP7z9CwxGQTg",
                "detail": "http://media-service.uz/video/public/M1RxN4VIdT4"
            },
            {
                "id": "pP7vc_jmjpA",
                "title": "SARVAR - ABV (FT.SHOXRUX) 2006",
                "channel": "SHOXRUX TV",
                "duration": 190.0,
                "thumbnail_url": "https://i.ytimg.com/vi/pP7vc_jmjpA/hqdefault.jpg?sqp=-oaymwE2COADEI4CSFXyq4qpAygIARUAAIhCGAFwAcABBvABAfgB_gSAAuADigIMCAAQARhlIFUoUTAP&rs=AOn4CLAsx6m4iIuoFFaZGyuzOcrXfzn29g",
                "detail": "http://media-service.uz/video/public/pP7vc_jmjpA"
            },
            {
                "id": "PR8c1_A55XA",
                "title": "FINAL AYANCHLI YAKUN ! SALOM QO'SHNI BERKINMACHOQ #4 | HELLO NEIGHBOR HIDE AND SEEK",
                "channel": "SHOKH Play",
                "duration": 703.0,
                "thumbnail_url": "https://i.ytimg.com/vi/PR8c1_A55XA/hq720.jpg?sqp=-oaymwEcCOgCEMoBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLAU6hq1WfuWwdtpO5hBpvaJnEKmqw",
                "detail": "http://media-service.uz/video/public/PR8c1_A55XA"
            },
            {
                "id": "UrGQZRoyE5o",
                "title": "Салам родной Узбекистан, катта рахмат! За детство, юность и за взрослые года.",
                "channel": "GUDRIKSSON TV",
                "duration": 423.0,
                "thumbnail_url": "https://i.ytimg.com/vi/UrGQZRoyE5o/hq720.jpg?sqp=-oaymwEcCOgCEMoBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLAekSQ4IXVWq6Up-cn7vhD6jA2JTQ",
                "detail": "http://media-service.uz/video/public/UrGQZRoyE5o"
            },
            {
                "id": "baDJ-ZIvYy0",
                "title": "Anjelah Johnson - Nail Salon Uncut (Stand Up Comedy)",
                "channel": "Comedy Time",
                "duration": 528.0,
                "thumbnail_url": "https://i.ytimg.com/vi/baDJ-ZIvYy0/hqdefault.jpg?sqp=-oaymwEcCOADEI4CSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLDxgOHeybdfMJFCcQGuIDUe2EONvw",
                "detail": "http://media-service.uz/video/public/baDJ-ZIvYy0"
            },
            {
                "id": "ZjLTFOAYD_w",
                "title": "Diddy | ፒዲዲ ሚስጥሩን ዘረገፈው ተረክ ሚዛን Salon Terek",
                "channel": "salon tube",
                "duration": 1499.0,
                "thumbnail_url": "https://i.ytimg.com/vi/ZjLTFOAYD_w/hq720.jpg?sqp=-oaymwEcCOgCEMoBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLDGwPTIULEnUHbCGguUMxOgRlQepg",
                "detail": "http://media-service.uz/video/public/ZjLTFOAYD_w"
            },
            {
                "id": "jpi_SEdryLI",
                "title": "Hey Saloma salom - HD Video Song | ஹே சலோமா சலோம் | Subash | Arjun | Revathi | Vidyasagar",
                "channel": "Ayngaran",
                "duration": 326.0,
                "thumbnail_url": "https://i.ytimg.com/vi/jpi_SEdryLI/hq720.jpg?sqp=-oaymwEcCOgCEMoBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLDHyfbWC_gtV7ohi9kKsfjJEKghXA",
                "detail": "http://media-service.uz/video/public/jpi_SEdryLI"
            }
        ]
    }
    ```

- **400 Bad Request**: Agar so'rovda xatolik bo'lsa yoki noto'g'ri parametrlar yuborilgan bo'lsa.
    ```json
    {
        "status": "failed",
        "reason": "Error message"
    }
    ```

- **500 Internal Server Error**: Server ichki xatoligi yuz bergan bo'lsa.
    ```json
    {
        "status": "failed",
        "reason": "An internal server error occurred. Please try again later."
    }
    ```

### 2. `/public/{video_id}`, `{video_id}`

**Method:** `GET`

#### Path Parameters:

- `video_id` (string, majburiy): Video id

#### Response:

- **200 OK**: So'rov muvaffaqiyatli amalga oshirilsa.
    ```json
    {
        "status": "ok",
        "data": {
            "id": "jpi_SEdryLI",
            "title": "Hey Saloma salom - HD Video Song | ஹே சலோமா சலோம் | Subash | Arjun | Revathi | Vidyasagar",
            "duration": 326,
            "thumbnail_url": "https://i.ytimg.com/vi/jpi_SEdryLI/3.jpg",
            "download_url": "http://media-service.uz/video/public/jpi_SEdryLI/download"
        }
    }
    ```

- **400 Bad Request**: Agar so'rovda xatolik bo'lsa yoki noto'g'ri parametrlar yuborilgan bo'lsa.
    ```json
    {
        "status": "failed",
        "reason": "Error message"
    }
    ```

- **500 Internal Server Error**: Server ichki xatoligi yuz bergan bo'lsa.
    ```json
    {
        "status": "failed",
        "reason": "An internal server error occurred. Please try again later."
    }
    ```

### 3. `/public/{video_id}/download`

**Method:** `GET`

#### Path Parameters:

- `video_id` (string, majburiy): Video id

#### Response:

- **200 OK**: So'rov muvaffaqiyatli amalga oshirilsa.
    ```
    Streaming response
    ```

- **400 Bad Request**: Agar so'rovda xatolik bo'lsa yoki noto'g'ri parametrlar yuborilgan bo'lsa.
    ```json
    {
        "status": "failed",
        "reason": "Error message"
    }
    ```

- **500 Internal Server Error**: Server ichki xatoligi yuz bergan bo'lsa.
    ```json
    {
        "status": "failed",
        "reason": "An internal server error occurred. Please try again later."
    }
    ```

### 4. `{video_id}/download`

**Method:** `GET`

#### Path Parameters:

- `video_id` (string, majburiy): Video ID

#### Query Parameters:

- `bot_id` (string, majburiy): Bot id

#### Response:

- **200 OK**: So'rov muvaffaqiyatli amalga oshirilsa.
    ```json
    {
      "status": "ok",
      "data": {
          "chat_id": 0,
          "message_id": 0
      } 
    }
    ```

- **400 Bad Request**: Agar so'rovda xatolik bo'lsa yoki noto'g'ri parametrlar yuborilgan bo'lsa.
    ```json
    {
        "status": "failed",
        "reason": "Error message"
    }
    ```

- **500 Internal Server Error**: Server ichki xatoligi yuz bergan bo'lsa.
    ```json
    {
        "status": "failed",
        "reason": "An internal server error occurred. Please try again later."
    }
    ```

<hr>

## Youtube

### Endpoints

### 1. `/`, `/public`

**Method:** `GET`

#### Query Parameters:

- `link` (string, majburiy): TikTok video havolasi.

#### Response:

- **200 OK**: So'rov muvaffaqiyatli amalga oshirilsa.
    ```json
    {
        "status": "ok",
        "data": {
            "title": "Borliqqa Tikilgan MATEMATIKA [Texnoplov]",
            "thumbnail": "https://i.ytimg.com/vi/vSe-wPxUNCc/maxresdefault.jpg",
            "video_id": "vSe-wPxUNCc",
            "duration": 3263,
            "formats": [
                {
                    "format_id": "140",
                    "ext": "m4a",
                    "resolution": "audio",
                    "size_mb": "50.37 MB",
                    "download_url": "http://media-service.uz/youtube/public/vSe-wPxUNCc/140/download"
                },
                {
                    "format_id": "137",
                    "ext": "mp4",
                    "resolution": "1080p",
                    "size_mb": "503.49 MB",
                    "download_url": "http://media-service.uz/youtube/public/vSe-wPxUNCc/137/download"
                },
                {
                    "format_id": "136",
                    "ext": "mp4",
                    "resolution": "720p",
                    "size_mb": "173.59 MB",
                    "download_url": "http://media-service.uz/youtube/public/vSe-wPxUNCc/136/download"
                },
                {
                    "format_id": "135",
                    "ext": "mp4",
                    "resolution": "480p",
                    "size_mb": "106.92 MB",
                    "download_url": "http://media-service.uz/youtube/public/vSe-wPxUNCc/135/download"
                },
                {
                    "format_id": "134",
                    "ext": "mp4",
                    "resolution": "360p",
                    "size_mb": "64.68 MB",
                    "download_url": "http://media-service.uz/youtube/public/vSe-wPxUNCc/134/download"
                },
                {
                    "format_id": "133",
                    "ext": "mp4",
                    "resolution": "240p",
                    "size_mb": "35.44 MB",
                    "download_url": "http://media-service.uz/youtube/public/vSe-wPxUNCc/133/download"
                }
            ]
        }
    }
    ```

- **400 Bad Request**: Agar so'rovda xatolik bo'lsa yoki noto'g'ri parametrlar yuborilgan bo'lsa.
    ```json
    {
        "status": "failed",
        "reason": "Error message"
    }
    ```

- **500 Internal Server Error**: Server ichki xatoligi yuz bergan bo'lsa.
    ```json
    {
        "status": "failed",
        "reason": "An internal server error occurred. Please try again later."
    }
    ```

### 2. `/public/{video_id}/{format}/download`

**Method:** `GET`

#### Path Parameters:

- `video_id` (string, majburiy): Video id
- `format` (string, majburiy): video formati

#### Response:

- **200 OK**: So'rov muvaffaqiyatli amalga oshirilsa.
    ```
    Streaming response
    ```

- **400 Bad Request**: Agar so'rovda xatolik bo'lsa yoki noto'g'ri parametrlar yuborilgan bo'lsa.
    ```json
    {
        "status": "failed",
        "reason": "Error message"
    }
    ```

- **500 Internal Server Error**: Server ichki xatoligi yuz bergan bo'lsa.
    ```json
    {
        "status": "failed",
        "reason": "An internal server error occurred. Please try again later."
    }
    ```

### 3. `/{video_id}/{format}/download`

**Method:** `GET`

#### Path Parameters:

- `video_id` (string, majburiy): Video id
- `format` (string, majburiy): video formati

#### Query Parameters:

- `bot_id` (string, majburiy): Bot id

#### Response:

- **200 OK**: So'rov muvaffaqiyatli amalga oshirilsa.
    ```json
    {
      "status": "ok",
      "data": {
          "chat_id": 0,
          "message_id": 0
      } 
    }
    ```

- **400 Bad Request**: Agar so'rovda xatolik bo'lsa yoki noto'g'ri parametrlar yuborilgan bo'lsa.
    ```json
    {
        "status": "failed",
        "reason": "Error message"
    }
    ```

- **500 Internal Server Error**: Server ichki xatoligi yuz bergan bo'lsa.
    ```json
    {
        "status": "failed",
        "reason": "An internal server error occurred. Please try again later."
    }
    ```

<hr>

## Service

### Endpoints

### 1. `/register_bot`

**Method:** `POST`

#### Body Parameters:

```
{
    "bot_id": 0,
    "bot_username": "@usernamebot"
}
```

#### Response:

- **200 OK**: So'rov muvaffaqiyatli amalga oshirilsa.
    ```json
    {
        "status": "ok",
        "data": "Registered"
    }
    ```

- **400 Bad Request**: Agar so'rovda xatolik bo'lsa yoki noto'g'ri parametrlar yuborilgan bo'lsa.
    ```json
    {
        "status": "failed",
        "reason": "Error message"
    }
    ```

- **500 Internal Server Error**: Server ichki xatoligi yuz bergan bo'lsa.
    ```json
    {
        "status": "failed",
        "reason": "An internal server error occurred. Please try again later."
    }
    ```

### 2. `/config`

**Method:** `GET`

#### Response:

- **200 OK**: So'rov muvaffaqiyatli amalga oshirilsa.
    ```
    {
        "status": "ok",
        "data": {
            "PROXY": {
                "url": ""
            },
            "DOMAIN": {
                "url": "http://domain.com"
            },
            "API": {
                "url": "https://bgdrive.uz/api.php",
                "key": "894e9cfad4dw342de2511a35b6Sb8ba310e46f3f"
            },
            "TRACK": {
                "title_suffix": ""
            },
            "TELEGRAM": {
                "telegram_bot_api_url": "http://telegram-bot-api:8081",
                "channel_id": "-1002377526958",
                "token": "6703740556:AAEDqVxG_YyXqdwfB0wMtFzDDcB89vj7KWg",
                "username": "@tester_token_bot"
            }
        }
    }
    ```

- **400 Bad Request**: Agar so'rovda xatolik bo'lsa yoki noto'g'ri parametrlar yuborilgan bo'lsa.
    ```json
    {
        "status": "failed",
        "reason": "Error message"
    }
    ```

- **500 Internal Server Error**: Server ichki xatoligi yuz bergan bo'lsa.
    ```json
    {
        "status": "failed",
        "reason": "An internal server error occurred. Please try again later."
    }
    ```

### 3. `/redis`

**Method:** `GET`

#### Response:

- **200 OK**: So'rov muvaffaqiyatli amalga oshirilsa.
    ```
    Streaming response
    ```

- **400 Bad Request**: Agar so'rovda xatolik bo'lsa yoki noto'g'ri parametrlar yuborilgan bo'lsa.
  ```json
  {
      "status": "ok",
      "data": {
        "youtube-download-134--1002385063125": {
            "total_records": 1
        },
        "twitter-download-0": {
            "total_records": 1
        },
        "video-download--1002377526958": {
            "total_records": 1
        },
        "video-search": {
            "total_records": 1
        } 
      }
  }
  ```

- **500 Internal Server Error**: Server ichki xatoligi yuz bergan bo'lsa.
    ```json
    {
        "status": "failed",
        "reason": "An internal server error occurred. Please try again later."
    }
    ```

### 4. `/redis/flushall`

**Method:** `POST`

#### Response:

- **200 OK**: So'rov muvaffaqiyatli amalga oshirilsa.
    ```json
    {
        "status": "ok",
        "data": "Flush all data successfully"
    }
    ```

- **400 Bad Request**: Agar so'rovda xatolik bo'lsa yoki noto'g'ri parametrlar yuborilgan bo'lsa.
    ```json
    {
        "status": "failed",
        "reason": "Error message"
    }
    ```

- **500 Internal Server Error**: Server ichki xatoligi yuz bergan bo'lsa.
    ```json
    {
        "status": "failed",
        "reason": "An internal server error occurred. Please try again later."
    }
    ```

### 5. `/config/change`

**Method:** `POST`

#### Body Parameters:

```
{
    "SECTION": {
        "option": "new_value"
    }
}
```

#### Response:

- **200 OK**: So'rov muvaffaqiyatli amalga oshirilsa.
    ```json
    {
        "status": "ok",
        "data": "config successfully change"
    }
    ```

- **400 Bad Request**: Agar so'rovda xatolik bo'lsa yoki noto'g'ri parametrlar yuborilgan bo'lsa.
    ```json
    {
        "status": "failed",
        "reason": "Error message"
    }
    ```

- **500 Internal Server Error**: Server ichki xatoligi yuz bergan bo'lsa.
    ```json
    {
        "status": "failed",
        "reason": "An internal server error occurred. Please try again later."
    }
    ```

<hr>

