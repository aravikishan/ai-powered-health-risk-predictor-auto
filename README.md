# AI-Powered Health Risk Predictor

## Overview
The AI-Powered Health Risk Predictor is a web application designed to provide users with personalized health risk assessments based on their demographic and health data. By leveraging AI algorithms, the application evaluates user inputs such as age, gender, weight, and height to determine potential health risks and offer tailored recommendations. This tool is particularly useful for individuals seeking to understand their health status and make informed lifestyle choices. Healthcare professionals and fitness enthusiasts can also benefit from the insights provided by this application.

## Features
- **User-Friendly Interface**: Intuitive and responsive web interface built with Bootstrap for seamless user experience.
- **Health Risk Assessment**: Calculates health risk levels based on user inputs such as age, gender, weight, and height.
- **Personalized Recommendations**: Provides actionable health tips and recommendations tailored to the user's risk level.
- **Data Persistence**: Stores user health data and assessment results in a SQLite database for future reference.
- **Informative Health Tips**: Offers general health tips to help users maintain a healthy lifestyle.
- **Dynamic Navigation**: Smooth scrolling and active state management for navigation links.

## Tech Stack
| Technology | Description |
|------------|-------------|
| Python     | Programming language for backend logic |
| FastAPI    | Web framework for building APIs |
| Uvicorn    | ASGI server for running FastAPI applications |
| Jinja2     | Templating engine for rendering HTML templates |
| Pydantic   | Data validation library |
| SQLite3    | Lightweight database for data storage |
| Bootstrap  | Frontend framework for responsive design |
| HTML/CSS/JS| Standard web technologies for frontend development |

## Architecture
The application follows a simple yet effective architecture where the FastAPI backend serves HTML templates rendered by Jinja2. User data is collected through forms and processed by FastAPI endpoints. The results are stored in an SQLite database. The frontend is styled using Bootstrap, and JavaScript is used for dynamic behaviors.

```plaintext
+-------------------+
|   User Interface  |
| (HTML/CSS/JS)     |
+---------+---------+
          |
          v
+---------+---------+
|    FastAPI        |
| (Backend Logic)   |
+---------+---------+
          |
          v
+---------+---------+
|    SQLite3        |
| (Database)        |
+-------------------+
```

## Getting Started

### Prerequisites
- Python 3.11+
- pip

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ai-powered-health-risk-predictor.git
   cd ai-powered-health-risk-predictor
   ```
2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application
1. Start the FastAPI application using Uvicorn:
   ```bash
   uvicorn app:app --reload
   ```
2. Open your web browser and visit `http://localhost:8000` to access the application.

## API Endpoints
| Method | Path                  | Description                                      |
|--------|-----------------------|--------------------------------------------------|
| GET    | `/`                   | Home page displaying welcome message             |
| GET    | `/assess`             | Page for inputting health data for assessment    |
| GET    | `/tips`               | Page displaying general health tips              |
| GET    | `/about`              | Page with information about the application      |
| POST   | `/api/health-risk`    | Endpoint for calculating health risk and storing data |
| GET    | `/api/tips`           | API endpoint returning health tips               |

## Project Structure
```
.
├── Dockerfile                # Docker configuration file for containerization
├── app.py                    # Main application file containing FastAPI logic
├── requirements.txt          # List of Python dependencies
├── start.sh                  # Shell script for starting the application
├── static                    # Directory for static files
│   ├── css
│   │   └── style.css         # Custom styles for the application
│   └── js
│       └── main.js           # JavaScript for dynamic behaviors
└── templates                 # Directory for HTML templates
    ├── about.html            # About page template
    ├── assess.html           # Health risk assessment page template
    ├── index.html            # Home page template
    └── tips.html             # Health tips page template
```

## Screenshots
*Screenshots of the application interface will be provided here.*

## Docker Deployment
To build and run the application using Docker:
1. Build the Docker image:
   ```bash
   docker build -t health-predictor .
   ```
2. Run the Docker container:
   ```bash
   docker run -p 8000:8000 health-predictor
   ```

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---
Built with Python and FastAPI.