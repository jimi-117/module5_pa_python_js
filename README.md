# Simple recipe app
---
<pre>
/
├── backend/ (Django: Django Rest Framework)
│   ├── manage.py
│   ├── core/
│   └── api/
├── frontend/ (Svelte5: )
│   ├── package.json
│   ├── src/
│   └── public/
└── docker-compose.yml ( TODO )
</pre>
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
- sveltkit (BFF: Backend for frontend)

### Backend:
- uv
- python3.14
- django
- nox-uv
- pytest

