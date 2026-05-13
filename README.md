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

## 🧪 API Testing & Documentation

You can test the API using either the public Postman collection link or the local JSON file provided in the repository.

### Option 1: Public Postman Workspace (Recommended)
Access the live collection with pre-configured requests and documentation here:
👉 **[View Postman Collection](https://veronikanazaryk8-8421330.postman.co/workspace/%D0%92%D0%B5%D1%80%D0%BE%D0%BD%D1%96%D0%BA%D0%B0-%D0%9D%D0%B0%D0%B7%D0%B0%D1%80%D1%83%D0%BA's-Workspace~ff954802-733e-459e-8fed-fe28761077d4/collection/54805060-911e3c2c-f62e-43f6-985e-792f6c9c23fb?action=share&source=copy-link&creator=54805060)**

### Option 2: Local Import
1. Import the `travel_planner_collection.json` file from the root directory into your Postman app.
2. The collection includes automated tests for:
   - **Nested Creation**: Creating projects and places in a single call.
   - **Validation**: Testing against the Art Institute of Chicago API.
   - **Business Logic**: Verifying the 10-place limit and deletion protection for visited projects.

## 🚦 Quick Start

### 1. Environment Setup
Ensure you have Docker and Docker Compose installed.

```bash
# Clone the repository
git clone <your-repo-url>
cd TravelProject

# Build and start services
docker-compose up --build
