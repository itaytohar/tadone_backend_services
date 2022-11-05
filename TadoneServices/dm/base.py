# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker, Session
# from google.cloud import secretmanager
# import os

# PROJECT_ID = str(os.environ.get("PROJECTID"))
# KEY_VER = str(os.environ.get("KEYVERSION"))

# secrets = secretmanager.SecretManagerServiceClient()
# URL_STR = "projects/" + PROJECT_ID + "/secrets/ConStr/versions/" + KEY_VER
# tadone_db_conn_string = secrets.access_secret_version(request={"name": URL_STR}).payload.data.decode(
#     "utf-8"
# )
# #tadone_db_conn_string = "postgresql://tadone_user:tadone!best@localhost:5432/tadone"

# tadone_engine = create_engine(
#     tadone_db_conn_string,
#     connect_args={"sslmode": "disable"},
# )

# # use session_factory() to get a new Session
# _SessionFactory = sessionmaker(bind=tadone_engine)

# Base = declarative_base()

# Base.metadata.create_all(tadone_engine)


# def session_factory() -> Session:
#     return _SessionFactory()
