# Jaswant Kondur - Portfolio & Blog

A modern, responsive portfolio and blog website built with Vue.js frontend and FastAPI backend, featuring a clean black and white aesthetic.

## 🚀 Features

- **Modern Design**: Clean, elegant black and white aesthetic
- **Responsive Layout**: Works seamlessly on desktop and mobile devices
- **Portfolio Showcase**: Display projects with images, descriptions, and links
- **Blog System**: Create and manage blog posts
- **Admin Panel**: Secure authentication system for content management
- **REST API**: FastAPI backend with PostgreSQL database
- **Docker Support**: Easy deployment with Docker Compose

## 🛠️ Tech Stack

### Frontend
- **Vue.js 3** - Progressive JavaScript framework
- **Vue Router** - Client-side routing
- **Tailwind CSS** - Utility-first CSS framework
- **Vite** - Fast build tool and dev server
- **Axios** - HTTP client for API calls

### Backend
- **FastAPI** - Modern Python web framework
- **SQLAlchemy** - SQL toolkit and ORM
- **PostgreSQL** - Relational database
- **JWT Authentication** - Secure token-based auth
- **Pydantic** - Data validation using Python type hints
- **Uvicorn** - ASGI server

### DevOps
- **Docker & Docker Compose** - Containerization
- **Git** - Version control

## 📁 Project Structure

```
portfolio-blog/
├── frontend/                 # Vue.js frontend application
│   ├── src/
│   │   ├── views/           # Vue components/pages
│   │   ├── api/             # API integration
│   │   ├── assets/          # Static assets
│   │   └── components/      # Reusable components
│   ├── public/              # Public assets
│   └── package.json         # Frontend dependencies
├── backend/                 # FastAPI backend application
│   ├── main.py             # FastAPI application entry point
│   ├── models.py           # Database models
│   ├── schemas.py          # Pydantic schemas
│   ├── crud.py             # Database operations
│   ├── auth.py             # Authentication logic
│   ├── config.py           # Configuration settings
│   └── pyproject.toml      # Backend dependencies
├── docker-compose.yml       # Docker services configuration
└── README.md               # Project documentation
```

## 🚀 Getting Started

### Prerequisites
- Docker and Docker Compose
- Node.js 16+ (for local frontend development)
- Python 3.13+ (for local backend development)

### Quick Start with Docker

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/portfolio-blog.git
   cd portfolio-blog
   ```

2. **Start the application**
   ```bash
   docker-compose up -d
   ```

3. **Access the application**
   - Frontend: http://localhost:5173
   - Backend API: http://localhost:8000
   - API Documentation: http://localhost:8000/docs

### Local Development

#### Backend Setup
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -e .
uvicorn main:app --reload --port 8000
```

#### Frontend Setup
```bash
cd frontend
npm install
npm run dev
```

## 🔐 Admin Access

To access the admin panel:

1. Navigate to `/admin`
2. Default credentials:
   - **Username**: `admin`
   - **Password**: `admin123`

⚠️ **Important**: Change these credentials in production by updating the environment variables.

## 📝 Environment Variables

Create a `.env` file in the backend directory:

```env
DATABASE_URL=postgresql://user:password@localhost:5432/portfolio_db
DB_USER=user
DB_PASSWORD=password
SECRET_KEY=your-secret-key-change-this-in-production
ADMIN_USERNAME=admin
ADMIN_PASSWORD=admin123
```

## 🎨 Customization

### Design Theme
The project uses a modern black and white aesthetic. You can customize colors by modifying:
- `frontend/src/App.vue` - Global CSS overrides
- Individual Vue components for component-specific styling

### Content Management
- **Portfolio Items**: Add/edit through the admin panel at `/admin`
- **Blog Posts**: Create and manage blog posts through the admin interface
- **Site Information**: Update site name and personal information in the Vue components

## 🚢 Deployment

### Docker Production Deployment
```bash
# Build and start services
docker-compose up -d --build

# View logs
docker-compose logs -f

# Stop services
docker-compose down
```

### Environment Configuration
Update the following for production:
- Change default admin credentials
- Set secure SECRET_KEY
- Configure production database
- Update CORS origins in `backend/main.py`

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Jaswant Kondur**
- Portfolio: [Your Portfolio URL]
- LinkedIn: [Your LinkedIn Profile]
- GitHub: [@yourusername](https://github.com/yourusername)

## 🙏 Acknowledgments

- Vue.js community for the amazing framework
- FastAPI for the excellent Python web framework
- Tailwind CSS for the utility-first CSS framework
- All open-source contributors who made this project possible

---

Built with ❤️ using Vue.js and FastAPI
