# Travel Planner Service

A RESTful backend application designed to manage travel itineraries and curated points of interest. This project implements a robust integration with the **Art Institute of Chicago API** and enforces complex business constraints for trip planning.

## 🛠 Architecture & Tech Stack

- **Backend**: Django 5.x / Django REST Framework (DRF)
- **Environment**: Containerized with **Docker** & **Docker Compose**
- **Dependency Management**: [uv](https://github.com/astral-sh/uv) (high-performance Python package installer)
- **Database**: PostgreSQL
- **Third-Party Integration**: Real-time validation via the [Art Institute of Chicago API](https://api.artic.edu/docs/)

## 🏗 Key Technical Features

- **Nested Resources**: Implemented using `drf-nested-routers` for a clean `projects/{id}/places/` API structure.
- **Atomic Transactions**: Ensures project and place creation are handled safely in a single request.
- **External Validation**: Integrated custom serializer validation to verify `external_id` existence against the Chicago Art Institute database.
- **Business Constraints**:
    - **Capacity Limit**: Strict maximum of 10 places per project.
    - **Integrity Protection**: Projects with visited locations are protected from deletion.
    - **Dynamic Status**: Project completion is dynamically calculated based on the visited status of all linked places.

## 🚦 Quick Start

### 1. Environment Setup
Ensure you have Docker and Docker Compose installed.

```bash
# Clone the repository
git clone <your-repo-url>
cd TravelProject

# Build and start services
docker-compose up --build
