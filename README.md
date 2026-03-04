# Simple recipe app
---

/
├── backend/ (Django)
│   ├── manage.py
│   ├── core/
│   └── api/
├── frontend/ (Svelte5)
│   ├── package.json
│   ├── src/
│   └── public/
└── docker-compose.yml ( TODO )

## Architecture
- Communications: Rest API communication by using fetch or/and axios between frontend and backend
- Auth          : Token base auth with JWT
- CORS          : Need to set up to allow frontend's requests wih django-cors-headers

## Requirements
### Frontend:
- node.js
- volta
- pnpm
- svelte5
- express.js

### Backend:
- uv
- python3.14
- django
- nox-uv
- pytest

