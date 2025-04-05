# Yacine Live TV API

This is an unofficial api wrapper for yacineapp.tv in python. With this api you are able to browse tv categories and get stream links.

## API Reference

### 🛡️ Authorization Header

All endpoints require an API token to be passed in the request headers.

### Required Header:

| Header Name | Type   | Required | Description               |
|-------------|--------|----------|---------------------------|
| `Token` | string | ✅ Yes    | Your secret API token key |

### Example:

```http
GET /categories HTTP/1.1
Host: your-api-domain.com
Token: YOUR_API_TOKEN_HERE
```

#### Get all categories

```bash
  GET /categories
```

#### Get category channels

```bash
  GET /categories/${id}/channels
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of category  |

#### Get channel

```bash
  GET /channel/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of channel  |

#### Get all events

```bash
  GET /events
```

#### Get event by id

```bash
  GET /event/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of event  |

#### Search Endpoint

```bash
  GET /search?query=your_search_term
```

| Query Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `query`      | `string` | **Required**. The keyword to search by  |

## Run Locally

Clone the project

```bash
  git clone https://github.com/aimadnet/yacinetv-api
```

Go to the project directory

```bash
  cd yacinetv-api
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the FastAPI Application Server using:

```bash
  bash run.sh
```

## Feedback

If you have any feedback, contact me on telegram https://t.me/aimadnet

## Support Us

ETH: 0x7c0564bfCFe48ffCdee95ee137e33367C0077429