
```markdown
# APIproject
# 🌍 Capital City Time API

This API returns the current local time and UTC offset for a given **capital city**.  
It is protected by token-based authentication and deployed on a **Google Cloud Platform (GCP) VM**.

---

## ✅ Endpoint

```
[GET http://34.145.178.111:5000/api/time?city=CityName](http://34.145.178.111:5000/api/time?city=London)
```

---

## 🔐 Authorization

You **must** include a Bearer token in the request headers:

```
Authorization: supersecrettoken123
```

If the token is missing or incorrect, the API will respond with:

```json
{
  "error": "Unauthorized. Please provide a valid token."
}
```

---

## 📦 Example Request

```bash
curl -H "Authorization: Bearer supersecrettoken123" \
"http://34.145.178.111:5000/api/time?city=Tokyo"

```

---

## 📄 Example Response

```json
{
  "city": "London",
  "current_time": "2025-04-15 18:51:50",
  "utc_offset": "+01:00"
}
```

---

## ❌ Error Responses

| HTTP Code | Reason                                |
|-----------|----------------------------------------|
| 401       | Unauthorized (missing or invalid token) |
| 400       | Missing `city` parameter               |
| 404       | City not found in the database         |

---

## 🌐 Live API Info

- **Public IP:** `34.145.178.111`
- **Port:** `5000`
- **Sample Endpoint:**

```
http://34.145.178.111:5000/api/time?city=London
```

