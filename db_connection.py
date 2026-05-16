from sqlalchemy import create_engine


#postgreSQL connection
engine= create_engine(
    "postgresql://postgres:abhi2621@localhost:5432/ecommerce_projects"
)

print("connection created successfully")
